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

from core.io import io
from core.badges import badges

class parser:
    def __init__(self):
        self.io = io()
        self.badges = badges()
        
        self.commands = {
            '%black': self.badges.BLACK,
            '%red': self.badges.RED,
            '%green': self.badges.GREEN,
            '%yellow': self.badges.YELLOW,
            '%blue': self.badges.BLUE,
            '%purple': self.badges.PURPLE,
            '%cyan': self.badges.CYAN,
            '%white': self.badges.WHITE,

            '%end': self.badges.END,
            '%bold': self.badges.BOLD,
            '%dark': self.badges.DARK,
            '%bent': self.badges.BENT,
            '%line': self.badges.LINE,
            '%twink': self.badges.TWINK,
            
            '%empty': ""
        }

    def parse_colors(self, path):
        result = ""
        with open(path) as file:
            for line in file:
                if line[0:8] != "%comment" and not line.isspace():
                    for command in self.commands.keys():
                        line = line.partition('%comment')[0]
                        line = line.replace(command, self.commands[command])
                    result += line
        return result
    
    def parse_options(self, options, option=None):
        if not option:
            values = []
            for option in options.keys():
                values.append(str(options[option]['Value']))
            if len(values) == 1:
                return values[0]
            return values
        else:
            return str(options[option]['Value'])
