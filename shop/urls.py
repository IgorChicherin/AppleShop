from django.conf.urls import url
from shop.views import index_view, iphone_view, about_view, contacts_view, MacListView, IpadListView, IwatchListView

urlpatterns = [
    url(r'^$', index_view),
    url(r'^index/$', index_view),
    url(r'^mac/$', MacListView.as_view()),
    url(r'^iphone/$', iphone_view),
    url(r'^ipad/$', IpadListView.as_view()),
    url(r'^iwatch/$', IwatchListView.as_view()),
    url(r'^about/$', about_view),
    url(r'^contacts/$', contacts_view),
]