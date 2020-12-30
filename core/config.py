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

import yaml

from core.storage import storage

class config:
    def __init__(self):
        self.storage = storage()
        
        self.base_path = '/opt/zsf/'
        self.config_path = self.base_path + 'config/'
        
        self.path_config_file = self.config_path + 'path_config.yml'
        self.core_config_file = self.config_path + 'core_config.yml'
        
        self.path_config = self.storage.get("path_config")
        self.core_config = self.storage.get("core_config")

    def configure(self):
        path_config = yaml.safe_load(open(self.path_config_file))
        core_config = yaml.safe_load(open(self.core_config_file))

        self.path_config = path_config
        self.core_config = core_config
        
        self.storage.set("path_config", self.path_config)
        self.storage.set("core_config", self.core_config)
