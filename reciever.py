import socket
import RPi.GPIO as GPIO


DESTINATION = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((DESTINATION, 25565))
    data = s.recv(1024)
    print(data)
    if data == "exit" or "quit":
        s.close()
        sys.exit()
    s.sendall("s")
