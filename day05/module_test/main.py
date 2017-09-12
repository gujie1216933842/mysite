#Author:Bob

# import  module_gujie
# module_gujie.log()
#from module_gujie import *  #把module_gujie模块中的代码都拉到这和位置,慎用
#from module_gujie import log as log_gujie  导入方法起别名




from module_gujie import log as log_gujie  #把module_gujie模块中的代码都拉到这和位置,慎用
def log():
    print('我是main文件中的方法')

log_gujie()
