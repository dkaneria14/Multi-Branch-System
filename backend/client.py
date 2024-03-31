import bank_service_pb2_grpc
import bank_service_pb2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import grpc
import json
from pydantic import BaseModel
import random


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you might want to restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def fetchJSONFile():
        file_path = 'db.json'

        with open(file_path, 'r') as file:
            json_string = file.read()

        data = json.loads(json_string)
        
        return data

def calculateCashRequirement( emp):
        if emp <50:
            branchMinCash = 50000
            
        if emp >= 50 and emp<= 100:
            branchMinCash = 100000
            
        if emp > 100:
            branchMinCash = 200000
        
        return branchMinCash
    

class BranchData(BaseModel):
    branchLocation: str
    branchSize: int

# Initialize gRPC stub
def initialize_stub():
    channel = grpc.insecure_channel('localhost:50051')
    return bank_service_pb2_grpc.GreeterStub(channel)

# Get total employees endpoint
@app.get("/total_employees/{branchID}")
async def get_total_employees(branchID: int):
    stub = initialize_stub()
    response = stub.GetTotalEmployees(bank_service_pb2.BankRequest(branchID=branchID))
    return {"total_employees": response.total_employees}

@app.post("/add_branch")
async def add_branch(branch_data: BranchData):
    data = fetchJSONFile()
    
    branchMinCash = calculateCashRequirement(branch_data.branchSize)
    
    branchID = random.randint(1000, 9999)


    new_branch = {
        "branchID": branchID,
        "branchSize": branch_data.branchSize,
        "branchLocation": branch_data.branchLocation,
        "branchMinCash": branchMinCash
    }
    
    data['Branches'].append(new_branch)
    
    with open('db.json', 'w') as file:
        json.dump(data, file, indent=2)
        
    return new_branch


# Update branch size endpoint
@app.put("/update_branch_size/{branchID}/{new_number_of_employees}")
async def update_branch_size(branchID: int, new_number_of_employees: int):
    stub = initialize_stub()
    response = stub.UpdateBranchSize(bank_service_pb2.UpdateBranchSizeRequest(branchID=branchID, newNumberOfEmployees=new_number_of_employees))
    
    return {
      "branchID": branchID,
      "branchSize": new_number_of_employees,
      "branchLocation": response.branchLocation,
      "branchMinCash": response.branchMinCash
    }

# get branch endpoint
@app.get("/get_all_branch")
async def get_all_branch():
    # Read the JSON data from the file
    file_path = 'db.json'
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Return all branches
    return data['Branches']

# get branch by id endpoint
@app.get("/get_branch_by_id/{branchID}")
async def get_all_branch(branchID: int):
    # Read the JSON data from the file
    file_path = 'db.json'
    
    with open(file_path, 'r') as file:
        data = json.load(file)

    for branch in data['Branches']:
        if branch['branchID'] == branchID:
            return branch
        
    
    return {"message":"Branch with the given ID not found"}

#Delete branch
@app.post("/delete_branch/{branchID}")
async def delete_branch_by_id(branchID: int):
     # Read the JSON data from the file
    file_path = 'db.json'
    print(branchID)
    with open(file_path, 'r') as file:
        data = json.load(file)

    deleteFlag = 0
    for branch in data['Branches']:
        if branch['branchID'] == branchID:
            data['Branches'].remove(branch)
            deleteFlag = 1
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    if deleteFlag == 0:
        return {"message" : "Delete unsuccessful"}
    else: 
        return {"message" : "Deleted successfully"}
            

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)