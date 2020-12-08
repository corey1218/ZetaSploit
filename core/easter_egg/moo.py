import sys
import textwrap

from core.helper import helper

class moo:
    def __init__(self):
        self.helper = helper()
        
    def moo(self):
        self.helper.ouput(cowsay("No easter egg could be found."))
        
    def cowsay(self, str, length=40):
	      return build_bubble(str, length) + self.build_cow()

    def build_cow(self):
	      return """
              \  ^__^ 
               \ (oo)\_______
                 (__)\       )\/\\
                     ||----w |
                     ||     ||
        """

    def build_bubble(self, str, length=40):
	      bubble = []
	      lines = self.normalize_text(str, length)
	      bordersize = len(lines[0])
	      bubble.append("  " + "_" * bordersize)
	      for index, line in enumerate(lines):
		        border = self.get_border(lines, index)
		        bubble.append("%s %s %s" % (border[0], line, border[1]))
	      
        bubble.append("  " + "-" * bordersize)
	      return "\n".join(bubble)

    def normalize_text(self, str, length):
	      lines  = textwrap.wrap(str, length)
	      maxlen = len(max(lines, key=len))
	      return [line.ljust(maxlen) for line in lines]

    def get_border(self, lines, index):
	      if len(lines) < 2:
		        return [ "<", ">" ]
	      elif index == 0:
		        return [ "/", "\\" ]
	      elif index == len(lines) - 1:
		        return [ "\\", "/" ]
	      else:
		        return [ "|", "|" ]
