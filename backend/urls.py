from django.urls import path
from django.conf.urls import url

from backend.djangoapps.sample import views as SampleViews
from backend.djangoapps.login import views as LoginViews
from backend.djangoapps.logout import views as LogoutViews

from backend.djangoapps.index import views as IndexViews

urlpatterns = [
    # main-url
    url('sample$', SampleViews.sample, name='sample'),

    url('login$', LoginViews.login, name='login'),
    url('logout$', LogoutViews.logout, name='logout'),

    url('$', IndexViews.index, name='index'),
]
