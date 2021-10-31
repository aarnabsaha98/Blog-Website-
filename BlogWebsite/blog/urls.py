from django.urls import path
from . import views 
from .views import PostListView,PostDetailView ,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,ReplyUserListView,ReplyCreateView


urlpatterns = [
    
# now instead of this we can use list of the blogs
    # path('' ,views.home , name='blog-home'),
    # and apparently it will go for a template for a specific namuing
    # conviction i.e. >  <app>/<model>_<viewtype>.html  > blog/post_list.html 
    path('',PostListView.as_view(),name='blog-home'),
    path('leave-reply/',ReplyUserListView.as_view(),name='leave-reply'), 
    path('post/comment/',ReplyCreateView.as_view(),name='leave-reply-post'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('about/',views.about , name = 'blog-about'),
    path('topic/',views.topic , name = 'blog-topic'),

]