Employee Directory API

A CRUD backend API for managing employee records using Python, FastAPI, SQLAlchemy, and SQLite.

Technologies

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

Project Structure

employee-directory-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
├── tests/
│   └── __init__.py
├── employee.db
├── requirements.txt
└── README.md

Setup

Create and use the virtual environment, then install dependencies:

venv\Scripts\python.exe -m pip install -r requirements.txt

Run the Application

venv\Scripts\python.exe -m uvicorn app.main:app --reload

After starting the server, open /docs to access the Swagger 
API documentation.

API Endpoints

Method	Endpoint	Description
POST	/employees	Add employee
GET	/employees	Get all employees
GET	/employees/{employee_id}	Get employee by ID
PUT	/employees/{employee_id}	Update employee
DELETE	/employees/{employee_id}	Delete employee

Employee Fields

* id
* name
* email
* phone
* department
* designation
* created_at

Validations

* Employee email must be unique.
* Required fields are validated.
* Invalid email formats are rejected.
* A non-existing employee returns 404.
* Duplicate email during creation or update returns 409.

Database

The application uses SQLite with the database file:

employee.db

The main table is:

employees

Testing

The API was tested using FastAPI Swagger UI, including:

* Create employee
* Get employees
* Get employee by ID
* Update employee
* Delete employee
* Duplicate email validation
* Invalid email validation
* Missing required field validation
* Employee not found validation