from django.test import TestCase, Client
from django.urls import reverse

from .models import Tree

# Create your tests here.
class TreeTests(TestCase):

    def setUp(self):
        self.tree = Tree.objects.create(
        title='Harry Potter',
        farmer='JK Rowling',
        price='25.00',
        )

    def test_tree_listing(self):
        self.assertEqual(f'{self.tree.title}', 'Harry Potter')
        self.assertEqual(f'{self.tree.farmer}', 'JK Rowling')
        self.assertEqual(f'{self.tree.price}', '25.00')


    def test_tree_list_view(self):
        response = self.client.get(reverse('tree_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'trees/tree_list.html')

    def test_tree_detail_view(self):
        response = self.client.get(self.tree.get_absolute_url())
        no_response = self.client.get('/trees/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'trees/tree_detail.html')