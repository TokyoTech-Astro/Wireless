import sys
import socket


DESTINATION = ""
ENCODE = "utf-8"


def sendStr(conn, msg, enc=ENCODE):
    conn.send(msg.encode(encoding=enc))


def recieveStr(conn, enc=ENCODE, size=1024):
    return conn.recv(size).decode(encoding=enc)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((DESTINATION, 25565))
    while True:
        data = recieveStr(s)
        print(data, end="")
        if data == "exit" or "quit":
            s.close()
            sys.exit()
        sendStr(s, "s")
        print(";")
