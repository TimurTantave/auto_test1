from playwright.sync_api import Page, expect
from faker import Faker


def test_login_with_invalid_credentials(page: Page):
    page.goto("http://2.26.162.45:8080/")
    page.get_by_role("link", name="Login").click()
    expect(page.get_by_text("Authorization")).to_be_visible()

    fake = Faker()

    login = fake.user_name()
    password = fake.password()

    page.get_by_test_id("login-username").fill(login)
    page.get_by_test_id("login-password").fill(password)
    page.get_by_test_id("login-submit").click()

    spinner = page.get_by_test_id("login-submit-spinner")
    expect(spinner).to_be_visible()
    expect(spinner).to_be_hidden()

    error = page.get_by_test_id("login-error-inline")
    expect(error).to_be_visible()
    expect(error).to_have_text("Invalid login or password.")