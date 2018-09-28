import sys
import socket
import RPi.GPIO as GPIO


DESTINATION = ""
ENCODE = "utf-8"

def sendStr(conn, msg, enc=ENCODE):
    conn.send(msg.encode(encoding=enc))


def recieveStr(conn, enc=ENCODE, size=1024):
    return conn.recv(size).decode(encoding=enc)


def send(conn, value):
    conn.send(value.to_bytes(1, 'big'))


def recieve(conn, size=256):
    return int.from_bytes(conn.recv(size), 'big')


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((DESTINATION, 25565))
    s.recieve = recieve

    try:
        while True:
            data = recieveStr(s)
            print(data)
            if data & 0b10000000 == 0b10000000:
                pin = data ^ 0b10000000
                GPIO.output(pin, GPIO.HIGH)
                print("TURN ON: %d -> DONE" % pin)
            elif data != 0b01111111:
                pin = data
                GPIO.output(pin, GPIO.LOW)
                print("TURN OFF: %d -> DONE" % pin)
            else:
                GPIO.cleanup()
                break
            send(s, 0)
    except:
        print("EXCEPTION WAS THROWN")
        send(s, 1)

print("EXITING NOW...")
