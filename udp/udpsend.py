#%%
# Van video:
# https://www.youtube.com/watch?v=oEOiBt6mD6Y
#
# Gebruik:
# python3 udpsend.py localhost 4444


import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = sys.argv[1]
port = int(sys.argv[2])

# 'n socket is 'n pyp wat aan 'n poort konnekteer

line = input('type message: ') # send only once ==== blocking
line = line.encode()
s.sendto(line, (host, port))