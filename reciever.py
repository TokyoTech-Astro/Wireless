import sys
import socket


DESTINATION = ""
ENCODE = "utf-8"


def sendallStr(conn, msg, enc=ENCODE):
    conn.sendall(msg.encode(encoding=enc))


def recieveStr(conn, enc=ENCODE, size=1024):
    return conn.recv(size).decode(encoding=enc)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((DESTINATION, 25565))
    while True:
        data = recieveStr(s)
        print(data)
        if data == "exit" or "quit":
            s.close()
            sys.exit()
        sendallStr(s, "s")
