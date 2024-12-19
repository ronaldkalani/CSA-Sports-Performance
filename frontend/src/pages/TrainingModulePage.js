import React from 'react';
import Navbar from '../components/Navbar';
import Sidebar from '../components/Sidebar';
import TrainingModule from '../components/TrainingModule';

const TrainingModulePage = () => (
  <div style={{ display: 'flex', height: '100vh' }}>
    <Sidebar />
    <div style={{ flexGrow: 1 }}>
      <Navbar />
      <TrainingModule />
    </div>
  </div>
);

export default TrainingModulePage;
