from django.shortcuts import HttpResponse,redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == int('404'):
            print("middleware",response.status_code)
            # return render(request,'info.html')
            return HttpResponse('<a style="text-decoration:none;"  class="btn btn-info" href="http://127.0.0.1:8000/web/info.html">您访问的页面不存在,点击跳转到正确页面</a>')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        pass

        # print("process_view____视图调用之前会先执行这个process_view:",self,request,view_func,view_args,view_kwargs)

    def process_exception(self,request,exception):
        token_error =''
        print("proces exception",exception,request,exception)
        # return redirect('error.html')

        return HttpResponse("<h1>您访问的页面%s不存在！错误信息:%s,%s</h1>" %(exception,request,exception))
