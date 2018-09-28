import sys
import socket

ENCODE = "utf-8"


def sendStr(conn, msg, enc=ENCODE):
    conn.send(msg.encode(encoding=enc))


def recieveStr(conn, enc=ENCODE, size=1024):
    return conn.recv(size).decode(encoding=enc)


def send(conn, value):
    conn.send(value.to_bytes(1, 'big'))


def recieve(conn, size=256):
    return int.from_bytes(conn.recv(size), 'big')


def sendExit(conn):
    send(conn, 0b01111111)


def sendCode(conn, toggle=True, port=0):
    value = 0
    if toggle:
        value = 0b10000000
    value += port
    send(conn, value)


def communicate(service):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 25565))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            print(addr)
            with conn:
                try:
                    while service(conn):
                        if recieve(conn) != 0:
                            raise Exception
                except Exception as e:
                    send(conn, 0b01111111)
                    print(e)
                    break
    print("EXITING NOW...")


def defaultService(conn):
    inp = input("On, off or exit? :")
    if inp.lower() in "exit":
        sendExit()
        return False
    t = True
    if inp.lower() in "on":
        pass
    elif inp.lower() in "off":
        t = False
    else:
        print("Invalid value.")
        return True
    
    inp = input("Pin? :")
    pin = 0
    try:
        pin = int(inp)
    except ValueError as e:
        print("Invalid value.")
        return True
    if pin > 128 or pin < 0:
        print("Invalid value.")
        return True
    sendCode(conn, t, pin)


if __name__ == '__main__':
    communicate(mainService)
        