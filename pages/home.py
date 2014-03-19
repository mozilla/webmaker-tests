#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import Page
from base import Base


class HomePage(Base):

    _page_title = 'Home - Mozilla Webmaker'

    def go_to_page(self):
        self.selenium.get(self.base_url + '/')
        self.is_the_current_page

    @property
    def center_links(self):
        return self.CenterLinks(self.testsetup)

    class CenterLinks(Page):
        _get_together_locator = (By.CSS_SELECTOR, '.get-together > div > a')
        _learn_locator = (By.CSS_SELECTOR, '.learn > div > a')
        _teach_locator = (By.CSS_SELECTOR, '.teach > div > a')

        def click_events(self):
            self.find_element(*self._get_together_locator).click()
            from events import EventsPage
            return EventsPage(self.testsetup)

        def click_teach(self):
            self.find_element(*self._teach_locator).click()
            from teach import TeachPage
            return TeachPage(self.testsetup)

        def click_learn(self):
            self.find_element(*self._learn_locator).click()
            from make import MakePage
            return MakePage(self.testsetup)
