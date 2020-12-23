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
from core.storage import storage

from data.modules.exploit.macos.stager.zetant_reverse_tcp.core.session import session

class ZetaSploitModule:
    def __init__(self):
        self.badges = badges()
        self.storage = storage()
        self.session = session()

        self.details = {
            'Name': "macos/zetant/trolling/say",
            'Authors': [
                'enty8080'
            ],
            'Description': "Say text message on device.",
            'Comments': [
                ''
            ]
        }

        self.options = {
            'MESSAGE': {
                'Description': "Message to say.",
                'Value': "Hello, zetant!",
                'Required': True
            },
            'SESSION': {
                'Description': 'Session to run on.',
                'Value': 0,
                'Required': True
            }
        }

    def get_session(self):
        session = self.options['SESSION']['Value']
        sessions = self.storage.get("post/macos/zetant")
        if sessions != None:
            for i in sessions.keys():
                if int(session) == int(i):
                    return (True, sessions[int(session)])
        self.badges.output_error("Invalid session given!")
        return (False, None)

    def run(self):
        exists, controller = self.get_session()
        if exists:
            status, output = controller.send_command("say", self.options['MESSAGE']['Value'])
            if status == "error":
                self.badges.output_error("Failed to say message!")