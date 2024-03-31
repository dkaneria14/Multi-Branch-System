from concurrent import futures
import json
from fastapi import FastAPI
from threading import Thread
from time import sleep, perf_counter
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor, as_completed
import random

import grpc
import bank_service_pb2_grpc
import bank_service_pb2

class GreeterServicer(bank_service_pb2_grpc.GreeterServicer):
    
    def fetchJSONFile(self, context):
        file_path = 'db.json'

        with open(file_path, 'r') as file:
            json_string = file.read()

        data = json.loads(json_string)
        
        return data
    
    
    def calculateCashRequirement(self, context, emp):
        if emp <50:
            cashReq = 50000
            
        if emp >= 50 and emp<= 100:
            cashReq = 100000
            
        if emp > 100:
            cashReq = 200000
        
        return cashReq
        
        
       
    def GetTotalEmployees(self, request, context):
        data = self.fetchJSONFile(context)       
        
        print(data)
        # Access the value of branch_size for each branch
        for branch in data['Branches']:
            if request.branchID == branch['branchID']:
                branchSize = branch['branchSize']
                print(f"Branch Size: {branchSize}")

        return bank_service_pb2.TotalEmployeesResponse(total_employees=int(branchSize))
    
    def GetCashRequirement(self, request, context):
        data = self.fetchJSONFile(context)
        
        for branch in data['Branches']:
            if request.branchID == branch['branchID']:
                cash_req = branch['branchMinCash']
                print(f"Cash req: {cash_req}")
        
        return bank_service_pb2.GetCashRequirementResponse(cash=cash_req)
    
    def UpdateBranchSize(self, request, context):
        data = self.fetchJSONFile(context)
        cashReq = self.calculateCashRequirement(context, request.newNumberOfEmployees)
        
        for branch in data['Branches']:
            if request.branchID == branch['branchID']:
                branch['branchMinCash'] = cashReq
                branch['branchSize'] = request.newNumberOfEmployees
                print(f"Updated Branch size: {branch['branchSize']}")
                print(f"Updated cash requirement: {branch['branchMinCash']}")
                branchID = branch['branchID']
                branchMinCash = branch['branchMinCash']
                branchLocation = branch['branchLocation']

        # Write the updated JSON data back to the file
        with open('db.json', 'w') as file:
            json.dump(data, file, indent=2)  # indent=2 for pretty printing

        return bank_service_pb2.UpdateBranchSizeResponse(branchID = branchID, branchMinCash = branchMinCash, branchLocation = branchLocation )

        
    
    def AddBranch(self, request, context):
        data = self.fetchJSONFile(context)
            
        cashReq = self.calculateCashRequirement(context, request.branchSize)
            
        branchID = random.randint(1000, 9999)

        new_branch = {
            "branchID": branchID,
            "branchSize": request.branchSize,
            "branchLocation": request.branchLocation,
            "branchMinCash": cashReq
        }
            
        data['Branches'].append(new_branch)
            
        with open('db.json', 'w') as file:
            json.dump(data, file, indent=2)

        print(branchID)
        # Return a BankAllAtributesResponse object with proper BranchID set
        return bank_service_pb2.BankAllAtributesResponse(branchID=branchID, branchSize=request.branchSize, branchLocation=request.branchLocation, branchMinCash=cashReq)

    
    def GetBranchesAll(self, request, context):
        # Read the JSON data from the file
        file_path = 'db.json'
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Convert JSON data into gRPC message type
        branches_backend = []
        for branch_data in data["Branches"]:
            branch = bank_service_pb2.BankAllAtributesResponse(
                branchID=branch_data["branchID"],
                branchSize=branch_data["branchSize"],
                branchLocation=branch_data["branchLocation"],
                branchMinCash=branch_data["branchMinCash"]
            )
            branches_backend.append(branch)

        # Create the response message
        response = bank_service_pb2.BranchesResponseAll(branches=branches_backend)

        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bank_service_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()