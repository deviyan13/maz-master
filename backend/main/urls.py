from django.urls import path
from main.views import CarsListView, CarDetailView, CarPostitionView
from main import views

urlpatterns = [
    path('cars/', CarsListView.as_view()),
    path('car/', CarDetailView.as_view()),
    path('car/simplified/', CarPostitionView.as_view()),
]
