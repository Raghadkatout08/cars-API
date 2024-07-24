# from django.shortcuts import render
# from django.views.generic import TemplateView

from rest_framework import generics 
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car 
from .serializer import CarSerializers
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars_object'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['buyer_id', 'model', 'brand', 'price', 'is_bought', 'buy_time']

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = '__all__'

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('car_list')

class CarCreateListView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class CarDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers