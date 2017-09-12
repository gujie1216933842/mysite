#进程之间共享数据

from  multiprocessing  import  Process,Manager
import  os   #导入操作系统模块
def f(f,l):
    d[os.getpgid()] = os.getpgid()
    l.append(os.getpgid())
    print(l)

if __name__ == '__main__': #判断该脚本是手动执行,还是作为模块被其他脚本引用,如果是手动执行,下面的代码就执行
    with Manager()  as  manager:
        d =  manager.dict()  #生成一个字典对象,可在多个进程间共享和传递
        l =  manager.list(range(5))  #生成一个列表,可在多个进程间共享和传递
        p_list = []
        for i in range(10):
            p = Process(target=f,args=(f,l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)