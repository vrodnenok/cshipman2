from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class VoyagesTest(LiveServerTestCase):
    fixtures=['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_voyage_via_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        """
        testing my first try
        """
        self.browser.get(self.live_server_url + '/admin/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)
        # She types in her username and passwords and hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('root')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('8102977aa')
        password_field.send_keys(Keys.RETURN)

        # her username and password are accepted, and she is taken to
        # the Site Administration page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        # She now sees a couple of hyperlink that says "Polls"
        voyages_links = self.browser.find_elements_by_link_text('Voyages')
        self.assertEquals(len(voyages_links), 1)

        # TODO: Gertrude uses the admin site to create a new Poll
        # self.fail('todo: finish tests')

        self.browser.get(self.live_server_url)
        body = self.browser.find_element_by_id("container")
        self.assertIn('Content of this page is here', body.text)
        home_btn = self.browser.find_element_by_id("home_btn")
        self.assertIn('Home', home_btn.text)
        manage_voyages_btn = self.browser.find_element_by_id('manage_voyages_btn')
        self.assertIn('Manage voyages', manage_voyages_btn.text)
        blog_btn = self.browser.find_element_by_id('blog_btn')
        self.assertIn('Blog', blog_btn.text)
        blog_btn.click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Blogfd', body.text)
