#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.base import Base


class ResourcesPage(Base):

    _page_title = 'Teach - Mozilla Webmaker'

    _teach_make_locator = (By.CSS_SELECTOR, 'div.make-teach')

    @property
    def teach_make_count(self):
        return len(self.find_elements(*self._teach_make_locator))

    @property
    def is_teach_makes_visible(self):
        return self.is_element_visible(*self._teach_make_locator)
