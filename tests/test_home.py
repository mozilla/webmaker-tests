#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from tests.base_test import BaseTest


@pytest.mark.xfail(reason="Bug 1029294 - Page title for home page is incorrect")
class TestHome(BaseTest):

    @pytest.mark.nondestructive
    def test_center_link_teach(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        teach_page = home_page.center_links.click_teach()
        Assert.true(teach_page.is_the_current_page)

    @pytest.mark.nondestructive
    def test_center_link_learn(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        learn_page = home_page.center_links.click_learn()
        Assert.true(learn_page.is_the_current_page)

    @pytest.mark.nondestructive
    def test_center_link_events(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()

        events_page = home_page.center_links.click_events()
        Assert.true(events_page.is_the_current_page)

    @pytest.mark.nondestructive
    @pytest.mark.xfail("'mofostaging.net' in config.getvalue('base_url')",
           reason="Bug 985799 - Makes templates are not displayed on the home page")
    def test_sample_makes_are_visible_on_home_page(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        makes = home_page.makes_templates_present()
        Assert.greater(makes, 0, u'%s templates displayed' %makes)
