from django.conf.urls import url
from .views import admin_view, get_user, del_user, edit_content, delete_content, add_content, ManageConntentListView, \
    PreviewContentDetailView, CategoriesListView, CategoriesCreateView, delete_category, CategoriesUpdateView

urlpatterns = [
    url(r'^$', admin_view),
    url(r'get_user/(\d+)/$', get_user),
    url(r'del_user/(\d+)/$', del_user),
    url(r'content/$', ManageConntentListView.as_view()),
    url(r'categories/$', CategoriesListView.as_view()),
    url(r'categories/add/$', CategoriesCreateView.as_view()),
    url(r'categories/delete/(\d+)$', delete_category),
    url(r'categories/edit/(?P<pk>\d+)/$', CategoriesUpdateView.as_view()),
    url(r'content/edit/(\d+)/$', edit_content),
    url(r'content/delete/(\d+)/$', delete_content),
    url(r'content/add/$', add_content),
    url(r'content/preview/(?P<pk>\d+)/$', PreviewContentDetailView.as_view()),
]
