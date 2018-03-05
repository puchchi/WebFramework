
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from django.conf.urls import url
import views

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.optionHome, name="optionHome"),

]