from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BoockSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

# class BookListApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BoockSerializer

class BookListApiView(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer_data = BoockSerializer(books, many=True).data
        info = {
            'status':'All books have been shown',
            'books list':serializer_data
        }
        return Response(info, status=status.HTTP_200_OK)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BoockSerializer
#     lookup_field = 'id'

class BookDetailApiView(APIView):
    def get(self, request, pk):
        book = Books.objects.get(id=pk)
        serializer_data = BoockSerializer(book).data
        info = {
            'status':'Book taken successfully',
            'book info':serializer_data
        }
        return Response(info)
# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BoockSerializer

# class BookDeleteApiView(APIView):
    # def delete(self, request, pk):
    #     try:
    #         book = Books.objects.get(id=pk)
    #         book.delete()
    #         return Response({'status:''This book deleted succsessfully'})
    #     except:
    #         return Response({'status':'There is no book like that!'})
class BookDeleteApiView(APIView):
    def delete(self, request, pk):
            book = get_object_or_404(Books, pk=pk)
            book.delete()
            return Response({'status':'This book deleted succsessfully'})


# class BookUpdateApiViwe(generics.UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BoockSerializer
class BookUpdateApiViwe(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        serializer = BoockSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            book = Books.objects.get(id=pk)
            serializer = BoockSerializer(book, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"status":"Bad Request"}, status=status.HTTP_400_BAD_REQUEST)


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BoockSerializer

class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BoockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            info = {
                'status':"This book is saved to database",
                'book info':data
            }
            return Response(info)

# class BookMixedApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BoockSerializer

class BookMixedApiView(APIView):
    def get(selfself, request, pk):
           book = get_object_or_404(Books, pk=pk)
           serializer = BoockSerializer(book).data
           info = {
               'status':'Query worked succesfully'
           }
           return Response(info)

    def put(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        serializer = BoockSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"status: Your serializer has got a problem"})


    def patch(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        serializer = BoockSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"status: Your serializer has got a problem"})

    def delete(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        book.delete()
        return Response({"status":"This book deleted succsessfully"})
