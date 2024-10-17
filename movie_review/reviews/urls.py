from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_view, name='review_form'),
    path('success/', views.review_success, name='review_success'),
]