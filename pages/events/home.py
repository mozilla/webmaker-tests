#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.page import Page


class EventsPage(Page):

    _page_title = 'Webmaker Events'

    _upcoming_event_locator = (By.CSS_SELECTOR, '.listing-home > li > a')

    @property
    def upcoming_events_count(self):
        return len(self.find_elements(*self._upcoming_event_locator))

    @property
    def upcoming_events_is_visible(self):
        return self.is_element_visible(*self._upcoming_event_locator)
