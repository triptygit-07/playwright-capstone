import pytest

from utils.json_utils import deep_compare


@pytest.mark.readonly
def test_deep_json_comparison():

    actual = {
        "id": 1,
        "name": "Leanne Graham",
        "address": {
            "city": "Gwenborough",
            "zipcode": "92998-3874"
        }
    }

    expected = {
        "id": 1,
        "name": "Leanne Graham",
        "address": {
            "city": "Gwenborough",
            "zipcode": "92998-3874"
        }
    }

    # Exact JSON comparison
    assert actual == expected

    # Reusable deep JSON comparison
    matched, message = deep_compare(actual, expected)

    assert matched, message



@pytest.mark.readonly
def test_deep_json_comparison_reports_mismatch_path():

    actual = {
        "address": {
            "city": "Sunnyvale"
        }
    }

    expected = {
        "address": {
            "city": "San Jose"
        }
    }

    matched, message = deep_compare(actual, expected)

    assert matched is False
    assert "root.address.city" in message