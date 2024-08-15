#%%
# Van video:
# https://www.youtube.com/watch?v=oEOiBt6mD6Y
#
# Gebruik:
# python3 udprcv.py localhost 4444

#%% Stel die klient op

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#%%

host = sys.argv[1]
port = int(sys.argv[2])
s.bind((host, port))

#%%

while True:
    print('before')
    data, addr = s.recvfrom(1024) # this line blocks
    print('after')

    if data.decode()== 'q':
        break

    print(data.decode(), ' is from ', addr)
