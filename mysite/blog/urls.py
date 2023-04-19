from django.conf.urls import url
from blog import views

urlpatterns = [
     url('about/', views.AboutView.as_view(), name='about'),
     url("/", views.PostListView.as_view(),name='post_list'),
     url('post/(?P<pk>\d+)$', views.PostDetailView.as_view(),name='post_detail'),
     url('post/new/$', views.CreatePostView.as_view(),name='post_new'),
     url('post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name="post_edit"),
     url('post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
     url('drafts/$',views.DraftListView.as_view(),name='post_draft_list')
]
