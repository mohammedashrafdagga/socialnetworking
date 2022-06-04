from django.urls import path
from . import views as vs


app_name = 'posts'


urlpatterns = [
    path('', vs.home_page, name='homepage'),
    path('post-json/', vs.post_view_json, name='post-json'),
]
