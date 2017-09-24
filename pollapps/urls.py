from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.PollList.as_view()),

    # poll / p_id
    url(r'^(?P<p_id>[0-9]+)/$', views.pollById.as_view()),
    
]