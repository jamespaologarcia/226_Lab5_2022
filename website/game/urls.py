from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('get/<int:token>', views.get, name='get'),
    path('put/<int:level>/<int:row>/<int:col>/<int:token>', views.put, name='put'),
    path('clear/<int:token>', views.clear, name='clear')
]