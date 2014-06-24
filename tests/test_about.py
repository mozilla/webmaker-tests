#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
from unittestzero import Assert

from pages.home import HomePage
from tests.base_test import BaseTest


@pytest.mark.xfail("'mofostaging.net' in config.getvalue('base_url')",
       reason="Bug 1029294 - Page title for home page is incorrect")
class TestAbout(BaseTest):

    @pytest.mark.nondestructive
    def test_that_about_page_displays_hello_message(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        about_page = home_page.header.go_to_info_page()
        Assert.true(about_page.is_hello_message_visible)
