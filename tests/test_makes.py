#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage


class TestMakes:

    @pytest.mark.nondestructive
    def test_sample_makes_are_visible_on_home_page(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        makes = home_page.makes_templates_present()
        Assert.greater(makes, 0, u'%s templates displayed' %makes)
