"# Frontend" 
# CSA-Sports-Performance Frontend

This is the **React.js frontend** for the CSA Sports Performance project, providing an interactive user interface with dashboards and training module components.

---

## Features

- **Dashboard**: Visualizes athlete performance data using charts and graphs.
- **Training Module**: Allows users to manage workshops and skill-tracking activities.
- **Interactive Design**: Built with modern UI components for a seamless user experience.

---

## Installation and Setup

### Prerequisites
- **Node.js**: Install the latest LTS version from [https://nodejs.org](https://nodejs.org).
- **npm**: Comes with Node.js.

### Steps
1. Clone the repository and navigate to the `frontend` directory:
   ```bash
   git clone https://github.com/ronaldkalani/CSA-Sports-Performance.git
   cd CSA-Sports-Performance/frontend
2. Install dependencies:
npm install

3. Start the development server:
npm start
The app will be available at http://localhost:3000.

API Integration
This frontend connects to the Flask backend for data. Ensure the backend is running at http://127.0.0.1:5000.

Example API Endpoints
Dashboard: Fetch skill data for the dashboard from /api/skills.
Training Module: Submit new workshops to /api/workshops.

Dependencies
Key dependencies used in this project:

React Router: For navigation between components.
Axios: For API communication.
Chart.js: For visualizing data.
Contribution
Contributions are welcome! Follow these steps:
1. Fork the repository and clone your fork locally.
2. Create a new branch for your changes:
git checkout -b feature-name
License
This project is licensed under the MIT License. See the main project LICENSE file for details.
 
