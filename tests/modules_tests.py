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
from core.importer import importer
from core.config import config

class modules_test:
    def __init__(self):
        self.badges = badges()
        self.importer = importer()
        self.config = config()
        
    def perform_test(self):
        self.config.configure()
        failed = False
        try:
            module_path = self.config.path_config['base_paths']['modules_path']
            for module_category in os.listdir(module_path):
                module_path = self.config.path_config['base_paths']['modules_path'] + module_category
                for path, sub, files in os.walk(module_path):
                    for file in files:
                        if file.endswith('py'):
                            module_file_path = path + '/' + file[:-3]
                            try:
                                module_directory = module_file_path.replace(self.config.path_config['base_paths']['root_path'], '', 1)
                                module_directory = module_directory.replace("/", ".")
                                module_file = __import__(module_directory)
                                module_object = self.importer.get_module(module_file, file[:-3], module_directory)
                                module_object = module_object.ZetaSploitModule()
                                self.badges.output_success(module_file_path + ": OK!")
                            except:
                                self.badges.output_error(module_file_path + ": FAIL!")
                                failed = True
        except:
            self.badges.output_error("Failed to perform modules test!")
            failed = True
        if failed:
            return False
        return True
