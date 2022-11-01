from django.urls import path
from . import views


urlpatterns = [
    path('recommend/', views.recommend_movie, name='recommend_movie'),
    path('recommed/<int:id>', views.reviews, name='reviews'),
]