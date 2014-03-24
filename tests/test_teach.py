#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest
from unittestzero import Assert

from pages.teach.resources import ResourcesPage
from tests.base_test import BaseTest


class TestTeach(BaseTest):

    @pytest.mark.nondestructive
    def test_that_resources_page_display_makes(self, mozwebqa):
        resources_page = ResourcesPage(mozwebqa)
        resources_page.go_to_page()

        Assert.greater(resources_page.teach_make_count, 0)
        Assert.true(resources_page.is_teach_makes_visible)
