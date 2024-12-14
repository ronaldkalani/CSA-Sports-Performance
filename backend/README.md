# CSA Sports Performance Backend

The CSA Sports Performance Backend is developed using Flask and provides APIs to manage workshops, track skills, and collect feedback. It serves as the backend service for the CSA Sports Performance platform, aimed at enhancing athletic performance.

## Project Structure

The project is organized as follows:
backend/ ├── app.py # Main application entry point ├── database.py # Database connection and session handling ├── models.py # Database models ├── requirements.txt # Python dependencies ├── routes/ # API route definitions │ ├── feedback.py # Routes for feedback │ ├── skill_tracking.py # Routes for skill tracking │ ├── workshops.py # Routes for workshops └── README.md # Project documentation

## Features

- **Workshops Management**: APIs to create, retrieve, and manage workshops.
- **Skill Tracking**: APIs to track and retrieve data related to athlete skill development.
- **Feedback System**: APIs to collect and view feedback from users.

## Setup Instructions

### Prerequisites

To set up and run this backend, you will need the following:
- Python 3.7 or higher
- `pip`, the Python package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ronaldkalani/CSA-Sports-Performance.git
   cd CSA-Sports-Performance/backend
2.  Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.  Install the required dependencies:
pip install -r requirements.txt

Running the Application
1. Start the Flask application:
python app.py

2. Open a web browser or API testing tool like Postman and access the application at:
http://127.0.0.1:5000

API Endpoints
Workshops
     GET /workshops - Retrieve a list of workshops.
Skill Tracking
     GET /skill-tracking - Retrieve skill tracking data.
Feedback
     GET /feedback - Retrieve feedback from users.

Contributing
Contributions to this project are welcome. To contribute:
1. Fork the repository to your GitHub account.
2. Clone your fork to your local machine:
git clone https://github.com/your-username/CSA-Sports-Performance.git

3. Create a new branch for your feature or bug fix:
git checkout -b feature-name

4. Make your changes and commit them:
git commit -m "Add feature-name"

5. Push the branch to your fork:
git push origin feature-name

6. Open a pull request to the main repository.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This project is developed as part of the CSA Sports Performance initiative to support athlete development through technology.

