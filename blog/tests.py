from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post


class BlogPostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="user1", )
        cls.post1 = Post.objects.create(
            title="post1",
            text="this is test object from Post",
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
            email='post1@gmail.com'
        )
        cls.post2 = Post.objects.create(
            title="post2",
            text="python is the beast lang",
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user,
            email='post2@gmail.com'
        )

    def test_check_model_str(self):
        self.assertEqual(str(self.post1), self.post1.title)

    def test_post_ditail(self):
        self.assertEqual(self.post1.title, 'post1')
        self.assertEqual(self.post1.text, 'this is test object from Post')
        self.assertEqual(self.post1.status, self.post1.STATUS_CHOICES[0][0])
        self.assertEqual(self.post1.author, self.user)
        self.assertEqual(self.post1.email, 'post1@gmail.com')

        self.assertEqual(self.post2.title, 'post2')
        self.assertEqual(self.post2.text, "python is the beast lang", )
        self.assertEqual(self.post2.status, self.post1.STATUS_CHOICES[1][0])
        self.assertEqual(self.post2.author, self.user)
        self.assertEqual(self.post2.email, 'post2@gmail.com')

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.author)

    def test_post_drf_not_in_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertNotContains(response, self.post2.title)
        self.assertNotContains(response, self.post2.text)

    def test_post_detail_on_blog_detail_post(self):
        response = self.client.get('/blog/1/')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_delete_post(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)

    def test_update_url(self):
        response = self.client.get('/blog/1/update/')
        self.assertEqual(response.status_code, 200)

    def test_update_url_by_name(self):
        response = self.client.get(reverse('post_update', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_url(self):
        response = self.client.get('/blog/1/delete/')
        self.assertEqual(response.status_code, 200)

    def test_delete_url_by_name(self):
        response = self.client.get(reverse('post_delete', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_create_new_post_url(self):
        response = self.client.get('/blog/1/delete/')
        self.assertEqual(response.status_code, 200)

    def test_create_new_post_url_by_name(self):
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_new_post(self):
        response = self.client.post('/blog/add/', {
            'title': "post3",
            'text': "django is the beast framework",
            'status': 'pub',
            'author': self.user.id,
            'email': 'post3@gmail.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "post3")
        self.assertEqual(Post.objects.last().text, "django is the beast framework")
        self.assertEqual(Post.objects.last().email, 'post3@gmail.com')

    def test_update_post_one(self):
        response = self.client.post(reverse('post_update', args=[self.post1.id]), {
            'title': "Post1 Updated",
            'text': 'I user test for project',
            'status': Post.STATUS_CHOICES[0][0],
            'author': self.user.id,
            'email': 'post1@gmail.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.get(pk=self.post1.id).title, "Post1 Updated")
        self.assertEqual(Post.objects.get(pk=self.post1.id).text, 'I user test for project')
        self.assertEqual(Post.objects.get(pk=self.post1.id).email, 'post1@gmail.com')

    def test_delete_post_by_url_name(self):
        response = self.client.post(reverse('post_delete', args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertNotContains(response, self.post1.title)
        self.assertNotContains(response, self.post1.text)
        self.assertNotContains(response, self.post1.author)

