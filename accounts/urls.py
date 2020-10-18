from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
#from django.conf import settings
app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^login/$' , login , {'template_name':'login.html'}, name='login')
    url(r'^login/$',LoginView.as_view(template_name='login.html'), name='login'),
    #url(r'^logout/$' , logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'signup$' , views.register, name='register'),
    url(r'^(?P<slug>[-\w]+)/$', views.profile, name='profile'),
]
