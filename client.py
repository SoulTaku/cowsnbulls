#!/usr/bin/python3
import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('localhost', 420)

sock.connect(server)

nick = ''
while nick == '':
    nick = input('Your nickname is: ')
sock.send(nick.encode())

def check(nr):
    for i in range(3):
        for j in range(i+1, 4):
            if choice[i] == choice[j]: return 0

    return 1

while True:
    while True:
        choice = input('Your guess (4 digit number):\n')
        if len(choice) == 4 and choice.isdigit() and check(choice):
            choice = str(choice)
            break

    sock.send(choice.encode())
    data = sock.recv(1024).decode()
    print('\n' + data)
    
    if data.startswith('[+]'):
        print('Wait for other players!')
        while True:
            data = sock.recv(1024).decode()
            print('\n' + data)

            if data == '[!] Next round!': break
	    
