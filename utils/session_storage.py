import json
from pathlib import Path


SESSION_FILE = Path("session_data.json")


def write_session_storage(page, key, value):
    page.evaluate(
        """([key, value]) => {
            sessionStorage.setItem(key, value);
        }""",
        [key, value]
    )


def read_session_storage(page):
    return page.evaluate(
        """() => Object.fromEntries(
            Object.entries(sessionStorage)
        )"""
    )


def save_session_storage(page, file_path=SESSION_FILE):
    session_data = read_session_storage(page)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(session_data, file, indent=2)

    return session_data


def clear_session_storage(page):
    page.evaluate("() => sessionStorage.clear()")


def restore_session_storage(page, file_path=SESSION_FILE):
    with open(file_path, "r", encoding="utf-8") as file:
        session_data = json.load(file)

    page.evaluate(
        """(data) => {
            for (const [key, value] of Object.entries(data)) {
                sessionStorage.setItem(key, value);
            }
        }""",
        session_data
    )


def validate_session_storage(page, expected_data):
    actual_data = read_session_storage(page)

    return actual_data == expected_data