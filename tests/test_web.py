#!/usr/bin/env python3

import pytest

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def browser():

    opts = Options()
    opts.headless = True
    driver = Firefox(options=opts)

    driver.implicitly_wait(5)

    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_get_title(browser):
    browser.get("http://webcode.me")

    assert 'My html page' == browser.title
