#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from base import Base


class HomePage(Base):

    _page_title = 'Home - Mozilla Webmaker'

    def go_to_page(self):
        self.selenium.get(self.base_url + '/')
        self.is_the_current_page
