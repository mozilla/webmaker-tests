#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage

class TestExplorePage:

    @pytest.mark.xfail(reason="Bug 1029294 - Page title for home page is incorrect")
    @pytest.mark.nondestructive
    def test_explore_title(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        explore_page = home_page.header.click_on_explore_tab()
        Assert.equal(explore_page._page_title, explore_page.page_title)
