from django.contrib import admin
from django.urls import path
from app_gen import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('personapi/', views.LCPersonAPI.as_view()),
    path('personapi/<int:pk>/', views.RUDPersonAPI.as_view()),
    
]
