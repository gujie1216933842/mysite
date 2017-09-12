

import os
import sys
import  redis
#os.path.dirname(os.__file__)
#print(sys.path)

#print(redis)
r = redis.Redis(host='192.168.42.30', port='6379')
print(r)
r.set('xx','xiap')
print(r.get('gujie'))


