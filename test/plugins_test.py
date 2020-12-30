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

from core.badges import badges
from core.loader import loader
from core.config import config

class plugins_test:
    def __init__(self):
        self.badges = badges()
        self.loader = loader()
        self.config = config()
        
    def perform_test(self):
        self.config.configure()
        failed = False
        plugin_path = self.config.path_config['base_paths']['plugins_path']
        try:
            for plugin in os.listdir(plugin_path):
                if plugin.endswith("py"):
                        plugin_file_path = plugin_path + plugin[:-3]
                        try:
                            plugin_directory = plugin_file_path.replace(self.config.path_config['base_paths']['root_path'], '', 1)
                            plugin_directory = plugin_directory.replace("/", ".")
                            plugin_file = __import__(plugin_directory)
                            plugin_object = self.loader.get_module(plugin_file, plugin[:-3], plugin_directory)
                            plugin_object = plugin_object.ZetaSploitPlugin()
                            self.badges.output_success(plugin_file_path + ": OK!")
                        except:
                            self.badges.output_error(plugin_file_path + ": FAIL!")
                            failed = True
        except:
            self.badges.output_error("Failed to perform plugins test!")
            failed = True
        if failed:
            return False
        return True
