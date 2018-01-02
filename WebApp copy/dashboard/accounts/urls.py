from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.profile, name='profile'),
	#url(r'^test_page/$', views.test_page),
	#url(r'^test_page/', views.tables2),
	#url(r'^dbtest/$', views.dbtest),
	url(r'^buttons/$', views.buttons),
	url(r'^buttons/', views.tables)
]