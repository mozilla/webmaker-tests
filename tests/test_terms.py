#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage

@pytest.mark.xfail(reason="Bug 1029294 - Page title for home page is incorrect")
class TestTermsPage:

    @pytest.mark.nondestructive
    def test_terms_title(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        terms_page = home_page.footer.click_on_terms_page()
        Assert.equal(terms_page._page_title, terms_page.page_title)
