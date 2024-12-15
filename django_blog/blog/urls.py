from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import PostListView, PostDetailView, PostByTagListView
from .views import home_view
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', home_view, name='home'),  # The empty string ('') represents the root URL
    path('', PostListView.as_view(), name='post-list'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Replace 'blog' with your app name
    path('base/', views.base_template_view, name='base'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post-by-tag'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),  # Post detail and comments
    path('post/<int:pk>/comments/new/', views.comment_create, name='comment-create'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment-edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', views.search, name='search'),
    path('tags/<str:tag_name>/', views.tag_detail, name='tag-detail'),
]

