```md
# FastAPI Calculator Application

## Overview
This project is a FastAPI-based calculator application that supports arithmetic operations along with user authentication, database integration, automated testing, CI/CD, and Docker deployment.

The application demonstrates a complete backend system using FastAPI, SQLAlchemy, Pydantic, Playwright, GitHub Actions, and Docker. It includes secure user authentication, calculation CRUD operations, reporting/statistics functionality, automated testing, and containerization.

---

## Features

### User Authentication
- Register user
- Login user
- Secure password hashing using bcrypt

### Calculation Operations (BREAD)
- Browse all calculations
- Read calculation by ID
- Add new calculation
- Edit/update calculation
- Delete calculation

### Calculation Statistics Dashboard
- View total calculations
- View total Add operations
- View total Subtract operations
- View highest calculation result
- View average calculation result

### Technologies Used
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite/PostgreSQL
- Playwright
- Pytest
- Docker
- GitHub Actions

### Testing
- Unit Testing
- Integration Testing
- End-to-End Testing (Playwright)

### CI/CD
- Automated GitHub Actions workflow
- Automatic testing on every push
- Docker image build and deployment

---

# Project Structure

```

fastapi-calculator/

├── main.py
├── operations.py
├── requirements.txt
├── pytest.ini
├── README.md
├── Dockerfile
├── docker-compose.yml

├── app/
│
│   ├── models/
│   │   ├── user.py
│   │   └── calculation.py
│
│   ├── schemas/
│   │   ├── user.py
│   │   ├── calculation.py
│   │   └── report.py
│
│   ├── security/
│   │   └── password.py
│
│   ├── routes_user.py
│   ├── routes_calculation.py
│   └── database.py

├── tests/
│
│   ├── test_main.py
│   ├── test_operations.py
│
│   ├── unit/
│   │   ├── test_calculation_schema.py
│   │   ├── test_password.py
│   │   ├── test_report_feature.py
│   │   └── test_user_schema.py
│
│   └── integration/
│       ├── test_api_routes.py
│       ├── test_calculation_model.py
│       ├── test_report_route.py
│       └── test_user_model.py

├── e2e/
│   ├── test_auth_e2e.py
│   ├── test_e2e.py
│   └── test_report_e2e.py

├── .github/
│   └── workflows/
│       └── ci.yml

````

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/kavyareddypodduturi/fastapi-calculator.git

cd fastapi-calculator
````

---

## Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

```bash
uvicorn main:app --reload
```

Open the following URLs:

* Main App:
  [http://127.0.0.1:8000](http://127.0.0.1:8000)

* Swagger UI:
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

# API Features

## User APIs

* Register User
* Login User

## Calculation APIs

* Add Calculation
* Get All Calculations
* Get Calculation By ID
* Update Calculation
* Delete Calculation

## Report API

* `/calculations/stats/report`

This route returns:

* Total calculations
* Total add operations
* Total subtract operations
* Highest result
* Average result

---

# Front-End Features

The application includes frontend pages for:

* User Login
* User Registration
* Calculation Operations
* Statistics Dashboard

The statistics dashboard displays:

* Total calculations
* Total add operations
* Total subtract operations
* Highest result
* Average result

A “Load Statistics” button dynamically fetches data using JavaScript Fetch API.

---

# Running Tests

## Run All Tests

```bash
python3 -m pytest -v
```

---

## Unit Tests

Includes:

* Schema validation tests
* Password hashing tests
* Statistics feature tests

Run:

```bash
python3 -m pytest tests/unit
```

---

## Integration Tests

Includes:

* API route testing
* Database integration testing
* Report route testing

Run:

```bash
python3 -m pytest tests/integration
```

---

## End-to-End Tests (Playwright)

Includes:

* Authentication flow testing
* Calculation UI testing
* Statistics dashboard testing

Run:

```bash
python3 -m pytest e2e
```

---

# Playwright E2E Testing Notes

Playwright tests validate:

* Frontend interactions
* User flows
* Statistics dashboard functionality

The E2E tests use:

* Chromium browser
* Headless execution
* HTML page interaction testing

---

# CI/CD Pipeline

GitHub Actions workflow automatically:

* Installs dependencies
* Runs unit tests
* Runs integration tests
* Runs Playwright E2E tests
* Verifies application functionality
* Builds Docker image
* Pushes Docker image to Docker Hub

This ensures continuous integration and automated testing on every push.

---

# Docker Deployment

## Build Docker Image

```bash
docker build -t kavyareddypodduturi/fastapi-calculator:latest .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 kavyareddypodduturi/fastapi-calculator:latest
```

---

## Push Docker Image

```bash
docker push kavyareddypodduturi/fastapi-calculator:latest
```

---

## Pull Docker Image

```bash
docker pull kavyareddypodduturi/fastapi-calculator:latest
```

---

# Docker Hub Repository

[https://hub.docker.com/r/kavyareddypodduturi/fastapi-calculator](https://hub.docker.com/r/kavyareddypodduturi/fastapi-calculator)

---

# Calculation Statistics Dashboard Feature

## Overview

As part of the final project enhancement, a new Calculation Statistics Dashboard feature was implemented.

This feature generates calculation reports and statistics directly from the database.

---

## Statistics Included

* Total number of calculations
* Total Add operations
* Total Subtract operations
* Highest calculation result
* Average calculation result

---

## Backend Implementation

Implemented using:

* FastAPI routes
* SQLAlchemy aggregate queries
* Pydantic response schemas

New API Route:

```


/calculations/stats/report


```

The route performs:

* Database querying
* Aggregation calculations
* JSON response generation

---

## Front-End Implementation

The frontend was extended by:

* Updating `calculations.html`
* Adding a “Load Statistics” button
* Displaying statistics dynamically using JavaScript

The frontend interacts with FastAPI APIs using Fetch API requests.

---

## Testing for Statistics Feature

### Unit Test

File:

* `test_report_feature.py`

Validates:

* Statistics schema
* Data correctness

### Integration Test

File:

* `test_report_route.py`

Validates:

* Report API route functionality

### End-to-End Test

File:

* `test_report_e2e.py`

Validates:

* Statistics UI rendering
* Frontend interaction flow

---

# Security Features

* Password hashing using bcrypt
* Input validation using Pydantic
* API validation using FastAPI
* Secure request handling

---

# Reflection

In this project, I implemented user authentication and calculation CRUD operations using FastAPI, SQLAlchemy, and Pydantic. I learned how to securely handle user data using password hashing and how to validate API inputs effectively.

Writing integration tests helped me understand how different components such as routes, databases, schemas, and frontend interactions work together. Setting up GitHub Actions gave me practical experience with CI/CD pipelines where tests run automatically on every commit.

One challenge I faced was fixing test failures in GitHub Actions due to missing dependencies and frontend Playwright issues. I resolved these by updating the requirements file and modifying E2E tests to work correctly in CI environments.

Additionally, I implemented a Calculation Statistics Dashboard feature that generates reports and statistics directly from the database. This helped me better understand SQLAlchemy aggregate queries, frontend API integration, automated testing, and full-stack workflow implementation.

Overall, this project improved my understanding of backend development, testing, API design, security practices, CI/CD workflows, Docker deployment, and software engineering best practices.

---

# Conclusion

This project demonstrates a complete backend and full-stack workflow including:

* FastAPI API development
* Database integration
* Authentication and security
* CRUD operations
* Reporting/statistics functionality
* Frontend integration
* Automated testing
* CI/CD pipeline setup
* Docker containerization

The project reflects modern software development practices using FastAPI, SQLAlchemy, Playwright, GitHub Actions, and Docker.

```
```
