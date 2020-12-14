from core.badges import badges

class ZetaSploitModule:
    def __init__(self):
        self.badges = badges()
        
        self.details = {
            'Name': "",
            'Authors': [
                ''
            ],
            'Description': "",
            'Comments': [
                ''
            ]
        }
        
        self.options = {
            'OPTION': {
                'Description': "",
                'Value': "",
                'Required': True
            }
        }
        
        self.commands = {
            'command': {
                'Description': "",
                'Usage': "",
                'ArgsCount': 0,
                'NeedsArgs': False,
                'Args': [],
                'Run': self.command
            },
        }
        
    def command(self):
        pass
      
    def run(self):
        pass
