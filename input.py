import getpass

import socket
_username = 'gujie'
_password = '123'

username = input('username:')
password = input('password:')


if username == _username and password != _password:
    print('password is valide')
elif username !=_username and password ==_password:
    print('username is valide')
elif username !=_username and password !=_password:
	print('password and username is both valide')
else:
    print('login is success')



