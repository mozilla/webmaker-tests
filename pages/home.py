#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import Page
from base import Base


class HomePage(Base):

    _page_title = 'Home - Mozilla Webmaker'
    _makes_templates_locator = (By.CSS_SELECTOR, 'DIV.make-now')

    def go_to_page(self):
        self.selenium.get(self.base_url + '/')
        self.is_the_current_page

    def makes_templates_present(self):
        return len(self.selenium.find_elements(*self._makes_templates_locator))

    @property
    def center_links(self):
        return self.CenterLinks(self.testsetup)

    class CenterLinks(Page):
        _get_together_locator = (By.CSS_SELECTOR, '.get-together > div > a')
        _learn_locator = (By.CSS_SELECTOR, '.learn > div > a')
        _teach_locator = (By.CSS_SELECTOR, '.teach > div > a')

        def click_events(self):
            self.find_element(*self._get_together_locator).click()
            from events.home import EventsPage
            return EventsPage(self.testsetup)

        def click_teach(self):
            self.find_element(*self._teach_locator).click()
            from teach.resources import ResourcesPage
            return ResourcesPage(self.testsetup)

        def click_learn(self):
            self.find_element(*self._learn_locator).click()
            from make.starter_makes import StarterMakes
            return StarterMakes(self.testsetup)
