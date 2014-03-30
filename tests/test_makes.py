#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage


class TestMakes:

    @pytest.mark.nondestructive
    def test_verify_make_page_display(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        makes_page = home_page.header.click_on_make_tab()
        Assert.greater(makes_page.starter_makes_count, 0)
