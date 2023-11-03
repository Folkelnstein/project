from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('',index, name ='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post , name='advertisement-post'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('advertisement/<int:pk>',advertisement_detail, name ='adv-detail')
]