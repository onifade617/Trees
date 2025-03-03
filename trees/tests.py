from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase, Client
from django.urls import reverse

from .models import Tree,Review

# Create your tests here.
class TreeTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user( # new
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )
        self.special_permission = Permission.objects.get(codename='special_status')


        self.tree = Tree.objects.create(
            title='Harry Potter',
            farmer='JK Rowling',
            price='25.00',
        )

        self.review = Review.objects.create( # new
            tree = self.tree,
            farmer = self.user,
            review = 'An excellent review',
        )

    def test_tree_listing(self):
        self.assertEqual(f'{self.tree.title}', 'Harry Potter')
        self.assertEqual(f'{self.tree.farmer}', 'JK Rowling')
        self.assertEqual(f'{self.tree.price}', '25.00')


    def test_tree_list_view_for_logged_in_user(self): # new
        self.client.login(email='reviewuser@email.com', password='testpass123')
        response = self.client.get(reverse('tree_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'trees/tree_list.html')

    def test_tree_list_view_for_logged_out_user(self): # new
        self.client.logout()
        response = self.client.get(reverse('tree_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/trees/' % (reverse('account_login')))
        response = self.client.get('%s?next=/trees/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

    def test_tree_detail_view_with_permissions(self): # new
        self.client.login(email='reviewuser@email.com', password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.tree.get_absolute_url())
        no_response = self.client.get('/trees/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'trees/tree_detail.html')


    
   