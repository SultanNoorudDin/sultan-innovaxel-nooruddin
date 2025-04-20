from django.urls import path
from . import views

# url endpoints
urlpatterns = [
    path('shorten/', views.CreateShortURL.as_view(), name='create'),
    path('shorten/<str:shortCode>/', views.RetrieveShortURL.as_view(), name='retrieve'),
    path('shorten/<str:shortCode>/update/', views.UpdateShortURL.as_view(), name='update'),
    path('shorten/<str:shortCode>/delete/', views.DeleteShortURL.as_view(), name='delete'),
    path('shorten/<str:shortCode>/stats/', views.GetStatsView.as_view(), name='stats'),
]
