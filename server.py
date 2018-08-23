import socket


HERE = socket.gethostname()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HERE, 25565))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = input(">")
                conn.send(data)
                data = conn.recv(1024)
                if data == "f":
                    print("Failed.")
                    conn.send("exit")
                    sys.exit()
                elif data == "s":
                    print("Succeed.")
                else:
                    print("Unexpected Responce: {}".format(data))
                    conn.send("exit")
                    conn.close()
                    sys.exit()
                if data == "quit" or "exit":
                    conn.close()
                    sys.exit()
