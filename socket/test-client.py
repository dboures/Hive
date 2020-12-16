import socket


s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =  "192.168.1.30"
port = 5555

print('Waiting for connection')
try:
    s.connect((host,port))
except s.error as e:
    print(str(e))

response = s.recv(2048)
while True:
    ins = 'This is my input'
    s.send(str.encode(ins))
    response = s.recv(2048)
    print(response.decode('utf-8'))

s.close()

