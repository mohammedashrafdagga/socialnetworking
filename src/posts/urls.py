from django.urls import path
from . import views as vs


app_name = 'posts'


urlpatterns = [
    path('', vs.home_page, name='homepage')
]