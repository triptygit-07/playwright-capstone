import pytest

from utils.session_storage import (
    write_session_storage,
    read_session_storage,
    save_session_storage,
    clear_session_storage,
    restore_session_storage,
    validate_session_storage,
)


@pytest.mark.regression
def test_session_storage_save_and_restore(page):

    # Write data to sessionStorage
    write_session_storage(page, "test_user", "standard_user")
    write_session_storage(page, "test_role", "qa")

    # Read and verify
    session_data = read_session_storage(page)

    assert session_data["test_user"] == "standard_user"
    assert session_data["test_role"] == "qa"

    # Save sessionStorage to session_data.json
    saved_data = save_session_storage(page)

    assert saved_data == session_data

    # Clear sessionStorage
    clear_session_storage(page)

    cleared_data = read_session_storage(page)

    assert cleared_data == {}

    # Restore sessionStorage from session_data.json
    restore_session_storage(page)

    # Validate restored data
    assert validate_session_storage(page, saved_data)