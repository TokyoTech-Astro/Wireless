import sys
import socket

ENCODE = "utf-8"


def sendStr(conn, msg, enc=ENCODE):
    conn.send(msg.encode(encoding=enc))


def recieveStr(conn, enc=ENCODE, size=1024):
    return conn.recv(size).decode(encoding=enc)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 25565))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print(addr)
        with conn:
            while True:
                data = input(">")
                sendStr(conn, data)
                data = recieveStr(conn)
                if data == "f":
                    print("Failed.")
                    sendStr(conn, "exit")
                    sys.exit()
                elif data == "s":
                    print("Succeed.")
                else:
                    print("Unexpected Responce: {}".format(data))
                    sendStr(conn, "exit")
                    conn.close()
                    sys.exit()
                if data == "quit" or data == "exit":
                    conn.close()
                    sys.exit()
