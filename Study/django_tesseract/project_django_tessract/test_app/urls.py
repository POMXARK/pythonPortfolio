from django.urls import path
from .views import *

app_name = 'test_app'
urlpatterns = [
    path('', HomeView.as_view()),
    path('process_image/', process_image, name='process_image') # New line
]
