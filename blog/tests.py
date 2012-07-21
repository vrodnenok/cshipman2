
from django.test import TestCase, LiveServerTestCase
from blog.models import Post
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BlogModelTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_creating_a_new_post(self):
        """
        Testing the Posts creation in Blog application
        """
        post=Post()
        post.body='Test post'
        post.created=timezone.now()

        # now i'm gonna check if i can save this post
        post.save()

        # check if post is in database
        all_posts_in_database=Post.objects.all()
        self.assertEquals(len(all_posts_in_database), 1)
        only_post_in_database=all_posts_in_database[0]
        self.assertEquals(only_post_in_database, post)

        #check the data in post
        self.assertEquals(only_post_in_database.body, 'Test post')
        self.assertEquals(only_post_in_database.created.date(), post.created.date())

        self.browser.get(self.live_server_url + '/blog/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Blog', body.text)