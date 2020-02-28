import socket
import os

class ExternalProgressBar():

    def __enter__(self):

        path = os.path.join(
            os.path.dirname(__file__),
            'progressbar.bat'
        )
        
        os.startfile(path)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('localhost', 10000))
        self._percentage = b""
    
    def set_percentage(self, inPercentage):
        if self._percentage != inPercentage:
            self._percentage = inPercentage

            #In case the connection dropped, wrap in try
            try:
                # Send percentage to socket and wait for reply
                self.socket.sendall(self._percentage)
                self.socket.recv(3)
            except:
                pass

    def __exit__(self, inType, inValue, inTraceback):
        try:
            self.socket.close()
        except:
            pass