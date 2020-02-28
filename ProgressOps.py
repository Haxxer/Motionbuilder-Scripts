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
            self.socket.sendall(self._percentage)

    def __exit__(self, inType, inValue, inTraceback):
        self.socket.close()