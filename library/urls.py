from django.urls import path
from .views import BookListApiView, BookDetailApiView


urlpatterns = [
    path('kitoblar/', BookListApiView.as_view()),  
    path('kitob/<str:title>/', BookDetailApiView.as_view()),
]
