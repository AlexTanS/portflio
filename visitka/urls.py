from django.urls import path, include
from .views import visitka

app_name = "visitka"

urlpatterns = [    
    path("", visitka, name="visitka"),  # home page 'visitka'
]
