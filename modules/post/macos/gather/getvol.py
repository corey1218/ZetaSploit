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
from core.vars import vars

class ZetaSploitModule:
    def __init__(self):
        self.badges = badges()
        self.vars = vars()

        self.details = {
            'Name': "macos/gather/getvol",
            'Authors': ['enty8080'],
            'Description': "Get device volume level.",
            'Comment': ""
        }

        self.options = {
            'SESSION': {
                'Description': 'Session to run on.',
                'Value': 0,
                'Required': True
            }
        }

    def get_session(self):
        session = self.options['SESSION']['Value']
        sessions = self.vars.get("macos_sessions")
        if sessions != None:
            for i in sessions.keys():
                if int(session) == int(i):
                    return (True, sessions[int(session)])
        self.badges.output_error("Invalid session given!")
        return (False, None)

    def run(self):
        exists, controller = self.get_session()
        if exists:
            status, output = controller.send_command("getvol")
            if status == "error":
                self.badges.output_error("Failed to get device volume level!")
            else:
                self.badges.output_information("Volume Level: " + output)