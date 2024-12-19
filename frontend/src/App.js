import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import Home from './pages/Home';
import DashboardPage from './pages/DashboardPage';
import TrainingModulePage from './pages/TrainingModulePage';

const App = () => (
  <Router>
    <Navbar />
    <div style={{ display: 'flex' }}>
      <Sidebar />
      <div style={{ marginLeft: '200px', padding: '20px', flex: 1 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/training" element={<TrainingModulePage />} />
        </Routes>
      </div>
    </div>
  </Router>
);

export default App;
