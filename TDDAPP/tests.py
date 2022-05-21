from django.test import TestCase
from django.urls import resolve
from TDDAPP.views import index


class AppUnitTest(TestCase):

    def test_resolve_to_index(self):
        found = resolve('/')
        print(found)
        self.assertEqual(found.func, index)
