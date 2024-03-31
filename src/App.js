import React, { useEffect, useState } from "react";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import HomePage from "./components/HomePage";
import AddBranchDialog from "./components/AddBranchDialog";
import apiEndpoint from "./apiEndpoint";
import axios from "axios";

const theme = createTheme({
  palette: {
    primary: {
      main: "#2c3e50", // Matching the previous UI primary color
    },
    secondary: {
      main: "#27ae60", // Matching the previous UI secondary color
    },
    // Custom green color palette
    green: {
      main: "#2ecc71",
      dark: "#27ae60",
      light: "#4caf50",
    },
  },
});

const App = () => {
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [branches, setBranches] = useState([]);
  const getAllBranches = "http://127.0.0.1:8000/get_all_branch/";

  useEffect(() => {
    // Load all the branches from the backend
    axios({
      method: "get",
      url: `${getAllBranches}`,
    })
      .then((response) => {
        if (response.data == null) {
          setBranches([]);
        } else {
          setBranches(response.data);
        }
      })
      .catch((error) => {
        // Handle any errors here
        console.error("Error fetching all branch info:", error);
      });

  }, [])

  const handleOpenDialog = () => {
    setIsDialogOpen(true);
  };

  const handleCloseDialog = () => {
    setIsDialogOpen(false);
  };

  const handleBranchAdded = (newBranch) => {
    setBranches([...branches, newBranch]);
  };

  const updateBranches = (updatedBranches) => {
    setBranches(updatedBranches);
  };

  return (
    <ThemeProvider theme={theme}>
      <div>
        <HomePage
          branches={branches}
          onOpenDialog={handleOpenDialog}
          updateBranches={updateBranches}
        />
        <AddBranchDialog
          open={isDialogOpen}
          editMode={false}
          onClose={handleCloseDialog}
          handleBranchChanges={handleBranchAdded}
        />
      </div>
    </ThemeProvider>
  );
};

export default App;
