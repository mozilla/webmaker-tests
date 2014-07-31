#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from base import Base


class ExplorePage(Base):

    _page_title = u'Explore - Mozilla Webmaker'

    def go_to_explore_page(self):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        explore_page = home_page.header.click_on_explore_tab()
