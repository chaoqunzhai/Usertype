from django.forms import Form
from django.forms import widgets
from django.forms import fields



class UserFrom(Form):
    token = fields.CharField(
        max_length='40',
        min_length='10',
        label='认证token',
        widget=widgets.TextInput(attrs={'class': 'form-control ','placeholder':'请输入值,最小为10,不超过40'}),
        error_messages={
            'required':'不能为空',
            'min_length':'最小为10个字符',
            'max_length':'最多为40个字符',
        }

    )
class WorkFrom(Form):
    datetime = fields.DateTimeField(
        label='日期',
        widget=widgets.DateInput(attrs={'class':'form-control ','placeholder':'日期格式2015-09-01 11:12'}),
        error_messages={
            'required':'不能为空',
            'invalid':'时间格式错误'
        }
    )
    content = fields.CharField(
        label='反馈内容',
        widget=widgets.Textarea(attrs={'class':'id_body form-control','placeholder':'故障'}),

    )