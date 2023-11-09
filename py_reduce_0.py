
#see: https://www.programcreek.com/python/?CodeExample=send+packet

import socket
import plistlib
import struct

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.connect(("127.0.0.1", 1024)) #be sure to replace that otherwise you will
                                  #hack yourself. On the other hand, this is not really a problem for tests


#def send_packet(self, payload: dict, reqtype: int = 8):
def send_packet( payload: dict, reqtype: int = 8):
        """
        Args:
            payload: required

            # The following args only used in the first request
            reqtype: request type, always 8 
            tag: int
        """
        body_data = plistlib.dumps(payload)
        # if self._first:  # first package
        #length = 16 + len(body_data)
        length_my_hack = 1000
        header = struct.pack(
        "hlll", 
        length_my_hack,
        1, reqtype,
        1)
        
        sock.sendall(header)# + body_data) 



while 1:
    send_packet("no_payload")