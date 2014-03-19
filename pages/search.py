#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By
from unittestzero import Assert

from pages.base import Base
from pages.page import Page


class Search(Page):

    _search_box_locator = (By.ID, 'search-field')
    _search_button_locator = (By.CSS_SELECTOR, 'button.search-btn')
    _search_query_word_locator = (By.CSS_SELECTOR, 'span.search-query-word')

    def search(self, search_term):
        element = self.selenium.find_element(*self._search_box_locator)
        element.send_keys(search_term)
        self.selenium.find_element(*self._search_button_locator).click()

    @property
    def search_query(self):
        return self.selenium.find_element(*self._search_query_word_locator).text
