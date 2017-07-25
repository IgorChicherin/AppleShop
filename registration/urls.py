from django.conf.urls import url
from registration.views import registration_view

urlpatterns = [
    url(r'^$', registration_view),
]