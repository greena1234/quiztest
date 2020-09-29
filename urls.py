from . import views
from django.urls import path

urlpatterns = [
    path('questions/', views.QuestionView.as_view(), name='question'),
]
