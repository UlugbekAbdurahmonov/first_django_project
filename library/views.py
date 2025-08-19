from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BoockSerializer

# Create your views here.

class BookListApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BoockSerializer

class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BoockSerializer
    lookup_field = 'id'

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BoockSerializer

class BookUpdateApiViwe(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BoockSerializer

class BookCreateApiView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BoockSerializer

class BookMixedApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BoockSerializer