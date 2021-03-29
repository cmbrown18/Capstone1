from django.conf.urls import url
from . import views


urlpatterns = [

    #url('', views.home, name='home-page'),
    #url('about/', views.about, name='about-page'),

    url('^$', views.HomePageView.as_view()),
    url('^about/$', views.AboutPageView.as_view()),
    url('^create/$', views.CreatePageView.as_view()),
    url('^analysis/$', views.AnalysisPageView.as_view()),
   #url('^analysis/display', views.DisplayPageView.as_view()),
    url('^user/$', views.UserPageView.as_view()),
    url('^user/display$', views.DisUserPageView.as_view()),
    url('^user/create$', views.CreUserPageView.as_view()),
    url('^user/modify$', views.ModUserPageView.as_view()),
    url('^user/delete$', views.DelUserPageView.as_view()),
]
