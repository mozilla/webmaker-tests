#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.base import Base


class StarterMakes(Base):

    _page_title = 'Starter Makes - Mozilla Webmaker'
    _starter_makes_locator = (By.CSS_SELECTOR, '.make')

    @property
    def starter_makes_count(self):
        return len(self.selenium.find_elements(*self._starter_makes_locator))
