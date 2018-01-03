'''
Created on 3 janv. 2018

@author: Loic.Rondel
'''

from django.conf.urls import url
from . import views

urltemplattes = [
    url(r'^$', views.set_bounds_map,  name="set_bounds"),
    url(r'home', views.home,  name="home"),
]
