import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from api.users_api import UsersAPI
from utils.logger import get_logger


logger = get_logger("automation")

SCREENSHOT_DIR = Path("screenshots")
TRACE_DIR = Path("test-results/traces")
VIDEO_DIR = Path("test-results/videos")

SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
TRACE_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run Playwright with browser visible"
    )


@pytest.fixture
def page(request):

    logger.info(f"Starting UI test: {request.node.name}")

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=not request.config.getoption("--headed")
        )

        # Record video for the test.
        context = browser.new_context(
            record_video_dir=str(VIDEO_DIR)
        )

        # Start Playwright tracing.
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        logger.debug("Opening SauceDemo application")

        page.goto("https://www.saucedemo.com/")

        yield page

        failed = getattr(request.node, "test_failed", False)

        if failed:

            screenshot_path = (
                SCREENSHOT_DIR /
                f"failure_{request.node.name}.png"
            )

            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )

            logger.error(
                f"Failure screenshot saved: {screenshot_path}"
            )

            trace_path = (
                TRACE_DIR /
                f"{request.node.name}.zip"
            )

            context.tracing.stop(
                path=str(trace_path)
            )

            logger.error(
                f"Failure trace saved: {trace_path}"
            )

        else:
            # Stop tracing without saving a trace file.
            context.tracing.stop()

        # Video is finalized when the page/context closes.
        video = page.video

        context.close()

        if video:

            video_path = Path(video.path())

            if failed:
                final_video_path = (
                    VIDEO_DIR /
                    f"{request.node.name}.webm"
                )

                if video_path.exists() and video_path != final_video_path:
                    video_path.rename(final_video_path)

                logger.error(
                    f"Failure video saved: {final_video_path}"
                )

            else:
                # Retain video only when the test fails.
                if video_path.exists():
                    video_path.unlink()

        logger.info(
            f"Closing browser for test: {request.node.name}"
        )

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        if report.passed:
            item.test_failed = False
            logger.info(f"PASSED: {item.name}")

        elif report.failed:
            item.test_failed = True
            logger.error(f"FAILED: {item.name}")

        elif report.skipped:
            item.test_failed = False
            logger.warning(f"SKIPPED: {item.name}")


@pytest.fixture
def users_api():

    with sync_playwright() as p:

        request_context = p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com"
        )

        api = UsersAPI(request_context)

        yield api

        request_context.dispose()