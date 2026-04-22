# FastAPI Calculator Application

## Overview
This project is a FastAPI-based calculator application that supports arithmetic operations along with user authentication and database integration.

The application demonstrates a complete backend system with secure user handling, calculation CRUD operations, automated testing, CI/CD pipeline, and Docker deployment.

---

## Features
- User Authentication:
  - Register user
  - Login user (with hashed passwords)

- Calculation Operations (BREAD):
  - Browse (GET all calculations)
  - Read (GET by ID)
  - Add (POST new calculation)
  - Edit (PUT/PATCH calculation)
  - Delete (DELETE calculation)

- Built using FastAPI and SQLAlchemy
- Input validation using Pydantic
- Password hashing using bcrypt
- Swagger UI for API testing
- Automated testing:
  - Unit tests
  - Integration tests
  - End-to-End tests (Playwright)
- CI/CD using GitHub Actions
- Docker containerization

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

├── app/
│   ├── routes_user.py
│   └── routes_calculation.py

├── tests/
│   ├── test_main.py
│   ├── test_operations.py
│   ├── unit/
│   └── integration/
│       └── test_api_routes.py

├── e2e/
│   └── test_e2e.py

├── .github/workflows/ci.yml

```

---

## Installation & Setup

### Clone repository
```

git clone [https://github.com/kavyareddypodduturi/fastapi-calculator.git](https://github.com/kavyareddypodduturi/fastapi-calculator.git)
cd fastapi-calculator

```

### Create virtual environment
```

python3 -m venv venv
source venv/bin/activate

```

### Install dependencies
```

pip install -r requirements.txt

```

---

## Running the Application

```

uvicorn main:app --reload

```

Open:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

---

## Running Tests

```

python3 -m pytest -v

```

---

## API Testing (OpenAPI)

Use Swagger UI:

http://127.0.0.1:8000/docs

Verify:
- User register
- User login
- Calculation create
- Fetch calculations
- Update & delete operations

---

## End-to-End Testing Note

Playwright E2E tests require the FastAPI server to be running locally at:

http://127.0.0.1:8000

---

## CI/CD Pipeline

GitHub Actions is configured to:
- Install dependencies
- Run all tests (unit + integration + E2E)
- Ensure code quality on every push
- Build and push Docker image on success

---

## Docker Deployment

### Build Image
```

docker build -t kavyareddypodduturi/fastapi-calculator:latest .

```

### Push to Docker Hub
```

docker push kavyareddypodduturi/fastapi-calculator:latest

```

### Pull Image
```

docker pull kavyareddypodduturi/fastapi-calculator:latest

```

Docker Hub:
https://hub.docker.com/r/kavyareddypodduturi/fastapi-calculator

---

## Reflection (Summary)

In this project, I implemented user authentication and calculation CRUD operations using FastAPI, SQLAlchemy, and Pydantic. I learned how to securely handle user data using password hashing and how to validate API inputs effectively.

Writing integration tests helped me understand how different components (routes, database, and schemas) work together. Setting up GitHub Actions gave me hands-on experience with CI/CD pipelines, where tests run automatically on every commit.

One challenge I faced was fixing test failures in CI due to missing dependencies, which I resolved by updating the requirements file. Another challenge was handling Playwright E2E tests, which required running the FastAPI server separately.

Overall, this project helped me understand backend development, testing, and deployment in a practical way.

---

## Conclusion

This project demonstrates a complete backend system including API development, testing, security, CI/CD, and containerization. It reflects best practices in modern software development using FastAPI.
```
