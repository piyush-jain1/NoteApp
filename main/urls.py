from django.conf.urls import include, url
from . import views

app_name = 'main'

urlpatterns = [
	url(r'^user/home$', views.user_home, name='user_home'),
	url(r'^user/login$', views.user_login, name='user_login'),
	url(r'^user/signup', views.user_signup, name='user_signup'),
]
