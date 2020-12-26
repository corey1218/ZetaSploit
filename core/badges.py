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

class badges:
    def __init__(self):
        self.io = io()

        self.RED = '\033[1;31m'
        self.WHITE = '\033[1;77m'
        self.BLUE = '\033[1;34m'
        self.YELLOW = '\033[1;33m'
        self.GREEN = '\033[1;32m'
        self.END = '\033[0m'

        self.I = '\033[1;77m[i] \033[0m'
        self.S = '\033[1;32m[+] \033[0m'
        self.W = '\033[1;33m[!] \033[0m'
        self.E = '\033[1;31m[-] \033[0m'
        self.P = '\033[1;34m[*] \033[0m'
        self.Q = '\033[1;77m[?] \033[0m'

    def output_process(self, message):
        self.io.output(self.P + message)

    def output_success(self, message):
        self.io.output(self.S + message)

    def output_error(self, message):
        self.io.output(self.E + message)

    def output_warning(self, message):
        self.io.output(self.W + message)

    def output_information(self, message):
        self.io.output(self.I + message)

    def input_confirm(self, message):
        return self.io.input(self.Q + message)[0][0]
