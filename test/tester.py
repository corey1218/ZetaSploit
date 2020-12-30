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

from core.badges import badges

from test.modules_test import modules_test
from test.plugins_test import plugins_test
from test.commands_test import commands_test

class tester:
    def __init__(self):
        self.badges = badges()

        self.modules_test = modules_test()
        self.plugins_test = plugins_test()
        self.commands_test = commands_test()
        
    def perform_tests(self):
        self.badges.output_process("Performing modules test...")
        status = self.modules_test.perform_test()
        
        self.badges.output_process("Performing plugins test...")
        status = self.plugins_test.perform_test()
        
        self.badges.output_process("Performing commands test...")
        status = self.commands_test.perform_test()
        
        if status:
            self.badges.output_success("All checks passed!")
            sys.exit(0)
        self.badges.output_error("Not all checks passed!")
        sys.exit(1)
