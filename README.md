
---

```markdown
# FastAPI Calculator Application

## Overview
This project is a simple FastAPI-based calculator that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

The application is designed with a strong focus on testing and automation, including unit testing, integration testing, end-to-end testing, and continuous integration using GitHub Actions.

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
- Automated testing:
  - Unit Tests (pytest)
  - Integration Tests (FastAPI TestClient)
  - End-to-End Tests (Playwright)
- Continuous Integration (CI) using GitHub Actions

---

## Project Structure
```

fastapi-calculator/
│
├── main.py
├── operations.py
├── requirements.txt
├── pytest.ini
├── README.md
│
├── tests/
│   ├── test_main.py
│   └── test_operations.py
│
├── e2e/
│   └── test_e2e.py
│
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

## Using the API

1. Open `/docs`
2. Select any endpoint (example: `/add`)
3. Click **Try it out**
4. Enter values
5. Click **Execute**

Example:
```

a = 3
b = 4

```

Response:
```

{
"result": 7
}

```

---

## Running Tests

Run all tests:
```

pytest

```

Includes:
- Unit tests
- Integration tests
- End-to-end tests (Playwright)

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
- Writing unit, integration, and end-to-end tests
- Using Playwright for browser testing
- Implementing logging
- Setting up CI/CD using GitHub Actions

---

## Conclusion

This project showcases a complete workflow from development to testing and automation, ensuring the reliability and correctness of the application.
```

