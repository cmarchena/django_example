from django.test import TestCase, Client
from .models import Post
import json
class PostModelTestCase(TestCase):
    def test_post_creation(self):
        post = Post(title="Title", content="content")
        post.save()
        self.assertEqual(post.title, "Title")
    def test_post_read_by_id(self):
        post = Post(title="Title", content="content")
        post.save()
        read_post = Post.objects.get(id=post.id)
        self.assertEqual(post.title, read_post.title)
    def test_read_all(self):
        post = Post(title="Title", content="content")
        post.save()
        read_post = Post.objects.all()
        self.assertEqual(post.title, read_post[0].title)
    def test_update(self):
        post = Post(title="Title", content="content")
        post.save()
        post.title = "New Title"
        post.content = "New Content"
        post.save()
        updated_post = Post.objects.get(id=post.id)
        self.assertEqual(updated_post.title, "New Title")
        self.assertEqual(updated_post.content, "New Content")
    def test_delete(self):
        post = Post(title="Title", content="content")
        post.save()
        post.delete()
        deleted_post = Post.objects.filter(id=post.id)
        self.assertEqual(len(deleted_post), 0)

class PostEndpointTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list_endpoint(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_create_endpoint(self):
        data = {'title': 'Test Post', 'content': 'This is a test post', 'status': 'published'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, 201)

    def test_post_detail_endpoint(self):
        post = Post.objects.create(title='Test Post', content='This is a test post', status='published')
        response = self.client.get(f'/api/posts/{post.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_post_update_endpoint(self):
        post = Post.objects.create(title='Test Post', content='This is a test post', status='published')
        data = {'title': 'Updated Post', 'content': 'This is an updated post'}
        response = self.client.put(f'/api/posts/{post.pk}/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_delete_endpoint(self):
        post = Post.objects.create(title='Test Post', content='This is a test post', status='published')
        response = self.client.delete(f'/api/posts/{post.pk}/')
        self.assertEqual(response.status_code, 204)