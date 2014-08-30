#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from base import Base


class TermsPage(Base):

    _terms_title_locator = (By.CSS_SELECTOR, '/html/head/meta[139]')

    @property
    def is_page_title_visible(self):
        return self.is_element_visible(*self._terms_title_locator).text
