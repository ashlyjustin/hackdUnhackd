from django.conf.urls import url
from . import views

app_name = 'user_login'

urlpatterns =[
	url(r'^register/$',views.register,name="register"),
	url(r'^$',views.homepage,name="homepage"),
	url(r'^user_login/$',views.user_login,name="user_login"),
	url(r'^logout/$',views.user_logout,name="logout"),
	url(r'^user/$',views.user_page,name="user_page"),
	url(r'^user/$',views.apply_page,name="apply")


	]