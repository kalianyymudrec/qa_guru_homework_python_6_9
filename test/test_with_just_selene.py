from allure_commons.types import Severity
from selene import browser, by, be
import allure


@allure.story('just selene')
@allure.label("owner", "DanilaPanov")
@allure.tag('web')
@allure.severity(Severity.NORMAL)
def test_github():
    browser.open("https://github.com/")

    browser.element("#query-builder-test").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#81")).should(be.visible)

    browser.quit()
