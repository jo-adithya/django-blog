from django.urls.conf import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    re_path(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_update'),
    re_path(r'^post/(?P<pk>\d+)/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='draft_list'),
]
