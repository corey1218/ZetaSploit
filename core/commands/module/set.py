#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os

from core.badges import badges
from core.storage import storage

class ZetaSploitCommand:
    def __init__(self):
        self.badges = badges()
        self.storage = storage()

        self.details = {
            'Category': "module",
            'Name': "set",
            'Description': "Set an option value.",
            'Usage': "set <option> <value>",
            'ArgsCount': 2,
            'NeedsArgs': True,
            'Args': list()
        }

    def run(self):
        option = self.details['Args'][0].upper()
        value = self.details['Args'][1]
        current_module = self.storage.get_array("current_module", self.storage.get("pwd"))
        if option in current_module.options.keys():
            self.badges.output_information(option + " ==> " + value)
            self.storage.set_module_option("current_module", self.storage.get("pwd"), option, value)
        else:
            self.badges.output_error("Unrecognized option!")
