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
import subprocess

from core.badges import badges
from core.storage import storage
from core.modules import modules

class ZetaSploitCommand:
    def __init__(self):
        self.badges = badges()
        self.storage = storage()
        self.modules = modules()
        
        self.details = {
            'Category': "developer",
            'Name': "edit",
            'Description': "Open module in editor.",
            'Usage': "edit <module>",
            'ArgsCount': 1,
            'NeedsArgs': True,
            'Args': list()
        }

    def run(self):
        module = self.details['Args'][0]
        module_category = self.modules.get_category(module)
        module_platform = self.modules.get_platform(module)
        module_name = self.modules.get_name(module)
        
        if not os.environ['EDITOR']:
            editor = "vi"
        else:
            editor = os.environ['EDITOR']
            
        imported_modules = self.storage.get("imported_modules")
        if not imported_modules or module not in imported_modules:
            module_path = self.storage.get("modules")[module_category][module_platform][module_name]['Path']
            edit_mode = [editor, module_path]
            subprocess.call(edit_mode)
        else:
            self.badges.output_error("Can not edit already used module!")
