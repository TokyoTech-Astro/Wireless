import sys
import socket


DESTINATION = ""
ENCODE = "utf-8"


def sendallStr(conn, msg: str, enc=ENCODE: str):
    conn.sendall(str.encode(encoding=encode))


def recieveStr(conn, enc=ENCODE: str, size=1024: int):
    return conn.recv(size).decode(encoding=enc)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((DESTINATION, 25565))
    data = recieveStr(s)
    print(data)
    if data == "exit" or "quit":
        s.close()
        sys.exit()
    sendallStr(s, "s")
