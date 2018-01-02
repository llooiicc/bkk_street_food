'''
Created on 2 janv. 2018

@author: Loic.Rondel
'''
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$' , views.login , name='login')
]

