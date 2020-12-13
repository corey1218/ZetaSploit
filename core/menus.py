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
import re
import readline

from core.badges import badges
from core.module.module import module
from core.formatter import formatter
from core.vars import vars
from core.io import io

class menus:
    def __init__(self):
        self.badges = badges()
        self.module = module()
        self.formatter = formatter()
        self.vars = vars()
        self.io = io()

    def main_menu(self, modules, title='zsf'):
        while True:
            try:
                commands, arguments = self.io.input('\033[4m' + title + '\033[0m> ')
                if commands == []:
                    continue
                if commands[0] == "exit":
                    sys.exit()
                elif commands[0] == "clear":
                    os.system("clear")
                elif commands[0] == "help":
                    self.io.output("")
                    self.io.output("Core Commands")
                    self.io.output("=============")
                    self.io.output("")
                    self.io.output("    Command        Description")
                    self.io.output("    -------        -----------")
                    self.io.output("    clear          Clear terminal window.")
                    self.io.output("    details        Show specified module details.")
                    self.io.output("    exec           Execute system command.")
                    self.io.output("    exit           Exit ZetaSploit Framework.")
                    self.io.output("    help           Show available commands.")
                    self.io.output("    show           Show specified information.")
                    self.io.output("    use            Use specified module.")
                    self.io.output("")
                elif commands[0] == "exec":
                    if len(commands) < 2:
                        self.io.output("Usage: exec <command>")
                    else:
                        self.badges.output_information("exec:")
                        os.system(arguments)
                        self.io.output("")
                elif commands[0] == "use":
                    if len(commands) < 2:
                        self.io.output("Usage: use <module>")
                    else:
                        not_found = True
                        for category in modules.keys():
                            if commands[1] in modules[category].keys():
                                not_found = False
                                self.modules_menu(modules, modules[category][commands[1]], category)
                        if not_found:
                            self.badges.output_error("Invalid module!")
                elif commands[0] == "details":
                    if len(commands) < 2:
                        self.io.output("Usage: details <module>")
                    else:
                        not_found = True
                        for category in modules.keys():
                            if commands[1] in modules[category].keys():
                                not_found = False
                                self.module.show_details(modules[category][commands[1]].details)
                        if not_found:
                            self.badges.output_error("Invalid module!")
                elif commands[0] == "show":
                    usage = "Usage: show ["
                    for category in modules.keys():
                        usage += category + "|"
                    usage = usage[:-1] + "]"
                    if len(commands) < 2:
                        self.io.output(usage)
                    else:
                        if commands[1] in modules.keys():
                            self.formatter.format_modules(modules[commands[1]], commands[1])
                        else:
                            self.io.output(usage)
                else:
                    self.badges.output_error("Unrecognized command!")
            except (KeyboardInterrupt, EOFError):
                self.io.output("")
            except Exception as e:
                self.badges.output_error("An error occurred: " + str(e) + "!")

    def modules_menu(self, modules, module, category, title='zsf'):
        current_module = []
        pwd = 0
        current_module.append('')
        current_module[pwd] = module
        while True:
            try:
                commands, arguments = self.io.input('\033[4m' + title + '\033[0m(\033[1;31m' + current_module[pwd].details['Name'] + '\033[0m)> ')
                if commands == []:
                    continue
                if commands[0] == "exit":
                    sys.exit()
                elif commands[0] == "clear":
                    os.system("clear")
                elif commands[0] == "help":
                    self.io.output("")
                    self.io.output("Core Commands")
                    self.io.output("=============")
                    self.io.output("")
                    self.io.output("    Command        Description")
                    self.io.output("    -------        -----------")
                    self.io.output("    back           Return to the previous menu.")
                    self.io.output("    clear          Clear terminal window.")
                    self.io.output("    details        Show specified module details.")
                    self.io.output("    exec           Execute system command.")
                    self.io.output("    exit           Exit ZetaSploit Framework.")
                    self.io.output("    help           Show available commands.")
                    self.io.output("    run            Run current selected module.")
                    self.io.output("    set            Set module option value.")
                    self.io.output("    show           Show specified information.")
                    self.io.output("    use            Use specified module.")
                    if hasattr(current_module[pwd], "commands"):
                        self.formatter.format_commands(current_module[pwd].commands, "Module")
                    else:
                        self.io.output("")
                elif commands[0] == "exec":
                    if len(commands) < 2:
                        self.io.output("Usage: exec <command>")
                    else:
                        self.badges.output_information("exec:")
                        os.system(arguments)
                        self.io.output("")
                elif commands[0] == "use":
                    if len(commands) < 2:
                        self.io.output("Usage: use <module>")
                    else:
                        if commands[1] != category + "/" + current_module[pwd].details['Name']:
                            not_found = True
                            for category in modules.keys():
                                if commands[1] in modules[category].keys():
                                    not_found = False
                                    current_module.append('')
                                    pwd += 1
                                    current_module[pwd] = modules[category][commands[1]]
                            if not_found:
                                self.badges.output_error("Invalid module!")
                elif commands[0] == "show":
                    usage = "Usage: show ["
                    for category in modules.keys():
                        usage += category + "|"
                    usage = usage[:-1] + "]"
                    if len(commands) < 2:
                        self.io.output(usage)
                    else:
                        if commands[1] in modules.keys():
                            self.formatter.format_modules(modules[commands[1]], commands[1])
                        else:
                            self.io.output(usage)
                elif commands[0] == "back":
                    pwd -= 1
                    current_module = current_module[0:-1]
                    if current_module == []:
                        pwd = 0
                        break
                elif commands[0] == "options":
                    if hasattr(current_module[pwd], "options"):
                        self.formatter.format_options(current_module[pwd].options, "Module")
                    else:
                        self.badges.output_warning("Module does not have options.")
                elif commands[0] == "details":
                    if len(commands) < 2:
                        self.io.output("Usage: details <module>")
                    else:
                        not_found = True
                        for category in modules.keys():
                            if commands[1] in modules[category].keys():
                                not_found = False
                                self.module.show_details(modules[category][commands[1]].details)
                        if not_found:
                            self.badges.output_error("Invalid module!")
                elif commands[0] == "set":
                    if len(commands) < 3:
                        self.io.output("Usage: set <option> <value>")
                    else:
                        if commands[1] in current_module[pwd].options.keys():
                            self.badges.output_information(commands[1] + " ==> " + commands[2])
                            current_module[pwd].options[commands[1]]['Value'] = commands[2]
                        else:
                            self.badges.output_error("Unrecognized option!")
                elif commands[0] == "run":
                    count = 0
                    if hasattr(current_module[pwd], "options"):
                        for option in current_module[pwd].options.keys():
                            if current_module[pwd].options[option]['Value'] == '' and current_module[pwd].options[option]['Required'] == True:
                                count += 1
                        if count > 0:
                            self.badges.output_error("Missed some required options! (" + count + ")")
                        else:
                            try:
                                current_module[pwd].run()
                            except (KeyboardInterrupt, EOFError):
                                self.io.output("")
                    else:
                        try:
                            current_module[pwd].run()
                        except (KeyboardInterrupt, EOFError):
                            self.io.output("")
                else:
                    if hasattr(current_module[pwd], "commands"):
                        if commands[0] in current_module[pwd].commands.keys():
                            if current_module[pwd].commands[commands[0]]['NeedsArgs']:
                                if (len(commands) - 1) < current_module[pwd].commands[commands[0]]['ArgsCount']:
                                    self.io.output("Usage:" + current_module[pwd].commands[commands[0]]['Usage'])
                                else:
                                    arguments = re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', arguments)
                                    current_module[pwd].commands[commands[0]]['Args'] = arguments
                                    try:
                                        current_module[pwd].commands[commands[0]]['Run']()
                                    except (KeyboardInterrupt, EOFError):
                                        self.io.output("")
                            else:
                                try:
                                    current_module[pwd].commands[commands[0]]['Run']()
                                except (KeyboardInterrupt, EOFError):
                                    self.io.output("")
                        else:
                            self.badges.output_error("Unrecognized command!")
                    else:
                        self.badges.output_error("Unrecognized command!")
            except (KeyboardInterrupt, EOFError):
                self.io.output("")
            except Exception as e:
                self.badges.output_error("An error occurred: " + str(e) + "!")