from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),  # Post detail and comments
    path('post/<int:pk>/comments/new/', views.comment_create, name='comment-create'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment-edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]

