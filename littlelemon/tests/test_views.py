from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import menuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(Title='Pizza', Price=1.3, Inventory=1)
        self.menu2 = Menu.objects.create(Title='cake', Price=1.5, Inventory=2)

    def test_getall(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = menuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
