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

import os

class colors_script:
    def __init__(self):
        self.script_extension = "colors"
        
        self.commands = {
            '%black': '\033[30m',
            '%red': '\033[31m',
            '%green': '\033[32m',
            '%yellow': '\033[33m',
            '%blue': '\033[34m',
            '%purple': '\033[35m',
            '%cyan': '\033[36m',
            '%white': '\033[77m',

            '%end': '\033[0m',
            '%bold': '\033[1m',
            '%dark': '\033[2m',
            '%bent': '\033[3m',
            '%line': '\033[4m',
            '%twink': '\033[5m',
            '%back': '\033[7m'
        }

    def read_file_lines(self, path):
        lines = list()
        with open(path) as file:
            for line in file:
                lines.append(line)
        return lines
        
    def parse_colors_script(self, path):
        result = ""
        lines = self.read_file_lines(path)
        last_command = ""
        last_line = lines[-1]
        for command in self.commands.keys():
            if command in last_line:
                last_command += command
                last_line = last_line.replace(command, " ")
        if last_line.isspace():
            lines.pop()
            lines[-1] = last_command + lines[-1]
        if path.endswith(self.script_extension):
            try:
                for line in lines:
                    if line[0:8] != "%comment" and not line.isspace():
                        buffer_line = line
                        temp_buffer = ""
                        for command in self.commands.keys():
                            if command in buffer_line:
                                temp_buffer += command
                                buffer_line = buffer_line.replace(command, " ")
                        if buffer_line.isspace():
                            buffer_commands += temp_buffer
                        if not buffer_line.isspace():
                            line = buffer_commands + line
                            buffer_commands = ""
                            for command in self.commands.keys():
                                line = line.partition('%comment')[0]
                                line = line.replace('%empty', "")
                                line = line.replace(command, self.commands[command])
                            result += line
                return result
            except:
                return None
        else:
            return None

    def compile_colors_script(self, path, outfile='a.out'):
        result = self.parse_colors_script(path)
        if result:
            output = open(outfile, 'wb')
            output.write(result.encode())
            output.close()
