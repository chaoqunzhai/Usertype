from . import models
from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^info.html$',views.Webinfo.as_view()),
]