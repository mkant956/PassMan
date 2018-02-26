#!/usr/bin/python

import sys    
import termios
import fcntl
import os

def getch(prompt):
    print prompt
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    try:        
        while 1:            
            try:
                c = sys.stdin.read(1)
                break
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        return c

def getint(prompt):
    while True:
            response = getch(prompt)
            try:
                response = int(response)
                return response
            except Exception as e:
                print "Enter valid input"

if __name__ == '__main__':
    print myGetch()