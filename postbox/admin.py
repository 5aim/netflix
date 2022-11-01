from django.contrib import admin
from .models import Review, movieModel, favorite, MovieData, crawlReview

admin.site.register(Review)
admin.site.register(movieModel)
admin.site.register(favorite)
admin.site.register(MovieData)
admin.site.register(crawlReview)