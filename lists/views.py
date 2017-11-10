from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request,'home.html')#第一个参数是请求对象，第二个参数是渲染的模板名
