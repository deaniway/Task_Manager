import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


def test_signIn_signOut(browser):

    page = browser.new_page()
    page.goto("http://127.0.0.1:8000/")

    page.wait_for_selector('text="Вход"')

    assert page.query_selector('text="Вход"') is not None

    page.click('text="Вход"')

    page.wait_for_selector('text="Выход"')
    assert page.query_selector('text="Выход"') is not None
    page.click('text="Выход"')


if __name__ == "__main__":
    pytest.main(["-s", "test_translations.py"])
