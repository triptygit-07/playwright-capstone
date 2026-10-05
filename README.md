# Playwright Automation Capstone

A Python-based Playwright automation framework demonstrating UI automation, API testing, data-driven testing, reusable utilities, reporting, logging, parallel execution, and CI/CD using GitHub Actions.

## Tech Stack

- Python 3.12
- Playwright
- Pytest
- pytest-html
- pytest-xdist
- GitHub Actions

## Project Structure

```text
playwright-capstone/
├── api/
│   └── users_api.py
├── models/
│   └── user.py
├── pages/
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   └── products_page.py
├── test_data/
│   ├── login_data.json
│   ├── login_data.py
│   └── user_data.py
├── tests/
│   ├── api/
│   │   ├── test_json_comparison.py
│   │   └── test_users.py
│   └── ui/
│       ├── test_checkout.py
│       ├── test_login.py
│       ├── test_products.py
│       ├── test_session_storage.py
│       └── test_windows.py
├── utils/
│   ├── json_utils.py
│   ├── logger.py
│   └── session_storage.py
├── conftest.py
├── pytest.ini
└── requirements.txt


q


