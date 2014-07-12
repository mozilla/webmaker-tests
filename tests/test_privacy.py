#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.



import pytest
from unittestzero import Assert

from pages.home import HomePage
from tests.base_test import BaseTest

class TestPrivacy(BaseTest):

	@pytest.mark.nondestructive
	def test_verify_the_privacy_page_title(self, mozwebqa):
		home_page = HomePage(mozwebqa)
		home_page.go_to_page()

		privacy_page = home_page.header.click_privacy_link()
		Assert.true(privacy_page.is_the_current_page)