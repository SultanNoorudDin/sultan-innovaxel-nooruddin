from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.CreateShortURL.as_view(), name='create'),
    path('shorten/<str:shortCode>/', views.RetrieveShortURL.as_view(), name='retrieve'),
    path('shorten/<str:shortCode>/update/', views.UpdateShortURL.as_view(), name='update'),
]
