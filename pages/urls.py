from django.urls import path 
from .views import homePageView


urlpatterns = [
    path("helo", homePageView, name='home')
]
