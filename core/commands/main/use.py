#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020 EntySec
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

from core.menus.module import module
from core.badges import badges
from core.storage import storage
from core.modules import modules

class ZetaSploitCommand:
    def __init__(self):
        self.module = module()
        self.badges = badges()
        self.storage = storage()
        self.modules = modules()

        self.details = {
            'Name': "use",
            'Description': "Use specified module.",
            'Usage': "use <module>",
            'ArgsCount': 1,
            'NeedsArgs': True,
            'Args': []
        }

    def run(self):
        module = self.details['Args'][0]
        modules = self.storage.get("modules")
        category = self.modules.get_category(module)
        if category in modules.keys():
            if module in modules[category].keys():
                self.storage.set("current_module", [])
                self.storage.set("pwd", 0)
                self.storage.add_array("current_module", '')
                self.storage.set_array("current_module", self.storage.get("pwd"), modules[category][module])
                self.module.module_menu()
            else:
                self.badges.output_error("Invalid module!")
        else:
            self.badges.output_error("Invalid module!")