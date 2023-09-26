from django.urls import path, include
from . import views

from .dashboards import test_dash

urlpatterns = [
    path('', views.test1), #connect to function-test1 (inside view.py)  
    path('django_plotly_dash/', include('django_plotly_dash.urls'))
]
