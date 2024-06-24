from django.urls import path
from .views import PostDetailView, PostListCreateView, create_post, post_list, register, profile_view
from django.contrib.auth.views import LoginView, LogoutView
# from . import views

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('', post_list, name='post_list'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout URL
    path('profile/', profile_view, name='profile'),  # Profile URL
    # API endpoints
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # path('', views.home, name='home'),
]
