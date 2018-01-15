
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from django.conf.urls import url

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),

]