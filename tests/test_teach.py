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
class TestTeach(BaseTest):

    @pytest.mark.nondestructive
    def test_that_resources_page_display_makes(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        resources_page = home_page.header.click_teach_tab()
        Assert.greater(resources_page.teach_make_count, 0)
        Assert.true(resources_page.is_teach_makes_visible)
