import socket


DESTINATION = sys.argv[0]


def sendallStr(conn, msg:str, encode="UTF-8"):
    conn.sendall(str.encode(encode))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((DESTINATION, 25565))
    data = s.recv(1024)
    print(data)
    if data == "exit" or "quit":
        s.close()
        sys.exit()
    sendallStr(s, "s")
