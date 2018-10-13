
import socket, sys

for hostname in sys.argv[1:]:
   ip = repr(socket.gethostbyname_ex(hostname)[2])[2:-2]
   print ip
