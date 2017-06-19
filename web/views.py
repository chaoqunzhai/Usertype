from django.shortcuts import render,HttpResponse
from django.views import View
from web import forms
from web import models
from web.fusion import Info


class Webinfo(View):

    def get(self,request,*args,**kwargs):
        status_tag = ''
        userinform = forms.UserFrom()
        workFrom = forms.WorkFrom()
        return render(request,'info.html',{'userinform':userinform,'workFrom':workFrom,'status':status_tag})


    def post(self,request,*args,**kwargs):
        status_tag= ''
        token_error= ''
        userinform = forms.UserFrom(request.POST)
        workFrom = forms.WorkFrom(request.POST)
        if userinform.is_valid() and workFrom.is_valid():
            status_tag = True
            print("userdata:%s,workdata:%s" %(userinform.cleaned_data,workFrom.cleaned_data))
            user_token = request.POST.get('token')
            user_content = request.POST.get('content')
            user_datatime = request.POST.get('datetime')
            obj = models.User.objects.filter().values('id','token')
            work_dict = {'datetime': user_datatime, 'content': user_content}
            for i in obj:
                if str(i['token']) == user_token:
                    work_dict['uid_id'] = i['id']
                    models.Works.objects.create(**work_dict)
                    print('yes',work_dict)
                    return render(request,'suceess.html')
                else:
                    token_error = 'token认证错误'
                    return render(request, 'info.html',
                                  {'userinform': userinform, 'workFrom': workFrom, 'status': status_tag,'token_error':token_error})
        else:
            print('userinform:%s,workFrom:%s' %(userinform.errors.as_json,workFrom.errors.as_json))
            return render(request, 'info.html', {'userinform': userinform, 'workFrom': workFrom, 'status': status_tag})
        return render(request, 'info.html', {'userinform': userinform, 'workFrom': workFrom,'status':status_tag,'token_error':token_error})
