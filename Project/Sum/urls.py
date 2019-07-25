from django.urls import path

from . import views


urlpatterns=[
    path('',views.Sum,name='add'),
    path('add',views.add,name='Addition')
]