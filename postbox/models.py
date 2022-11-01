from django.db import models
from user.models import UserModel
from django.conf import settings

# =================================================================================================== #

# 영화모델추가
class movieModel(models.Model):
    class Meta:
        db_table = 'movies'

    movieId = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    Poster = models.CharField(max_length=200)
# =================================================================================================== #



# =================================================================================================== #

# 유저의 포스트한 리뷰 모델
class Review(models.Model):
    class Meta:
        db_table = 'reviews'

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # 리뷰작성자

    title = models.CharField(max_length=100)  # 영화 이름
    review = models.CharField(max_length=1000)  # 리뷰내용
    score = models.IntegerField()  # 평점

    genre = models.ForeignKey('movieModel', on_delete=models.SET_NULL, null=True, related_name='review_genre')
    Poster = models.CharField(max_length=200, default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# =================================================================================================== #

#크롤링 db 저장
class MovieData(models.Model):
    class Meta:
        db_table = 'recentMovies'
    title = models.CharField(max_length=200)
    link = models.URLField()
    image = models.URLField()

    def __str__(self):
        return self.title


# 찜 영화
class favorite(models.Model):
    class Meta:
        db_table = 'favorite'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(movieModel, on_delete=models.CASCADE, db_column='movieId')
    boxoffice = models.ForeignKey(MovieData, on_delete=models.CASCADE, null=True)




# =================================================================================================== #



#크롤링 리스트 db 저장

class crawlReview(models.Model):
    class Meta:
        db_table = 'crawl_reviews'

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # 리뷰작성자

    title = models.CharField(max_length=100, null = True, default='')  # 영화 이름
    review = models.CharField(max_length=500, null = True)  # 리뷰내용
    score = models.IntegerField()  # 평점

    created_at = models.DateTimeField(auto_now_add=True)  # 리뷰작성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 리뷰 업데이트

    def __str__(self):
        return self.title