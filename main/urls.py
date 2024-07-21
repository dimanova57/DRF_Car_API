from django.urls import path
from .views import GetAllCarsView

urlpatterns = [
    path('cars/<str:car_model>/', GetAllCarsView.as_view(), name='car-detail'),
    path('cars/', GetAllCarsView.as_view(), name='car-list'),
]