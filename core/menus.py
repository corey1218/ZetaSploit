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
from core.helper import helper
from core.module.module import module
from core.plugin.plugin import plugin
from core.formatter import formatter
from core.vars import vars

class menus:
    def __init__(self):
        self.badges = badges()
        self.helper = helper()
        self.module = module()
        self.plugin = plugin()
        self.formatter = formatter()
        self.vars = vars()

    def prompt(self, prompt_message):
        self.vars.set("active_input", True)
        command = input(prompt_message).strip()
        commands = command.split()
        arguments = ""
        if commands != []:
            arguments = "".join(command.split(commands[0])).strip()
        self.vars.set("active_input", False)
        return (commands, arguments)

    def main_modules_menu(self, modules, title='zsf'):
        while True:
            try:
                self.vars.set("current_prompt", '\033[4m' + title + '\033[0m> ')
                commands, arguments = self.prompt(self.vars.get("current_prompt"))
                if commands == []:
                    continue
                if commands[0] == "exit":
                    sys.exit()
                elif commands[0] == "clear":
                    os.system("clear")
                elif commands[0] == "help":
                    self.helper.output("")
                    self.helper.output("Core Commands")
                    self.helper.output("=============")
                    self.helper.output("")
                    self.helper.output("    Command        Description")
                    self.helper.output("    -------        -----------")
                    self.helper.output("    clear          Clear terminal window.")
                    self.helper.output("    details        Show specified module details.")
                    self.helper.output("    exec           Execute system command.")
                    self.helper.output("    exit           Exit ZetaSploit Framework.")
                    self.helper.output("    help           Show available commands.")
                    self.helper.output("    modules        Show available modules.")
                    self.helper.output("")
                elif commands[0] == "exec":
                    if len(commands) < 2:
                        self.helper.output("Usage: exec <command>")
                    else:
                        self.helper.output(self.badges.I + "exec:")
                        os.system(arguments)
                        self.helper.output("")
                elif commands[0] == "use":
                    if len(commands) < 2:
                        self.helper.output("Usage: use <module>")
                    else:
                        if commands[1] in modules.keys():
                            self.modules_menu(modules, modules[commands[1]])
                        else:
                            self.helper.output(self.badges.E + "Invalid module!")
                elif commands[0] == "details":
                    if len(commands) < 2:
                        self.helper.output("Usage: details <module>")
                    else:
                        if commands[1] in modules.keys():
                            self.module.show_details(modules[commands[1]].details)
                        else:
                            self.helper.output(self.badges.E + "Invalid module!")
                elif commands[0] == "modules":
                    self.formatter.format_modules(modules)
                else:
                    self.helper.output(self.badges.E + "Unrecognized command!")
            except (KeyboardInterrupt, EOFError):
                self.helper.output("")
            except Exception as e:
                self.helper.output(self.badges.E + "An error occurred: " + str(e) + "!")

    def main_plugins_menu(self, plugins, title='zsf'):
        while True:
            try:
                self.vars.set("current_prompt", '\033[4m' + title + '\033[0m> ')
                commands, arguments = self.prompt(self.vars.get("current_prompt"))
                if commands == []:
                    continue
                if commands[0] == "exit":
                    break
                elif commands[0] == "clear":
                    os.system("clear")
                elif commands[0] == "help":
                    self.helper.output("")
                    self.helper.output("Core Commands")
                    self.helper.output("=============")
                    self.helper.output("")
                    self.helper.output("    Command        Description")
                    self.helper.output("    -------        -----------")
                    self.helper.output("    clear          Clear terminal window.")
                    self.helper.output("    details        Show specified plugin details.")
                    self.helper.output("    exec           Execute system command.")
                    self.helper.output("    exit           Exit from current session.")
                    self.helper.output("    help           Show available commands.")
                    self.helper.output("    plugins        Show available plugins.")
                    self.helper.output("")
                elif commands[0] == "exec":
                    if len(commands) < 2:
                        self.helper.output("Usage: exec <command>")
                    else:
                        self.helper.output(self.badges.I + "exec:")
                        os.system(arguments)
                        self.helper.output("")
                elif commands[0] == "use":
                    if len(commands) < 2:
                        self.helper.output("Usage: use <plugin>")
                    else:
                        if commands[1] in plugins.keys():
                            self.plugins_menu(plugins, plugins[commands[1]], 'zeterpreter')
                        else:
                            self.helper.output(self.badges.E + "Unrecognozed plugin!")
                elif commands[0] == "details":
                    if len(commands) < 2:
                        self.helper.output("Usage: details <modules>")
                    else:
                        if commands[1] in plugins.keys():
                            self.plugin.show_details(plugins[commands[1]].details)
                        else:
                            self.helper.output(self.badges.E + "Unrecognozed plugin!")
                elif commands[0] == "plugins":
                    self.formatter.format_plugins(plugins)
                else:
                    self.helper.output(self.badges.E +"Unrecognized command!")
            except (KeyboardInterrupt, EOFError):
                self.helper.output("")
            except Exception as e:
                self.helper.output(self.badges.E +"An error occurred: "+str(e)+"!")

    def modules_menu(self, modules, module, title='zsf'):
        current_module = []
        pwd = 0
        current_module.append('')
        current_module[pwd] = module
        while True:
            try:
                self.vars.set("current_prompt", '\033[4m' + title + '\033[0m(\033[1;31m' + current_module[pwd].details['Name'] + '\033[0m)> ')
                commands, arguments = self.prompt(self.vars.get("current_prompt"))
                if commands == []:
                    continue
                if commands[0] == "exit":
                    sys.exit()
                elif commands[0] == "clear":
                    os.system("clear")
                elif commands[0] == "help":
                    self.helper.output("")
                    self.helper.output("Core Commands")
                    self.helper.output("=============")
                    self.helper.output("")
                    self.helper.output("    Command        Description")
                    self.helper.output("    -------        -----------")
                    self.helper.output("    back           Return to the previous menu.")
                    self.helper.output("    clear          Clear terminal window.")
                    self.helper.output("    details        Show specified module details.")
                    self.helper.output("    exec           Execute system command.")
                    self.helper.output("    exit           Exit ZetaSploit Framework.")
                    self.helper.output("    help           Show available commands.")
                    self.helper.output("    modules        Show available modules.")
                    if current_module[pwd].details['HasCommands']:
                        self.formatter.format_commands(current_module[pwd].commands, "Module")
                    else:
                        self.helper.output("")
                elif commands[0] == "exec":
                    if len(commands) < 2:
                        self.helper.output("Usage: exec <command>")
                    else:
                        self.helper.output(self.badges.I + "exec:")
                        os.system(arguments)
                        self.helper.output("")
                elif commands[0] == "use":
                    if len(commands) < 2:
                        self.helper.output("Usage: use <module>")
                    else:
                        if command[1] in modules.keys():
                            current_module.append('')
                            pwd += 1
                            current_module[pwd] = modules[commands[1]]
                        else:
                            self.helper.output(self.badges.E + "Invalid module!")
                elif commands[0] == "modules":
                    self.formatter.format_modules(modules)
                elif commands[0] == "back":
                    pwd -= 1
                    current_module = current_module[0:-1]
                    if current_module == []:
                        pwd = 0
                        break
                elif commands[0] == "options":
                    self.formatter.format_options(current_module[pwd].options, "Module")
                elif commands[0] == "details":
                    if len(commands) < 2:
                        self.helper.output("Usage: details <module>")
                    else:
                        if commands[1] in modules.keys():
                            self.module.show_details(modules[commands[1]].details)
                        else:
                            self.helper.output(self.badges.E + "Invalid module!")
                elif commands[0] == "set":
                    if len(commands) < 3:
                        self.helper.output("Usage: set <option> <value>")
                    else:
                        if commands[1] in current_module[pwd].options.keys():
                            self.helper.output(self.badges.I + commands[1] + " ==> " + commands[2])
                            current_module[pwd].options[commands[1]]['Value'] = commands[2]
                        else:
                            self.helper.output(self.badges.E + "Unrecognized option!")
                elif commands[0] == "run":
                    count = 0
                    for option in current_module[pwd].options.keys():
                        if current_module[pwd].options[option]['Value'] == '' and current_module[pwd].options[option]['Required'] == True:
                            count += 1
                    if count > 0:
                        self.helper.output(self.badges.E + "Missed some required options! (" + count + ")")
                    else:
                        current_module[pwd].run()
                else:
                    if current_module[pwd].details['HasCommands']:
                        if commands[0] in current_module[pwd].commands.keys():
                            if current_module[pwd].commands[commands[0]]['NeedsArgs']:
                                if (len(commands) - 1) < current_module[pwd].commands[commands[0]]['ArgsCount']:
                                    self.helper.output("Usage:" + current_module[pwd].commands[commands[0]]['Usage'])
                                else:
                                    arguments = re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', arguments)
                                    current_module[pwd].commands[commands[0]]['Args'] = arguments
                                    current_module[pwd].commands[commands[0]]['Run']()
                            else:
                                current_module[pwd].commands[commands[0]]['Run']()
                        else:
                            self.helper.output(self.badges.E + "Unrecognized command!")
                    else:
                        self.helper.output(self.badges.E + "Unrecognized command!")
            except (KeyboardInterrupt, EOFError):
                self.helper.output("")
            except Exception as e:
                self.helper.output(self.badges.E + "An error occurred: " + str(e) + "!")

    def plugins_menu(self, plugins, plugin, title='zsf'):
        current_plugin = []
        pwd = 0
        current_plugin.append('')
        current_plugin[pwd] = plugin
        while True:
            try:
                self.vars.set("current_prompt", '\033[4m' + title + '\033[0m(\033[1;34m' + current_plugin[pwd].details['Name'] + '\033[0m)> ')
                commands, arguments = self.prompt(self.vars.get("current_prompt"))
                if commands == []:
                    continue
                if commands[0] == "exit":
                    sys.exit()
                elif commands[0] == "clear":
                    os.system("clear")
                elif commands[0] == "help":
                    self.helper.output("")
                    self.helper.output("Core Commands")
                    self.helper.output("=============")
                    self.helper.output("")
                    self.helper.output("    Command        Description")
                    self.helper.output("    -------        -----------")
                    self.helper.output("    back           Return to the previous menu.")
                    self.helper.output("    clear          Clear terminal window.")
                    self.helper.output("    details        Show specified plugin details.")
                    self.helper.output("    exec           Execute system command.")
                    self.helper.output("    exit           Exit ZetaSploit Framework.")
                    self.helper.output("    help           Show available commands.")
                    self.helper.output("    plugins        Show available plugins.")
                    if current_plugin[pwd].details['HasCommands']:
                        self.formatter.format_commands(current_plugin[pwd].commands, "Plugin")
                    else:
                        self.helper.output("")
                elif commands[0] == "exec":
                    if len(commands) < 2:
                        self.helper.output("Usage: exec <command>")
                    else:
                        self.helper.output(self.badges.I + "exec:")
                        os.system(arguments)
                        self.helper.output("")
                elif commands[0] == "use":
                    if len(commands) < 2:
                        self.helper.output("Usage: use <plugin>")
                    else:
                        if command[1] in plugins.keys():
                            current_plugin.append('')
                            pwd += 1
                            current_plugin[pwd] = plugins[commands[1]]
                        else:
                            self.helper.output(self.badges.E + "Invalid plugin!")
                elif commands[0] == "plugins":
                    self.formatter.format_plugins(plugins)
                elif commands[0] == "back":
                    pwd -= 1
                    current_plugin = current_plugin[0:-1]
                    if current_plugin == []:
                        pwd = 0
                        break
                elif commands[0] == "options":
                    self.formatter.format_options(current_plugin[pwd].options, "Plugin")
                elif commands[0] == "details":
                    if len(commands) < 2:
                        self.helper.output("Usage: details <plugin>")
                    else:
                        if commands[1] in plugins.keys():
                            self.plugin.show_details(plugins[commands[1]].details)
                        else:
                            self.helper.output(self.badges.E + "Invalid module!")
                elif commands[0] == "set":
                    if len(commands) < 3:
                        self.helper.output("Usage: set <option> <value>")
                    else:
                        if commands[1] in current_plugin[pwd].options.keys():
                            self.helper.output(self.badges.I + commands[1] + " ==> " + commands[2])
                            current_plugin[pwd].options[commands[1]]['Value'] = commands[2]
                        else:
                            self.helper.output(self.badges.E + "Unrecognized option!")
                elif commands[0] == "run":
                    count = 0
                    for option in current_plugin[pwd].options.keys():
                        if current_plugin[pwd].options[option]['Value'] == '' and current_plugin[pwd].options[option]['Required'] == True:
                            count += 1
                    if count > 0:
                        self.helper.output(self.badges.E + "Missed some required options! (" + count + ")")
                    else:
                        current_plugin[pwd].run()
                else:
                    if current_plugin[pwd].details['HasCommands']:
                        if commands[0] in current_plugin[pwd].commands.keys():
                            if current_plugin[pwd].commands[commands[0]]['NeedsArgs']:
                                if (len(commands) - 1) < current_plugin[pwd].commands[commands[0]]['ArgsCount']:
                                    self.helper.output("Usage:" + current_plugin[pwd].commands[commands[0]]['Usage'])
                                else:
                                    arguments = re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', arguments)
                                    current_plugin[pwd].commands[commands[0]]['ArgsList'] = arguments
                                    current_plugin[pwd].commands[commands[0]]['Run']()
                            else:
                                current_plugin[pwd].commands[commands[0]]['Run']()
                        else:
                            self.helper.output(self.badges.E + "Unrecognized command!")
                    else:
                        self.helper.output(self.badges.E + "Unrecognized command!")
            except (KeyboardInterrupt, EOFError):
                self.helper.output("")
            except Exception as e:
                self.helper.output(self.badges.E + "An error occurred: " + str(e) + "!")