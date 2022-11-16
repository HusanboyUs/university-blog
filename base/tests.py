from django.test import TestCase, Client
from .models import Blog
from django.urls import reverse

class TestMyBlog(TestCase):
    def setUp(self):
        self.client=Client()
        self.blog_list=reverse('list-view_api')
        
    def test_blog_list(self):
        response=self.client.get(self.blog_list)
        self.assertEqual(response.status_code, 200)    

    def blog_create_post(self):
        response=self.client.post()



