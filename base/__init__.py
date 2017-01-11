#!/usr/bin/env ptyhon
# -*- coding: utf-8 -*-
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


def t4():
    a = int(raw_input())
    b = int(raw_input())
    print (a+b)
    print (a-b)
    print (a*b)


def t5():
    a = int(raw_input())
    b = int(raw_input())
    print a // b
    print a / b


def t6():
    n = int(raw_input())
    for i in range(0, n):
        print i * i


def t7():
    leap = False
    year = int(raw_input())
    if (year % 4 == 0 and year % 100 > 0) or year % 400 == 0:
        leap = True
    print leap


def t8():
    n = int(raw_input())
    #  print(*range(1, n+1), sep = '')
    result = 0
    for i in range(1, n+1):
        n -= 1
        if i < 4:
            result += i * pow(10, n)
        elif i == n:
            result
    print result


def t_1_1():
    mylist = list()
    for i in xrange(int(raw_input())):
        __operate_list(mylist, raw_input())


def __operate_list(data_list, strparam):
    if not strparam:
        return
    if 'print' == strparam:
        print data_list
    elif strparam.startswith('insert'):
        params = strparam.split(' ', 3)
        data_list.insert(int(params[1]), int(params[2]))
    elif strparam.startswith('remove'):
        params = strparam.split(' ', 2)
        data_list.remove(int(params[1]))
    elif strparam.startswith('append'):
        params = strparam.split(' ', 2)
        data_list.append(int(params[1]))
    elif strparam.startswith('sort'):
        data_list.sort()
    elif strparam.startswith('pop'):
        data_list.pop()
    elif strparam.startswith('reverse'):
        data_list.reverse()



if '__main__' == __name__:
    method = sys.argv[1]
    locals()[method]()

