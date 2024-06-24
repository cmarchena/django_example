# tests/test_posts_api.py

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from myapp.models import Post

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_post():
    return Post.objects.create(title='Test Title', content='Test Content')

@pytest.mark.django_db
def test_list_posts(api_client):
    # Create some sample posts
    Post.objects.create(title='Test Post 1', content='Test Content 1')
    Post.objects.create(title='Test Post 2', content='Test Content 2')
    
    response = api_client.get(reverse('post-list'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

@pytest.mark.django_db
def test_retrieve_post(api_client, create_post):
    response = api_client.get(reverse('post-detail', args=[create_post.id]))
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == create_post.title
    assert response.data['content'] == create_post.content

@pytest.mark.django_db
def test_create_post(api_client):
    data = {
        'title': 'New Post',
        'content': 'New Content'
    }
    response = api_client.post(reverse('post-list'), data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Post.objects.count() == 1
    assert Post.objects.get().title == 'New Post'

@pytest.mark.django_db
def test_update_post(api_client, create_post):
    data = {
        'title': 'Updated Title',
        'content': 'Updated Content'
    }
    response = api_client.put(reverse('post-detail', args=[create_post.id]), data)
    assert response.status_code == status.HTTP_200_OK
    create_post.refresh_from_db()
    assert create_post.title == 'Updated Title'
    assert create_post.content == 'Updated Content'

@pytest.mark.django_db
def test_delete_post(api_client, create_post):
    response = api_client.delete(reverse('post-detail', args=[create_post.id]))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Post.objects.count() == 0

