# Author:Bob

import threading, time


def run1():
    print('grap the first time')
    lock.acquire()
    global num1  # 定义一个全局变量
    num1 += 1
    lock.release()  # 释放锁
    return num1


def run2():
    print('grap the second part')
    lock.acquire()
    global num2
    num2 +=1
    lock.release()
    return num2

def run3():
    lock.acquire()
    res = run1()
    print('----between run1 and run2-----')
    res2=run2()
    lock.release()
    print(res,res2)


if __name__ == '__main__':
    num1, num2 = 0, 0
    lock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() !=1:
    print(threading.active_count())
else:
    print('---all threading done-----')
    print(num1,num2)
