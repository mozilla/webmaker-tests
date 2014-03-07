#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests


class BaseTest:

    def get_response_code(self, url, timeout):
        requests.adapters.DEFAULT_RETRIES = 5
        try:
            r = requests.get(url, verify=False, allow_redirects=True, timeout=timeout)
            return r.status_code
        except requests.Timeout:
            return 408

    def make_absolute(self, url, base_url):
        if url.startswith('http'):
            return url
        return base_url + url
