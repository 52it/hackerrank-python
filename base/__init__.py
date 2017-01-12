#!/usr/bin/env ptyhon
# -*- coding: utf-8 -*-
import sys, math, decimal


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


def t_1_2():
    n = int(raw_input())
    int_list = tuple(map(int, raw_input().split(' ', n-1)))
    print hash(int_list)


def t_1_3():
    #  x = int(raw_input())
    #  y = int(raw_input())
    #  z = int(raw_input())
    #  n = int(raw_input())
    #  result = []
    #  for i in xrange(x + 1):
        #  for j in xrange(y + 1):
            #  for k in xrange(z + 1):
                #  if i+j+k == n:
                    #  continue
                #  result.append([i, j, k])
    #  print result
# update
    x, y, z, n = [int(raw_input())+1 for _ in xrange(4)]
    n -= 1
    print [[i, j, k] for i in xrange(x) for j in xrange(y) for k in xrange(z) if i+j+k != n]


def t_1_4():
    n = int(raw_input())
    arr = set(map(int, raw_input().split(' ', n-1)))
    max_int = max(arr)
    arr.remove(max_int)
    print max(arr)


def t_1_5():
    #  students = []
    #  scores = set()
    #  for _ in xrange(int(raw_input())):
        #  name = raw_input()
        #  score = float(raw_input())
        #  scores.add(score)
        #  students.append([name, score])
    #  score_list = list(scores)
    #  score_list.sort()
    #  target_score = score_list[1]
    #  results = [n for n, s in students if s == target_score]
    #  results.sort()
    #  for n in results:
        #  print n
#update
    marksheet = []
    for _ in xrange(int(raw_input())):
        marksheet.append([raw_input(), float(raw_input())])
    score_set = set([s for _, s in marksheet])
    score_set.remove(min(score_set))
    target_score = min(score_set)
    result_list = sorted([ n for n, s in marksheet if s == target_score])
    print '\n'.join(result_list)


def t_1_6():
    marksheet = []
    for _ in xrange(int(raw_input())):
        marksheet.append(raw_input().split())
    student = raw_input()
    mark_list = map(float, [x for ss in marksheet if ss[0] == student for x in ss[1:]])
    r = math.fsum(mark_list)/round(len(mark_list), 1)
    print '%.2f' % (r)




if '__main__' == __name__:
    method = sys.argv[1]
    locals()[method]()

