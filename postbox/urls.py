from django.urls import path
from . import views
import datasetting

urlpatterns = [
    path('', views.home, name='home'),
    path('postbox/', views.postbox, name='postbox'),
    path('MyReview/', views.MyReview, name='MyReview'),
    path('MyReview/delete/<int:id>', views.delete_review, name='delete-review'),
    path('MovieReview/<int:id>', views.MovieReview, name='MovieReview'),
    path('ReviewList/<int:review_id>/', views.crawlreview),
    path('MovieReview/steam/<int:id>', views.movie_favorite, name='picklist'),
    path('postbox/<int:preview_id>/', views.detail),
    path('data/', datasetting.inputData, name='data'),
]