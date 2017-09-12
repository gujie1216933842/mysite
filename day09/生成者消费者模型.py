# Author:Bob
import queue, threading

q = queue.Queue()


def Producer(name):
    for i in range(10):
        q.put('骨头%s' % i)


def Consumer(name):
    while True:
        print('[%s]取到了第[%s]个骨头,并且吃了它.....' % (name, q.get()))


# 启动两个线程
p = threading.Thread(target=Producer, args=('gujie',))
c = threading.Thread(target=Consumer, args=('xiaoxiong',))

p.start()
c.start()
