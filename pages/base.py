#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.page import Page


class Base(Page):

    def sign_in(self, user='default'):
        credentials = self.testsetup.credentials[user]
        self.header.click_sign_in()
        from browserid import BrowserID
        browser_id = BrowserID(self.selenium, self.timeout)
        browser_id.sign_in(credentials['email'], credentials['password'])
        self.header.wait_for_sign_out_visible()

    def sign_out(self, user='default'):
        self.header.click_sign_out()
        self.header.wait_for_sign_in_visible()

    @property
    def is_signed_in(self):
        return not self.header.is_sign_in_visible

    @property
    def header(self):
        return self.HeaderRegion(self.testsetup)

    @property
    def footer(self):
        return self.Footer(self.testsetup)

    class HeaderRegion(Page):

        _login_locator = (By.CSS_SELECTOR, '.webmaker-login')
        _logout_locator = (By.CSS_SELECTOR, '.webmaker-logout')
        _search_page_locator = (By.LINK_TEXT, 'Search')
        _events_page_locator = (By.LINK_TEXT, 'Events')
        _teach_page_locator = (By.LINK_TEXT, 'Teach')
        _make_page_locator = (By.LINK_TEXT, 'Make')

        def click_sign_in(self):
            self.selenium.find_element(*self._login_locator).click()

        def click_sign_out(self):
            self.selenium.find_element(*self._logout_locator).click()

        def wait_for_sign_out_visible(self):
            self.wait_for_element_visible(*self._logout_locator)

        def wait_for_sign_in_visible(self):
            self.wait_for_element_visible(*self._login_locator)

        @property
        def is_sign_in_visible(self):
            return self.is_element_visible(*self._login_locator)

        def go_to_search_page(self):
            self.selenium.find_element(*self._search_page_locator).click()
            from pages.search import Search
            return Search(self.testsetup)

        def go_to_events_page(self):
            self.selenium.find_element(*self._events_page_locator).click()
            from pages.events.home import EventsPage
            return EventsPage(self.testsetup)

        def go_to_teach_page(self):
            self.selenium.find_element(*self._teach_page_locator).click()
            from pages.teach.resources import ResourcesPage
            return ResourcesPage(self.testsetup)

        def go_to_make_page(self):
            self.selenium.find_element(*self._make_page_locator).click()
            from pages.make.starter_makes import StarterMakes
            return StarterMakes(self.testsetup)

    class Footer(Page):

        copyright_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#copyright a:nth-of-type(1)'),
                'url_suffix': 'http://www.mozilla.org/privacy-policy.html',
            }, {
                'locator': (By.CSS_SELECTOR, '#copyright a:nth-of-type(2)'),
                'url_suffix': 'http://www.mozilla.org/about/legal.html'
            }, {
                'locator': (By.CSS_SELECTOR, '#site-info a.licence'),
                'url_suffix': 'http://www.mozilla.org/foundation/licensing/website-content.html'
            }, {
                'locator': (By.LINK_TEXT, 'About'),
                'url_suffix': '/about/'
            }
        ]
