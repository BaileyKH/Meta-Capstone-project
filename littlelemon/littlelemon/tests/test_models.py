from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Lasagna", price=24, inventory=36)
        self.assertEqual(item, "Lasagna : 24")