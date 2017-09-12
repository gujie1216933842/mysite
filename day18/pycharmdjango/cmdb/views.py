from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
USER_LIST = []
def home(request):
    if request.method == "POST":
        n = request.POST.get('name', None)
        e = request.POST.get('email', None)
        g = request.POST.get('gender', None)
        tmp = {'name': n, 'email': e, 'g': gender}
        USER_LIST.append(tmp)
    return render(request, 'home.html', {'user_list': USER_LIST})


def login(request):
    # request.POST['username']
    # request.POST['password']
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username', None)  # request.Post是字典格式的数据
        password = request.POST.get('password', None)
        print(username, password)

        if username == 'root' and password == '123':

            for index in range(20):
                tmp = {'name': '大雄'+str(index), 'email': '123@qq.com', 'gender': '男'}
                USER_LIST.append(tmp)

            # 去跳转
            return redirect('/home')
        # 用户名或密码不匹配
        else:
            error_msg = '用户名或密码错误'
    return render(request, 'login.html', {'error_msg': error_msg})
