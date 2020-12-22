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

sys.stdout.write("\033]0;ZetaSploit Framework\007")

import os
import readline

from core.menus.main import main

from core.loader import loader
from core.io import io
from core.helper import helper
from core.badges import badges
from core.banner import banner

readline.parse_and_bind("tab: complete")

class zsf:
    def __init__(self):
        self.main = main()
        self.loader = loader()
        self.io = io()
        self.helper = helper()
        self.badges = badges()
        self.banner = banner()

    def check_root(self):
        if os.getuid() == 0:
            return True
        self.badges.output_error("Operation not permitted!")
        return False
    
    def check_install(self):
        if os.path.exists(self.helper.base_path):
            return True
        self.badges.output_error("ZetaSploit is not installed!")
        self.badges.output_information("Consider running ./install.sh")
        return False

    def start_zsf(self):
        try:
            self.loader.load_all()
        except:
            sys.exit()

    def launch_shell(self):
        os.system("clear")
        self.banner.print_random_banner()
        self.io.output("ZetaSploit Framework "+self.helper.version)
        self.io.output("-------------------------")
        self.io.output("")

    def shell(self):
        self.start_zsf()
        self.launch_shell()
        self.main.main_menu()
