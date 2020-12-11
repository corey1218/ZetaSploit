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
import sys

from core.vars import vars

class io:
    def __init__(self):
        self.vars = vars()

    def output(self, message):
        sys.stdout.write('\033[1K\r' + message + os.linesep)
        sys.stdout.flush()
        if self.vars.get("current_prompt") != None and self.vars.get("active_input"):
            sys.stdout.write('\033[1K\r' + self.vars.get("current_prompt"))
            sys.stdout.flush()

    def input(self, prompt_message):
        self.vars.set("current_prompt", prompt_message)
        self.vars.set("active_input", True)
        command = input(prompt_message).strip()
        commands = command.split()
        arguments = ""
        if commands != []:
            arguments = "".join(command.split(commands[0])).strip()
        self.vars.set("active_input", False)
        return (commands, arguments)