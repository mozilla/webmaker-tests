#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import Base


class HomePage(Base):

    _page_title = 'Home - Mozilla Webmaker'
    _makes_templates_locator = (By.CSS_SELECTOR, 'DIV.make-now')

    def go_to_page(self):
        self.selenium.get(self.base_url + '/')
        self.is_the_current_page

    def makes_templates_present(self):
        return len(self.selenium.find_elements(*self._makes_templates_locator))
