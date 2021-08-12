from users.views import login
from django.urls import path, include
urlpatterns = [
    path('login/', login),
]
