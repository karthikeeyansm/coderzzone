from django.urls import path
from mailsender import views

urlpatterns=[
    path('',views.home,name="home"),
    path('send',views.send,name="send"),

]