#!/usr/bin/python
#--*--utf-8--*--
import sys


def t1():
    print 'Hello World!'


def t2():
    s = raw_input()
    print s


def t3():
    n = int(raw_input())
    if n % 2 == 1:
        print 'Weird'
    else:
        if n >= 6 and n <= 20:
            print 'Weird'
        else:
            print 'Not Weird'


if '__main__' == __name__:
    method = sys.argv[1]
    locals()[method]()

