import socket

UDP_IP = "127.0.2.1"
UDP_PORT = 45278

sock = socket.socket()
sock.bind((UDP_IP, UDP_PORT))
sock.listen(10)
while True:
    conn, addr = sock.accept()

    print ("connect to " + addr)


    data = conn.recv(1024).decode()
    conn.send(data.upper())
conn.close()
