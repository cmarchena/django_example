# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .forms import RegisterForm, PostForm
from .models import Post, Profile
from .serializers import PostSerializer
import requests
def home(request):
    # return HttpResponse("Hello, welcome to my app!")
    return render(request, 'myapp/home.html')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the list of posts after saving

            # Redirect to a success page or display a success message
    else:
        form = PostForm()
    return render(request, 'myapp/create_post.html', {'form': form})

def post_list(request):
    """  # posts = Post.objects.all()
    published_posts = Post.objects.filter(status='published')
    return render(request,  'myapp/post_list.html', {'posts': published_posts}) """
    # Fetch data from the API endpoint
    response = requests.get('http://127.0.0.1:8000/api/posts/')
    # filter response by  status

    data = response.json() if response.status_code == 200 else []
    published_posts = [item for item in data if item.get('status') == "published"]

    # Pass the data to the template
    return render(request, 'myapp/post_list.html', {'posts': published_posts})

""" @login_required
def post_list(request):
    # posts = Post.objects.all()
    published_posts = Post.objects.filter(status='published')
    return render(request,  'myapp/post_list.html', {'posts': published_posts}) """
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')  # Redirect to a page after registration
    else:
        form = RegisterForm()
    
    return render(request, 'myapp/register.html', {'form': form})

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'myapp/profile.html', {'profile': profile})

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
