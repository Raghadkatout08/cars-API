import datetime
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Car

class CarsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@gmail.com',
            password='1234'
        )

        cls.car = Car.objects.create(
            buyer_id=cls.user,
            model='Corolla',
            brand='Toyota',
            price=23999,
            is_bought=True,
            buy_time=datetime.date(2024, 9, 21)
        )

    def test_list_page_status_code(self):
        url = reverse('car_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('car_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'car_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_str_method(self):
        self.assertEqual(str(self.car), 'Toyota')

    def test_details_view(self):
        url = reverse('car_detail', args=[self.car.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'car_detail.html')

    def test_create_view(self):
        data = {
            'buyer_id': self.user.id,
            'model': 'Camry',
            'brand': 'Toyota',
            'price': 24999,
            'is_bought': False,
            'buy_time': '2024-07-01',
        }

        url = reverse('car_create')
        response = self.client.post(url, data, follow=True)
        self.assertEqual(Car.objects.count(), 2)
        new_car = Car.objects.last()
        self.assertRedirects(response, reverse('car_detail', args=[new_car.id]))

    def test_update_view(self):
        data = {
            'buyer_id': self.user.id,
            'model': 'Camry Updated',
            'brand': 'Toyota Updated',
            'price': 25999,
            'is_bought': True,
            'buy_time': '2024-08-01',
        }
        
        url = reverse('car_update', args=[self.car.id])
        response = self.client.post(url, data, follow=True)
        self.assertRedirects(response, reverse('car_detail', args=[self.car.id]))
        self.car.refresh_from_db()
        self.assertEqual(self.car.model, 'Camry Updated')

    def test_delete_view(self):
        url = reverse('car_delete', args=[self.car.id])
        response = self.client.post(url, follow=True)
        self.assertRedirects(response, reverse('car_list'))
        self.assertEqual(Car.objects.count(), 0)

    def test_field_max_length(self):
        car = Car.objects.get(id=self.car.id)
        max_length = car._meta.get_field('model').max_length
        self.assertEqual(max_length, 250)

    def test_field_types(self):
        car = Car.objects.get(id=self.car.id)
        self.assertIsInstance(car.price, int)
        self.assertIsInstance(car.is_bought, bool)
        self.assertIsInstance(car.buy_time, datetime.date)
