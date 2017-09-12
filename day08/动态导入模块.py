
#导入模块
#modname = 'aa'
mod = __import__('lib.aa')
obj = mod.aa.C()
print(obj.name)


#官方建议
import importlib
aa = importlib.import_module('lib.aa')
print(aa.C().name)