from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView,PostUpdateView,PostDeleteView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]