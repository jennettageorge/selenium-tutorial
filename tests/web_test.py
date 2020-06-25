#!/usr/bin/env python3

import pytest

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser():
    opts = Options()
    opts.headless = True
    driver = Firefox(options=opts)

    driver.implicitly_wait(10)

    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_greet_form(browser):
    user_name = "John"

    browser.get('http://localhost:5000/')

    form = browser.find_element_by_id("myform")
    name = browser.find_element_by_name("name")
    name.send_keys(user_name)

    form.submit()

    WebDriverWait(browser, 12).until(ec.url_matches('/greet'),
                                     'Timed out waiting for response')

    content = browser.page_source
    print(content)
    assert 'Hello John' in content
