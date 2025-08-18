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
    lookup_field = 'title'