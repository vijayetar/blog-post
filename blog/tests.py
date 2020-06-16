from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class BlogTests(TestCase):

  def test_url_testing_200_status(self):
    url = reverse('home')
    response = self.client.get(url)
    actual = response.status_code
    expected = 200
    self.assertEqual(actual, expected)


