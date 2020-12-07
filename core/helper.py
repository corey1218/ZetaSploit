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
import binascii
import socket
import base64
import readline

from core.badges import badges
from core.vars import vars

class helper:
    def __init__(self):
        self.badges = badges()
        self.vars = vars()

        self.version = "v1.0"
        self.lhost = self.getip()
        self.lport = 4444

    def getip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("192.168.1.1", 80))
            host = s.getsockname()[0]
            s.close()
            host = host
        except:
            host = "127.0.0.1"
        return host

    def output(self, msg):
        sys.stdout.write('\033[1K\r' + msg + os.linesep)
        sys.stdout.flush()
        if self.vars.get("current_prompt") != None and self.vars.get("active_input"):
            sys.stdout.write('\033[1K\r')
            sys.stdout.write(self.vars.get("current_prompt") + readline.get_line_buffer())
            sys.stdout.flush()

    def generate_terminator(self):
        return binascii.hexlify(os.urandom(8)).decode()

    def encode_remote_data(self, local_host, local_port):
        remote_data = (local_host + ":" + local_port).encode()
        return base64.b64encode(remote_data).decode()