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
from core.storage import storage
from core.config import config

class loader:
    def __init__(self):
        self.badges = badges()
        self.storage = storage()
        self.config = config()

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

    def import_commands(self):
        commands = dict()
        command_path = self.config.base_paths['commands_path']
        for menu in os.listdir(command_path):
            commands[menu] = dict()
        try:
            for command_menu in os.listdir(command_path):
                command_path = self.config.base_paths['commands_path'] + command_menu
                for path, sub, files in os.walk(command_path):
                    for file in files:
                        if file.endswith('py'):
                            command_file_path = path + '/' + file[:-3]
                            try:
                                command_directory = command_file_path.replace(self.config.base_paths['root_path'], '', 1)
                                command_directory = command_directory.replace("/", ".")
                                command_file = __import__(command_directory)
                                command_object = self.get_module(command_file, file[:-3], command_directory)
                                command_object = command_object.ZetaSploitCommand()
                                command_name = command_object.details['Name']
                                commands[command_menu][command_name] = command_object
                            except Exception as e:
                                self.badges.output_error("Failed to load command! Reason: " + str(e))
        except Exception as e:
            self.badges.output_error("Failed to load some commands! Reason: "+str(e))
        self.storage.set("commands", commands)

    def import_plugins(self):
        plugins = dict()
        plugin_path = self.config.base_paths['plugins_path']
        try:
            for plugin in os.listdir(plugin_path):
                if plugin.endswith("py"):
                        plugin_file_path = plugin_path + plugin[:-3]
                        try:
                            plugin_directory = plugin_file_path.replace(self.config.base_paths['root_path'], '', 1)
                            plugin_directory = plugin_directory.replace("/", ".")
                            plugin_file = __import__(plugin_directory)
                            plugin_object = self.get_module(plugin_file, plugin[:-3], plugin_directory)
                            plugin_object = plugin_object.ZetaSploitPlugin()
                            plugin_name = plugin_object.details['Name']
                            plugins[plugin_name] = plugin_object
                        except Exception as e:
                            self.badges.output_error("Failed to enumerate plugin! Reason: " + str(e))
        except Exception as e:
            self.badges.output_error("Failed to enumerate some plugins! Reason: "+str(e))
        self.storage.set("plugins", plugins)

    def import_modules(self):
        modules = dict()
        module_path = self.config.base_paths['modules_path']
        for category in os.listdir(module_path):
            modules[category] = dict()
        try:
            for module_category in os.listdir(module_path):
                module_path = self.config.base_paths['modules_path'] + module_category
                for path, sub, files in os.walk(module_path):
                    for file in files:
                        if file.endswith('py'):
                            module_file_path = path + '/' + file[:-3]
                            try:
                                module_directory = module_file_path.replace(self.config.base_paths['root_path'], '', 1)
                                module_directory = module_directory.replace("/", ".")
                                module_file = __import__(module_directory)
                                module_object = self.get_module(module_file, file[:-3], module_directory)
                                module_object = module_object.ZetaSploitModule()
                                module_name = module_object.details['Name']
                                modules[module_category][module_name] = module_object
                            except Exception as e:
                                self.badges.output_error("Failed to load module! Reason: " + str(e))
        except Exception as e:
            self.badges.output_error("Failed to load some modules! Reason: "+str(e))
        self.storage.set("modules", modules)

    def import_all(self):
        self.import_commands()
        self.import_plugins()
        self.import_modules()

    def load_all(self):
        loading_process = threading.Thread(target=self.import_all)
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
