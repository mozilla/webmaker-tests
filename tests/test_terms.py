#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.explore import ExplorePage
from pages.home import HomePage


class TestTermsPage:

    @pytest.mark.nondestructive
    def test_terms_title(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        terms_page = home_page.footer.click_on_terms_link()
        
        Assert.true(terms_page.is_page_title_visible)
        Assert.equal('Terms of Use - Mozilla Webmaker', terms_page._is_page_title_visible)
