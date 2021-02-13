from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Class to test the HomePageView 
class HomePageTests(SimpleTestCase):
    
    # Function to test that the URL '/' returns the webpage 
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    # Function to test that we can return the webpage using the view name not URL 
    def test_view_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    # Function to test that the view uses the correct template 
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

# Class to test the SignUpView 
class SignupPageTests(TestCase):
    # variables for test user 
    username = 'newuser'
    email = 'newuser@gmail.com'
   
    # Function to test that the URL '/accounts/signup/' returns the webpage
    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
    
    # Function to test that we can return the webpage using the view name not URL 
    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    # Function to test that we use the correct Template 
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    # Function to test that the SignUpView add User model to database correctly
    def test_signup_form(self):
        # Create new Test user 
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        # Check that the test user was added to model objects
        self.assertEqual(get_user_model().objects.all().count(), 1)
        # Check that the model's username is correct
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        # Check that the model's email is correct
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)

# Create your tests here.
