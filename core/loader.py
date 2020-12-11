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

import sys
import time
import threading
import os
import string

from core.badges import badges

class loader:
    def __init__(self):
        self.badges = badges()

    def get_module(self, mu, name, folderpath):
        folderpath_list = folderpath.split(".")
        for i in dir(mu):
            if i == name:
                pass
                return getattr(mu, name)
            else:
                if i in folderpath_list:
                    i = getattr(mu, i)
                    return self.get_module(i, name, folderpath)
    
    def import_modules(self):
        global modules
        modules = dict()
        module_path = "modules"
        for category in os.listdir(module_path):
            modules[category] = dict()
        try:
            for module_category in os.listdir(module_path):
                module_path = "modules/" + module_category
                for module_system in os.listdir(module_path):
                    module_path = "modules/" + module_category + "/" + module_system
                    for module_type in os.listdir(module_path):
                        module_path = "modules/" + module_category + "/" + module_system + "/" + module_type
                        for module in os.listdir(module_path):
                            if module == '__init__.py' or module[-3:] != '.py':
                                continue
                            else:
                                try:
                                    module_directory = module_path.replace("/", ".").replace("\\", ".") + "." + module[:-3]
                                    module_file = __import__(module_directory)
                                    module_object = self.get_module(module_file, module[:-3], module_directory)
                                    module_object = module_object.ZetaSploitModule()
                                    module_name = module_category + "/" + module_object.details['Name']
                                    modules[module_category][module_name] = module_object
                                except Exception as e:
                                    self.badges.output_error("Failed to load module! Reason: " + str(e))
        except Exception as e:
            self.badges.output_error("Failed to load some modules! Reason: "+str(e))

    def load_modules(self):
        loading_process = threading.Thread(target=self.import_modules)
        loading_process.start()
        base_line = "Starting the ZetaSploit Framework..."
        cycle = 0
        while loading_process.is_alive():
            for char in "/-\|":
                status = base_line + char + "\r"
                cycle += 1
                if status[cycle % len(status)] in list(string.ascii_lowercase):
                    status = status[:cycle % len(status)] + status[cycle % len(status)].upper() + status[cycle % len(status) + 1:]
                elif status[cycle % len(status)] in list(string.ascii_uppercase):
                    status = status[:cycle % len(status)] + status[cycle % len(status)].lower() + status[cycle % len(status) + 1:]
                sys.stdout.write(self.badges.P + status)
                time.sleep(.1)
                sys.stdout.flush()
        loading_process.join()
        return modules
