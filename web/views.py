from django.shortcuts import render,HttpResponse
from django.views import View
from web import forms
from web import models


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
            token_list=[]
            # for i in obj:
            #     token_list.append(i)
            #     print('111111', i['id'], i['token'], token_list)
            try:
                for i in obj:
                    if user_token == str(i['token']):
                        work_dict['uid_id'] = i['id']
                        models.Works.objects.create(**work_dict)
                        print('insert db  usertoken',work_dict)
                        return render(request, 'suceess.html')
                    else:
                        print('else---',i['token'],user_token)
                        token_error = 'token认证错误'


                return render(request, 'info.html',
                                      {'userinform': userinform, 'workFrom': workFrom, 'status': status_tag,
                                       'token_error': token_error})
            except Exception as e:
                datetime_errors = '时间重叠'
                return render(request, 'info.html',
                              {'userinform': userinform, 'workFrom': workFrom, 'status': status_tag,
                               'datetime_errors': datetime_errors})
        else:
            print('userinform:%s,workFrom:%s' %(userinform.errors.as_json,workFrom.errors.as_json))
            return render(request, 'info.html', {'userinform': userinform, 'workFrom': workFrom, 'status': status_tag})
