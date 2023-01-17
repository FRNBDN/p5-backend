from django.urls import path
from lists import views

urlpatterns = [
    path('lists/', views.ListList.as_view())
]