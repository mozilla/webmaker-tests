#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
from unittestzero import Assert

from pages.home import HomePage
from tests.base_test import BaseTest


class TestEvents(BaseTest):

    @pytest.mark.nondestructive
    def test_that_events_front_page_shows_upcoming_events(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        events_page = home_page.header.go_to_events_page()
        Assert.true(events_page.upcoming_events_count > 0)
        Assert.true(events_page.upcoming_events_is_visible)
