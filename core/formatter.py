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

from core.io import io

class formatter:
    def __init__(self):
        self.io = io()

    def format_options(self, options, title):
        names = []
        values = []
        required = []
        for name in options.keys():
            names.append(name)
            values.append(str(options[name]['Value']))
            required.append(str(options[name]['Required']))
        bigger_name = len(names[0])
        for name in names:
            if len(name) > bigger_name:
                bigger_name = len(name)
        bigger_value = len(values[0])
        for value in values:
            if len(value) > bigger_value:
                bigger_value = len(value)
        is_no_of_any = False
        for requ in required:
            if requ == "False":
                is_no_of_any = True
        if bigger_name >= 7:
            bigger_name = bigger_name - 2
        else:
            bigger_name = 4
        if bigger_value >= 8:
            bigger_value = bigger_value - 3
        else:
            bigger_value = 4
        if is_no_of_any:
            bigger_required = 4
        else:
            bigger_required = 4
        self.io.output(title.title() + " Options")
        self.io.output("="*len(title.title() + " Options"))
        self.io.output("")
        self.io.output("    Name" + " " * (bigger_name) + "Value" + " " * (bigger_value) + "Required    Description")
        self.io.output("    ----" + " " * (bigger_name) + "-----" + " " * (bigger_value) + "--------    -----------")
        for name in names:
            self.io.output("    " + name + " " * (4 - len(name) + bigger_name) + str(options[name]['Value']) + " " * (5 - len(str(options[name]['Value'])) + bigger_value) + str(options[name]['Required']) + " " * (8 - len(str(options[name]['Required'])) + bigger_required) + options[name]['Description'])

    def format_global_commands(self, commands, title):
        commands = sorted(commands.keys())
        command_names = []
        for command in commands:
            command_names.append(command)
        bigger = len(command_names[0])
        for i in command_names:
            if len(i) > bigger:
                bigger = len(i)
        if bigger >= 14:
            bigger = bigger - 5
        else:
            bigger = 8
        self.io.output(title.title() + " Commands")
        self.io.output("=" * len(title.title() + " Commands"))
        self.io.output("")
        self.io.output("    Command" + " " * (bigger) + "Description")
        self.io.output("    -------" + " " * (bigger) + "-----------")
        for i in command_names:
            self.io.output("    " + i + " " * (7 - len(i) + bigger) + commands[i].details['Description'])

    def format_local_commands(self, commands, title):
        commands = sorted(commands.keys())
        command_names = []
        for command in commands:
            command_names.append(command)
        bigger = len(command_names[0])
        for i in command_names:
            if len(i) > bigger:
                bigger = len(i)
        if bigger >= 14:
            bigger = bigger - 5
        else:
            bigger = 8
        self.io.output(title.title() + " Commands")
        self.io.output("=" * len(title.title() + " Commands"))
        self.io.output("")
        self.io.output("    Command" + " " * (bigger) + "Description")
        self.io.output("    -------" + " " * (bigger) + "-----------")
        for i in command_names:
            self.io.output("    " + i + " " * (7 - len(i) + bigger) + commands[i]['Description'])

    def format_modules(self, modules, title):
        module_names = []
        for name in modules.keys():
            module_names.append(name)
        bigger = len(module_names[0])
        for i in module_names:
            if len(i) > bigger:
                bigger = len(i)
        if bigger >= 13:
            bigger = bigger - 4
        else:
            bigger = 8
        self.io.output(title.title() + " Modules")
        self.io.output("=" * len(title.title() + " Modules"))
        self.io.output("")
        self.io.output("    Module" + " " * (bigger) + "Description")
        self.io.output("    ------" + " " * (bigger) + "-----------")
        for i in module_names:
            self.io.output("    " + i + " " * (6 - len(i) + bigger) + modules[i].details['Description'])

    def format_plugins(self, plugins):
        plugin_names = []
        for name in plugins.keys():
            plugin_names.append(name)
        bigger = len(plugin_names[0])
        for i in plugin_names:
            if len(i) > bigger:
                bigger = len(i)
        if bigger >= 13:
            bigger = bigger - 4
        else:
            bigger = 8
        self.io.output("ZetaSploit Plugins")
        self.io.output("==================")
        self.io.output("")
        self.io.output("    Plugin" + " " * (bigger) + "Description")
        self.io.output("    ------" + " " * (bigger) + "-----------")
        for i in plugin_names:
            self.io.output("    " + i + " " * (6 - len(i) + bigger) + plugins[i].details['Description'])
