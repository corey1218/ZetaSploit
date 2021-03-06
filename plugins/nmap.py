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

import nmap3

from core.badges import badges

from data.plugins.nmap.core.banner import banner

class ZetaSploitPlugin:
    def __init__(self):
        self.nmap = nmap3.Nmap()
        self.badges = badges()

        self.banner = banner()

        self.details = {
            'Name': "nmap",
            'Authors': [
                'enty8080'
            ],
            'Description': "Nmap scan plugin for ZetaSploit.",
            'Comments': [
                ''
            ]
        }

        self.commands = {
            'scanner': {
                'port_scan': {
                    'Description': "Run port scan on host.",
                    'Usage': "port_scan <host>",
                    'ArgsCount': 1,
                    'NeedsArgs': True,
                    'Args': list(),
                    'Run': self.port_scan
                }
            }
        }

    def port_scan(self):
        host = self.commands['scanner']['port_scan']['Args'][0]
        self.badges.output_process("Performing port scan on " + host + "...")
        try:
            result = self.nmap.scan_top_ports(host)
            self.badges.output_information("Raw: " + str(result))
        except Exception:
            self.badges.output_error("Failed to perform port scan on " + host + "!")

    def run(self):
        self.banner.print_banner()
        self.badges.output_information("nmap v1.0 | ZetaSploit nmap plugin")
