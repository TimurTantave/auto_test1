from playwright.sync_api import Page, expect
from faker import Faker


def test_login_with_invalid_credentials(page: Page):
    page.goto("http://2.26.162.45:8080/")
    # Предлагаю вынести в константу адрес, чтобы можно было легко поменять в будущем
    # и переиспользовать в других частях программы
    page.get_by_role("link", name="Login").click()
    expect(page.get_by_text("Authorization")).to_be_visible()
    # локаторы по тексту и by role не самые удачные, писал об этом в статье
    # там есть получше
    fake = Faker()

    login = fake.user_name()
    password = fake.password()

    page.get_by_test_id("login-username").fill(login)
    page.get_by_test_id("login-password").fill(password)
    page.get_by_test_id("login-submit").click()

    spinner = page.get_by_test_id("login-submit-spinner")
    expect(spinner).to_be_visible()
    # А давай без expect попробуем. В следующем задании его уже использовать не сможем
    # Потому что перейдем на PageObject, а в нем его использовать нельзя (писал об этом в статье про Page Object)
    expect(spinner).to_be_hidden()

    error = page.get_by_test_id("login-error-inline")
    expect(error).to_be_visible()
    expect(error).to_have_text("Invalid login or password.")
    # А тут заменим на assert. Только assert с сообщением, содержащим actual & expected result, это нужно для большей
    # информативности в случае ошибок
