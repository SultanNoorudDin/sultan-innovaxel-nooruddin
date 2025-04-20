from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.CreateShortURL.as_view(), name='create'),

]
