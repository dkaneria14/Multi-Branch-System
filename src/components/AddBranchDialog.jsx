import React, { useState, useEffect } from "react";
import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";
import apiEndpoint from "../apiEndpoint";
import axios from "axios";

const AddBranchDialog = ({
  editMode,
  open,
  onClose,
  handleBranchChanges,
  branchToEdit,
}) => {
  const [branch_name, setBranchName] = useState("");
  const [branch_size, setBranchSize] = useState("");
  const postNewBranch = "http://127.0.0.1:8000/add_branch/";
  const editBranch = "http://127.0.0.1:8000/update_branch_size/";

  useEffect(() => {
    if (open) {
      if (editMode) {
        setBranchName(branchToEdit.branchLocation);
        setBranchSize(branchToEdit.branchSize);
      } else {
        // Reset the input fields when the dialog is opened
        setBranchName("");
        setBranchSize("");
      }
    }
  }, [open, editMode, branchToEdit]);

  const handleBranchLocationChange = (event) => {
    setBranchName(event.target.value);
  };

  const handleNumEmployeesChange = (event) => {
    setBranchSize(event.target.value);
  };

  const handleAddBranch = () => {
    const newBranch = {
      branchLocation: branch_name,
      branchSize: branch_size,
    };
    // POST - add new branch and get branchID and cashLimit
    axios
      .post(postNewBranch, newBranch)
      .then((response) => {
        // Handle the response data
        if (response) {
          handleBranchChanges(response.data);
        }
      })
      .catch((error) => {
        // Handle errors
        console.error("Error adding branch:", error);
      })
      .finally(() => {
        // window.location.reload();
      });
    onClose();
  };

  const handleConfirmUpdate = () => {
    axios
      .put(`${editBranch}${branchToEdit.branchID}/${branch_size}`)
      .then((response) => {
        // Handle the response data
        if (response) {
          handleBranchChanges(branchToEdit.branchID, response.data);
        }
      })
      .catch((error) => {
        // Handle errors
        console.error("Error deleting branch:", error);
      })
      .finally(() => {
        // window.location.reload();
      });
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle> {editMode ? "Edit Branch Details" : "Add New Branch"}</DialogTitle>
      <DialogContent>
        <DialogContentText>
          Please fill out the form below to add a new branch.
        </DialogContentText>
        <FormControl fullWidth sx={{ marginBottom: 2 }}>
          <InputLabel id="branch-location-label">Branch Name</InputLabel>
          <Select
            labelId="branch-location-label"
            id="branch-location"
            value={branch_name}
            onChange={handleBranchLocationChange}
            label="Branch Location"
            disabled={editMode}
          >
            <MenuItem value="Union">Union</MenuItem>
            <MenuItem value="Finch">Finch</MenuItem>
            <MenuItem value="Mississauga">Mississauga</MenuItem>
            <MenuItem value="Vaughan">Vaughan</MenuItem>
            <MenuItem value="Brampton">Brampton</MenuItem>
          </Select>
        </FormControl>
        <TextField
          fullWidth
          label="Number of Employees"
          type="number"
          value={branch_size}
          onChange={handleNumEmployeesChange}
          sx={{ marginBottom: 2 }}
        />
        {/* <DialogContentText>Branch Cash Limit: $30,000</DialogContentText> */}
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button
          onClick={editMode ? handleConfirmUpdate : handleAddBranch}
          color="primary"
        >
          {editMode ? "Update" : "Add"}
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default AddBranchDialog;
