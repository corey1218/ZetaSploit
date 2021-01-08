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
import sys

from core.io import io
from core.badges import badges
from core.storage import storage

class execute:
    def __init__(self):
        self.io = io()
        self.badges = badges()
        self.storage = storage()

    def execute_system(self, commands):
        self.badges.output_information("exec: ")
        os.system(commands)
        self.io.output("")
        
    def execute_command(self, command):
        if command['NeedsArgs']:
            if (len(commands) - 1) < command['ArgsCount']:
                self.io.output("Usage: " + command['Usage'])
            else:
                command['Args'] = self.formatter.format_arguments(arguments)
                try:
                    command['Run']()
                except (KeyboardInterrupt, EOFError):
                    self.io.output("")
        else:
            try:
                command['Run']()
            except (KeyboardInterrupt, EOFError):
                self.io.output("")
        
    def execute_main(self, commands):
        if commands[0] in self.storage.get("commands")['main'].keys():
            command = self.storage.get("commands")['main'][commands[0]]
            self.execute_command(command)
                    
    def execute_main(self, commands):
        if commands[0] in self.storage.get("commands")['module'].keys():
            command = self.storage.get("commands")['module'][commands[0]]
            self.execute_command(command)
