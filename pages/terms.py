#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from base import Base


class TermsPage(Base):

    _page_title = u'Terms of Use - Mozilla Webmaker'

    def go_to_terms_page(self):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        terms_page = home_page.footer.click_on_terms_page()
        Assert.true(terms_page.is_the_current_page)
