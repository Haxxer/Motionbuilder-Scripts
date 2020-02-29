import socket
import os
import math

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

                if self._percentage < 10:
                    message = b'00{prc}'.format(prc=self._percentage)
                elif self._percentage < 100:
                    message = b'0{prc}'.format(prc=self._percentage)
                else:
                    message = b'{prc}'.format(prc=self._percentage)

                self.socket.sendall(message)

            except:
                pass

    def __exit__(self, inType, inValue, inTraceback):
        try:
            self.socket.close()
        except:
            pass