import React from 'react';
import Navbar from '../components/Navbar';
import Sidebar from '../components/Sidebar';
import Dashboard from '../components/Dashboard';

const DashboardPage = () => (
  <div style={{ display: 'flex', height: '100vh' }}>
    <Sidebar />
    <div style={{ flexGrow: 1 }}>
      <Navbar />
      <Dashboard />
    </div>
  </div>
);

export default DashboardPage;
