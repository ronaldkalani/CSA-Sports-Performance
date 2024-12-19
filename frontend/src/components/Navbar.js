import React from 'react';
import { AppBar, Toolbar, Typography } from '@mui/material';

const Navbar = () => (
  <AppBar position="static">
    <Toolbar>
      <Typography variant="h6" component="div" style={{ flexGrow: 1 }}>
        Dashboard & Training Module
      </Typography>
    </Toolbar>
  </AppBar>
);

export default Navbar;
