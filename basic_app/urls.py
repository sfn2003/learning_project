from django.conf.urls import url
from django.urls import path
from basic_app import views
# TEMPLATE TAGGING

app_name = 'basic_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('relative/', views.relative, name='relative'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('special/', views.special, name='special'),

]