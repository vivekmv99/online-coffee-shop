from django.conf.urls import url
from cafeapp.views import *
from cafeapp.models import register

urlpatterns = [
    url(r'^hello/', hello,name="hello"),
    url(r'^reg/',reg,name="reg"),
    url(r'^show',show,name="show"),
    url(r'^hello1/', hello1,name="hello1"),
    url(r'^log/',log,name="log"),
    url(r'^hello2/', hello2,name="hello2"),
    url(r'^hello3/(\d+)/', hello3,name="hello3"),
    url(r'^hello4/(\d+)/', hello4,name="hello4"),
]
