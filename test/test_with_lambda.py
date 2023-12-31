from allure_commons.types import Severity
from selene import browser, by, be
import allure


@allure.label("owner", "DanilaPanov")
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.story('with selene steps')
def test_github():
    with allure.step("Открываем главую страницу GitHub"):
        browser.open("https://github.com/")

    with allure.step("Открываем репозиторий eroshenkoam/allure-example"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step("Кликаем по ссылке репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Находим Issue  с номером #81"):
        browser.element(by.partial_text("#81")).should(be.visible)

    with allure.step("Закрываем браузер"):
        browser.quit()
