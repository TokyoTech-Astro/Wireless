import socket

def sendStr(conn, msg:str, encode="UTF-8"):
    conn.send(str.encode(encode))

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
                data = conn.recv(1024)
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
                if data == "quit" or "exit":
                    conn.close()
                    sys.exit()
