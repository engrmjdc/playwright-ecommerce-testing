# Playwright E-commerce Test Automation

[![Playwright Tests](https://github.com/engrmjdc/playwright-ecommerce-testing/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/engrmjdc/playwright-ecommerce-testing/actions/workflows/playwright-tests.yml)

An end-to-end test automation framework for [SauceDemo](https://www.saucedemo.com/) built with Python, pytest, and Playwright.

The project demonstrates maintainable UI automation through the Page Object Model, data-driven testing, reusable fixtures, failure evidence, HTML reporting, and continuous integration.

## Technology Stack

- Python
- Playwright
- pytest
- pytest-playwright
- pytest-html
- GitHub Actions
- Git and GitHub

## Test Coverage

The suite currently contains 11 automated test scenarios.

### Authentication

- Successful login with valid credentials
- Login rejection with invalid credentials
- Validation for a missing username
- Validation for a missing password

### Product Inventory

- Sort products by price from low to high
- Verify the displayed product prices are in ascending order

### Shopping Cart

- Add multiple products to the cart
- Verify product names and quantities
- Remove a product from the cart
- Verify the cart count and contents update correctly

### Checkout

- Complete a successful checkout
- Validate a missing first name
- Validate a missing last name
- Validate a missing postal code
- Verify invalid submissions cannot proceed to the order overview

## Project Structure

```text
playwright-ecommerce-testing/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
├── pages/
│   ├── __init__.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_inventory.py
│   └── test_login.py
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

## Framework Design

### Page Object Model

Page selectors and user interactions are stored in classes under `pages/`. Tests focus on scenarios and expected results instead of low-level browser operations.

### Reusable Fixtures

The `authenticated_page` fixture performs login setup for tests that require an authenticated user. Each test still receives an isolated browser context.

### Data-driven Testing

Pytest parameterization executes the same validation workflow with multiple datasets. It is currently used for invalid login and missing checkout information scenarios.

### Automatic Waiting

Playwright assertions automatically wait for expected UI conditions. This avoids unnecessary hard-coded delays and improves test reliability.

## Local Setup

### Prerequisites

Install:

- Python
- Git

Clone the repository:

```bash
git clone https://github.com/engrmjdc/playwright-ecommerce-testing.git
cd playwright-ecommerce-testing
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Install Chromium:

```bash
python -m playwright install chromium
```

## Running the Tests

Run the complete suite in headless mode:

```bash
pytest
```

Run with the browser visible:

```bash
pytest --headed
```

Run a specific test file:

```bash
pytest tests/test_checkout.py --headed
```

Run tests whose names match a keyword:

```bash
pytest -k checkout
```

## Reports and Failure Evidence

Every test run generates a self-contained HTML report:

```text
reports/report.html
```

Open it on Windows:

```powershell
Invoke-Item reports/report.html
```

When a test fails, Playwright retains diagnostic evidence under `test-results/`, including:

- Screenshot
- Browser video
- Playwright trace

Open a trace with:

```bash
python -m playwright show-trace path/to/trace.zip
```

Generated reports and evidence are excluded from Git because they are recreated during each test run.

## Continuous Integration

GitHub Actions runs the complete test suite automatically on:

- Pushes to `main`
- Pull requests targeting `main`

The workflow performs the following steps:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Installs Chromium
5. Runs the pytest suite
6. Uploads the HTML report and available failure evidence

The latest workflow status is displayed by the badge at the top of this README.

## Test Application

The application under test is [SauceDemo](https://www.saucedemo.com/), a public e-commerce demonstration website.

This repository is an independent portfolio project and is not affiliated with Sauce Labs.

## Future Improvements

- Move configuration and test credentials out of page and test classes
- Add product-detail validation
- Verify checkout prices and order totals
- Add logout and session tests
- Execute tests across Chromium, Firefox, and WebKit
- Add mobile viewport coverage
- Add accessibility checks
- Add API-assisted test setup
- Add code-quality checks

## Author

**Mack John Dela Cruz**

AI Test Engineer | Test Automation Engineer | Licensed Electronics Engineer

- [LinkedIn](https://www.linkedin.com/in/mackjohn-delacruz/)
- [GitHub](https://github.com/engrmjdc)
- Email: mjdelacruz.work@gmail.com