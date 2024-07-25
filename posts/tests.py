from django.test import TestCase
from django.contrib.auth.models import User
from .models import Posts

# Create your tests here.
class PostTests(TestCase):
    @classmethod
    
    def CreateTestData(cls):
        # create user
        testuser1 = User.objects.create_user(username='testuser1', password='user123')
        testuser1.save()

        # create post
        test_post = Posts.objects.create(author=testuser1, title='Blog title', body='Body content...')
        test_post.save()

    def TestBlog(self):
        post = Posts.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, 'testuser1')    
        self.assertEqual(title, 'Blog title')    
        self.assertEqual(body, 'Body content...')    
