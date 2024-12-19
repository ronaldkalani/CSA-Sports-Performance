import React from 'react';
import { List, ListItem, ListItemText } from '@mui/material';
import { Link } from 'react-router-dom';

const Sidebar = () => (
  <div style={{ width: '200px', height: '100vh', background: '#f4f4f4' }}>
    <List>
      <ListItem button component={Link} to="/">
        <ListItemText primary="Home" />
      </ListItem>
      <ListItem button component={Link} to="/dashboard">
        <ListItemText primary="Dashboard" />
      </ListItem>
      <ListItem button component={Link} to="/training">
        <ListItemText primary="Training Module" />
      </ListItem>
    </List>
  </div>
);

export default Sidebar;
