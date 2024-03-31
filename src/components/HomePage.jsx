import React, { useState } from "react";
import {
  AppBar,
  Button,
  Grid,
  IconButton,
  Toolbar,
  Typography,
  Card,
  CardContent,
  CardActions,
  Box,
} from "@mui/material";
import { Delete, Edit, Add } from "@mui/icons-material";
import DeleteBranchDialog from "./DeleteBranchDialog";
import axios from "axios";
import AddBranchDialog from "./AddBranchDialog";

const HomePage = ({ branches, onOpenDialog, updateBranches }) => {
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [editDialogOpen, setEditDialogOpen] = useState(false);
  const [deleteBranchID, setDeletingBranchID] = useState(null);
  const [editBranch, setEditBranch] = useState(null);
  const deleteBranch = "http://127.0.0.1:8000/delete_branch/";

  const handleDeleteBranch = (branchID) => {
    setDeletingBranchID(branchID);
    setDeleteDialogOpen(true);
  };

  const handleEditBranch = (branch) => {
    setEditBranch(branch);
    setEditDialogOpen(true);
  };

  const handleConfirmDelete = () => {
    const updatedBranches = branches.filter(
      (branch, index) => branch.branchID !== deleteBranchID
    );
    // POST - delete branch

    axios
      .post(deleteBranch + deleteBranchID)
      .then((response) => {
        // Handle the response data
        console.log("Response:", response.data.message);
      })
      .catch((error) => {
        // Handle errors
        console.error("Error deleting branch:", error);
      })
      .finally(() => {
        // window.location.reload();
      });

    updateBranches(updatedBranches);
    setDeletingBranchID(null);
    setDeleteDialogOpen(false);
  };

  const handleConfirmEdit = (branchId, newBranch) => {
    const updatedBranches = branches.map(branch => {
      if (branch.branchID === branchId) {
        // Update employee count if branchId matches
        return { ...branch, branchSize: newBranch.branchSize, branchMinCash: newBranch.branchMinCash  };
      }
      return branch; // Keep the branch unchanged if branchId doesn't match
    });

    updateBranches(updatedBranches); // Update the state with the modified array
    setEditDialogOpen(false);
  };

  return (
    <>
      <AppBar position="static">
        <Toolbar sx={{ justifyContent: "space-between" }}>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Multi-Branch Bank System
          </Typography>
          <Button
            variant="contained"
            color="secondary"
            startIcon={<Add />}
            onClick={onOpenDialog}
          >
            New Branch
          </Button>
        </Toolbar>
      </AppBar>
      <Box sx={{ overflow: "auto", marginTop: 1, padding: 2 }}>
        <Grid container spacing={3} justifyContent="center">
          {branches.map((branch, index) => (
            <Grid key={index} item xs={12} sm={6} md={4} lg={3}>
              <Card
                sx={{
                  height: "100%",
                  transition: "transform 0.3s",
                  "&:hover": { transform: "scale(1.05)" },
                  backgroundColor: "#f0f0f0",
                }}
              >
                <CardContent>
                  <Typography gutterBottom variant="h5" component="div">
                    {branch.branchLocation}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Branch ID: {branch.branchID}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Number of Employees: {branch.branchSize}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Minimum Cash Requirement: {branch.branchMinCash}
                  </Typography>
                </CardContent>
                <CardActions sx={{ justifyContent: "space-between" }}>
                  <IconButton
                    aria-label="edit"
                    onClick={() => handleEditBranch(branch)}
                  >
                    <Edit />
                  </IconButton>
                  <IconButton
                    aria-label="delete"
                    onClick={() => handleDeleteBranch(branch.branchID)}
                  >
                    <Delete />
                  </IconButton>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Box>
      <DeleteBranchDialog
        open={deleteDialogOpen}
        onClose={() => setDeleteDialogOpen(false)}
        onConfirmDelete={handleConfirmDelete}
      />
      <AddBranchDialog
        editMode={true}
        open={editDialogOpen}
        onClose={() => setEditDialogOpen(false)}
        branchToEdit={editBranch}
        handleBranchChanges={handleConfirmEdit}
      />
    </>
  );
};

export default HomePage;
