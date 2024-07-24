from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Car(models.Model):
    buyer_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    model = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    price = models.IntegerField()
    is_bought = models.BooleanField()
    buy_time = models.DateField(default=timezone.now)

    def __str__(self):
        return self.brand
    
    def get_absolute_url(self):
        return reverse("car_detail", args={self.id})