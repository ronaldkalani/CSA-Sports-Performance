import React from 'react';
import Navbar from '../components/Navbar';
import Sidebar from '../components/Sidebar';

const Home = () => (
  <div style={{ display: 'flex', height: '100vh' }}>
    <Sidebar />
    <div style={{ flexGrow: 1 }}>
      <Navbar />
      <div style={{ padding: '20px' }}>
        <h1>Welcome to the Interactive Dashboard</h1>
        <p>
          Explore the features of this dashboard to view insights, manage data, and access training modules. Use the navigation menu to switch between pages.
        </p>
      </div>
    </div>
  </div>
);

export default Home;
