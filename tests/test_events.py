#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
from unittestzero import Assert

from pages.home import HomePage
from tests.base_test import BaseTest


@pytest.mark.xfail(reason="Bug 1029294 - Page title for home page is incorrect")
class TestEvents(BaseTest):

    @pytest.mark.nondestructive
    def test_that_events_front_page_shows_upcoming_events(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        events_page = home_page.header.click_events_tab()
        Assert.true(events_page.upcoming_events_count > 0)
        Assert.true(events_page.upcoming_events_is_visible)
