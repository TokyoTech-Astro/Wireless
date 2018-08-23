import sys
import socket
import RPi.GPIO as GPIO


DESTINATION = ""
ENCODE = "utf-8"
PIN = 0

def sendStr(conn, msg, enc=ENCODE):
    conn.send(msg.encode(encoding=enc))


def recieveStr(conn, enc=ENCODE, size=1024):
    return conn.recv(size).decode(encoding=enc)


GPIO.setmode(GPIO.BUM)
GPIO.setup(PIN, GPIO.OUT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((DESTINATION, 25565))
    while True:
        data = recieveStr(s)
        print(data)
        if data == "on":
            GPIO.output(PIN, GPIO.HIGH)
            print(" -> DONE" end="")
        elif data == "off":
            GPIO.output(PIN, GPIO.LOW)
            print(" -> DONE" end="")
        sendStr(s, "s")
        if data == "exit" or data == "quit":
            print()
            s.close()
            GPIO.cleanup()
            sys.exit()
        print(";")
