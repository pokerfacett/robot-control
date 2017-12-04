# client  
#!usr/bin/python 
import socket  
import time
import sys

def player_notice(s):
    print 'control'
    # Control left up
    try: 
        s.send("\x00\x55\x7b\x22\x63\x6f\x6e\x74\x72\x6f\x6c\x4e\x61\x6d\x65\x22\x3a\x22\x43\x6f\x6e\x74\x72\x6f\x6c\x6c\x65\x72\x43\x68\x61\x6e\x67\x65\x53\x74\x61\x74\x65\x22\x2c\x22\x63\x6f\x6e\x74\x72\x6f\x6c\x50\x61\x72\x61\x6d\x73\x22\x3a\x5b\x22\x4c\x65\x66\x74\x41\x72\x6d\x54\x75\x72\x6e\x53\x69\x6e\x67\x6c\x65\x22\x2c\x31\x2c\x32\x2c\x31\x35\x30\x5d\x7d") 
    except Exception as error1:
        print 'Send package up error!!!'
        print 'Error reason is',error1
    time.sleep(3)
    # Control left down
    try:
        s.send("\x00\x54\x7b\x22\x63\x6f\x6e\x74\x72\x6f\x6c\x4e\x61\x6d\x65\x22\x3a\x22\x43\x6f\x6e\x74\x72\x6f\x6c\x6c\x65\x72\x43\x68\x61\x6e\x67\x65\x53\x74\x61\x74\x65\x22\x2c\x22\x63\x6f\x6e\x74\x72\x6f\x6c\x50\x61\x72\x61\x6d\x73\x22\x3a\x5b\x22\x4c\x65\x66\x74\x41\x72\x6d\x54\x75\x72\x6e\x53\x69\x6e\x67\x6c\x65\x22\x2c\x31\x2c\x32\x2c\x36\x30\x5d\x7d")
        data1 = s.recv(1024)
        print data1
    except Exception as error2:
        print 'Send package down error!!!'
        print 'Error reason is',error2
    time.sleep(5)


def keep_alive(s):
    print 'alive'
    try:
        s.send("\x00\x0a\x52\x4f\x42\x4f\x54\x4c\x45\x56\x45\x4c")
        time.sleep(4)
    except Exception as error:
        print 'Send package live error!!!'
        print 'Error reason is',error

if __name__ == '__main__':
    # package count
    count = 0
    # init socket
    address = ('192.168.1.102', 9007)  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        s.connect(address)
    except Exception as error:
        print "Connect failed!!"
        print error
        s.close()
        sys.exit()
    #player_notice(s)
    while 1:
        try:
            if count != 15:
                keep_alive(s)
                count += 1
                print count
                continue
            if count == 15:
                player_notice(s)
                count = 0
                print count
                continue
            else:
                continue
        except KeyboardInterrupt:
            s.close()
            sys.exit()

