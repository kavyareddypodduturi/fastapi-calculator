Perfect 👍 I’ll merge your README + add **Module 11 cleanly** (nothing extra, simple and professional).

---

### 👉 Replace your README.md with this (final version)

```markdown
# FastAPI Calculator Application

## Overview
This project is a simple FastAPI-based calculator that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

The application is designed with a strong focus on testing, security, and automation. It includes unit testing, integration testing, end-to-end testing, CI/CD using GitHub Actions, and Docker-based deployment.

---

## Features
- REST API built using FastAPI
- Supports basic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Interactive API interface using Swagger UI
- Logging implemented for tracking operations and errors
- Secure user model with password hashing
- Automated testing:
  - Unit Tests (pytest)
  - Integration Tests (SQLAlchemy + database)
  - End-to-End Tests (Playwright)
- Continuous Integration (CI) using GitHub Actions
- Docker containerization and deployment

---

## Project Structure

```

fastapi-calculator/

├── main.py
├── operations.py
├── requirements.txt
├── pytest.ini
├── README.md

├── app/
│   ├── models/
│   │   ├── user.py
│   │   └── calculation.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── calculation.py
│   ├── security/
│   │   └── password.py
│   └── database.py

├── tests/
│   ├── test_main.py
│   ├── test_operations.py
│   ├── unit/
│   │   └── test_calculation_schema.py
│   └── integration/
│       └── test_calculation_model.py

├── e2e/
│   └── test_e2e.py

├── .github/
│   └── workflows/
│       └── ci.yml

```

---

## Installation & Setup

### 1. Clone the repository
```

git clone [https://github.com/kavyareddypodduturi/fastapi-calculator.git](https://github.com/kavyareddypodduturi/fastapi-calculator.git)
cd fastapi-calculator

```

### 2. Create virtual environment
```

python3 -m venv venv
source venv/bin/activate

```

### 3. Install dependencies
```

pip install -r requirements.txt

```

---

## Running the Application

Start the FastAPI server:
```

uvicorn main:app --reload

```

Open in browser:
- API root: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

---

## Running Tests

Run all tests:
```

pytest

```

---

## Module 10 - Secure User Model & Deployment

### What was implemented
- SQLAlchemy User model with:
  - username (unique)
  - email (unique)
  - password_hash
  - created_at timestamp
- Pydantic schemas for validation
- Password hashing using bcrypt
- Unit and integration testing for user model
- CI pipeline using GitHub Actions
- Docker containerization and deployment

---

## Module 11 - Calculation Model & Validation

### What was implemented
- SQLAlchemy Calculation model with:
  - a, b (operands)
  - type (Add, Sub, Multiply, Divide)
  - result (optional)
- Pydantic schemas:
  - CalculationCreate (input validation)
  - CalculationRead (output serialization)
- Validations implemented:
  - Allowed operation types only
  - Division by zero is not allowed
- Unit tests for schema validation
- Integration test for database storage
- CI/CD pipeline updated to include calculation tests

---

## Docker Deployment

### Build Docker image
```

docker build -t kavyareddypodduturi/fastapi-calculator:latest .

```

### Push to Docker Hub
```

docker push kavyareddypodduturi/fastapi-calculator:latest

```

### Pull from Docker Hub
```

docker pull kavyareddypodduturi/fastapi-calculator:latest

```

Docker Hub Repository:  
https://hub.docker.com/r/kavyareddypodduturi/fastapi-calculator

---

## Continuous Integration (CI)

GitHub Actions is configured to:
- Install dependencies
- Install Playwright browsers
- Start FastAPI server
- Run all tests automatically on every push

---

## Learning Outcomes

This project demonstrates:
- Creating REST APIs using FastAPI
- Implementing secure user authentication (hashing)
- Using Pydantic for validation
- Writing unit, integration, and end-to-end tests
- Using Playwright for browser testing
- Setting up CI/CD using GitHub Actions
- Containerizing applications using Docker

---

## Conclusion

This project showcases a complete workflow from development to testing, security, and deployment. It demonstrates how to build reliable and scalable applications using modern tools and best practices.
```
