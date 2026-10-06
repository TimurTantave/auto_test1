from playwright.sync_api import Page, expect
from faker import Faker

Base_URL = "http://2.26.162.45:8080/"


def test_login_with_invalid_credentials(page: Page):
    page.goto(Base_URL)
    page.get_by_test_id("nav-login").click()
    expect(page.get_by_test_id("login-title")).to_be_visible()

    fake = Faker()

    login = fake.user_name()
    password = fake.password()

    page.get_by_test_id("login-username").fill(login)
    page.get_by_test_id("login-password").fill(password)
    page.get_by_test_id("login-submit").click()

    spinner = page.get_by_test_id("login-submit-spinner")
    spinner.wait_for(state="visible")
    spinner.wait_for(state="hidden")

    error = page.get_by_test_id("login-error-inline")
    expect(error).to_be_visible()

    actual_error = error.inner_text()
    expected_error = "Invalid login or password."

    assert actual_error == expected_error, (
        f"Expected error: '{expected_error}', "
        f"but actual error was: '{actual_error}'"
    )
