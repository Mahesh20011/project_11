from app.views import *
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('mahesh/',mahesh,name='mahesh')
]