from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect


# Create your views here.


def index(request):
    if request.method == "GET":
        return HttpResponse('index')


def login(request):
    if request.method == 'POST':
        obj = request.FILES.get('pic')
        print(obj, type(obj), obj.name)

        f = open(obj.name, mode='wb')
        for i in obj.chunks():
            f.write(i)
        f.close()
    return render(request, 'login.html')  # 重定向,跳转其他页面
