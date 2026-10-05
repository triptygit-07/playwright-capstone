import pytest


@pytest.mark.regression
@pytest.mark.readonly
def test_multiple_windows(page):

    page.goto(
    "https://the-internet.herokuapp.com/windows",
    wait_until="domcontentloaded",
    timeout=60000
    )

    parent_url = page.url
    initial_page_count = len(page.context.pages)

    with page.context.expect_page() as new_page_info:
        page.get_by_role("link", name="Click Here").click()

    child_page = new_page_info.value
    child_page.wait_for_load_state()

    assert len(page.context.pages) == initial_page_count + 1
    assert parent_url == "https://the-internet.herokuapp.com/windows"
    assert "/windows/new" in child_page.url

    heading = child_page.get_by_role("heading", name="New Window")
    heading.wait_for(state="visible")

    assert heading.is_visible()
