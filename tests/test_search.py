#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
from unittestzero import Assert

from pages.base import Base
from pages.home import HomePage


class TestSearch:

    @pytest.mark.nondestructive
    def test_main_search(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        search_page = home_page.header.go_to_search_page()
        search_page.search('QWERTY')
        Assert.equal(search_page.search_query, 'QWERTY')
