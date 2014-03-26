#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.base import Base


class AboutPage(Base):

    _hello_message_locator = (By.CSS_SELECTOR, 'div.about-hello')

    @property
    def is_hello_message_visible(self):
        return self.is_element_visible(*self._hello_message_locator)
