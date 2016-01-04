from app.views import HelloView
from django.conf.urls import url

urlpatterns = [
    url(r'^hello/$', HelloView.as_view()),
]
