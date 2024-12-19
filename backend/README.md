CSA-Sports-Performance Backend

This is the backend of the CSA Sports Performance Platform, built using Django and Django REST Framework (DRF). It provides APIs for managing workshops, skill tracking, feedback, and more.

Features
Workshops: CRUD operations for managing workshops.
Skill Tracking: Track and update athlete skills.
Feedback: Submit and retrieve feedback.
Authentication: Secure user authentication and authorization (future implementation).
Scalable Design: Built with Django’s robust framework for scalability.

Technology Stack
Backend Framework: Django 5.1.4
API Development: Django REST Framework
Database: SQLite (default, can be switched to PostgreSQL/MySQL in production)
Hosting: AWS
Language: Python 3.12

Project Structure
backend/
├── backend/                  # Django project folder
│   ├── __init__.py           # Package initialization
│   ├── asgi.py               # ASGI configuration
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI configuration
├── manage.py                 # Django CLI entry point
├── db.sqlite3                # SQLite database file
└── apps/
    ├── workshops/            # Workshop management app
    ├── skills/               # Skill tracking app
    └── feedback/             # Feedback management app

Getting Started
Setup

1. Clone the Repository:
git clone https://github.com/ronaldkalani/CSA-Sports-Performance.git
cd CSA-Sports-Performance/backend

2. Install Dependencies
Ensure Python is installed, then install the required dependencies:
pip install -r requirements.txt

3. Apply Database Migrations
Set up the database:
python manage.py migrate

4. Run the Development Server
Start the server locally:
python manage.py runserver

5. Access the APIs
Use a browser or API client (e.g., Postman) to interact with the APIs at:
http://127.0.0.1:8000/

API Endpoints
Workshops
Method	  Endpoint	           Description
GET	     /workshops/	        Retrieve all workshops
POST	     /workshops/	        Create a new workshop
GET	     /workshops/<id>/	  Retrieve a specific workshop
PUT	     /workshops/<id>/	  Update a specific workshop
DELETE	  /workshops/<id>/	  Delete a specific workshop

Skill Tracking
Method	       Endpoint	         Description
GET          	 /skills/	         Retrieve all skill data
PUT	          /skills/<id>/    	Update skill data for an athlete

Feedback
Method	      Endpoint	           Description
POST	         /feedback/	        Submit feedback
GET	         /feedback/	        Retrieve all feedback

Development
Run Tests
Run tests to ensure everything works as expected:
python manage.py test

Create a Superuser
To access Django’s admin interface:
python manage.py createsuperuser

Access the admin panel at:
http://127.0.0.1:8000/admin/

Deployment
1. Update Settings for Production
Set DEBUG = False in settings.py.
Configure ALLOWED_HOSTS with your domain or server IP.
2. Use a Production-Ready Database
Switch to a production database like PostgreSQL or MySQL by updating DATABASES in settings.py.

3. Collect Static Files
Prepare static files for production:
python manage.py collectstatic

4. Deploy
Deploy AWS Elastic Beanstalk platform.

Contributors
Ronald Kalani - Developer and Maintainer

License
This project is licensed under the GPL-2.0 License.








