from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [

    url('^$', views.home),
    url('^create/$', views.policy),
    url('^analysis/$', views.analysis),
    url('^user/$', views.user),
    url('^user/display$', views.display_user),
    url('^user/create$', views.create_user),
    url('^user/modify$', views.mod_user),
    url('^user/delete$', views.del_user),

]
