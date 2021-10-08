class Colors:
    def __init__(self):
        self.colors = {
            'default':'\033[0;0m',
            'green':'\033[32m',
            'red':'\033[31m',
            'blue':'\033[34m'
        }
    
    def print(self, msg ,color_name='default', *args, **kwargs):
        return print(f'{self.colors.get(color_name)}{msg}{self.colors["default"]}', *args, **kwargs)



