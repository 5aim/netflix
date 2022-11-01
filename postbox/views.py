from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, favorite, movieModel, MovieData, crawlReview


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/postbox')
    else:
        return redirect('/sign-in')


# 메인화면(홈)
def postbox(request):
    user = request.user.is_authenticated
    if user:
        movie_list = MovieData.objects.all()
        class_object = movieModel.objects.order_by('?')
        favorite_movie = favorite.objects.filter(author=request.user)
        print(class_object)

        return render(request, 'index.html',
                    {'movie_list': movie_list, 'class_object': class_object, 'favorite_movie': favorite_movie})
    else:
        return redirect('/sign-in')


# 유저 포스팅 리뷰
def MyReview(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            all_review = Review.objects.filter(author=request.user).order_by('-created_at')
            favorite_movie = favorite.objects.filter(author=request.user)
            return render(request, 'userpage.html', {'reviews': all_review,'favorite_movie': favorite_movie})
        else:
            return redirect('/sign-in')

    elif request.method == 'POST':
        user = request.user

        review = Review()
        review.author = user

        review.title = request.POST.get('movie-name', '')
        review.review = request.POST.get('my-review', '')
        review.score = request.POST.get('my-score')

        review.save()
        return redirect('/MyReview')


# 유저 포스팅 리뷰 삭제
@login_required()
def delete_review(request, id):
    print('1234')
    my_review = Review.objects.get(id=id)
    my_review.delete()
    return redirect('/MyReview')


# 자세한 무비 리뷰
@login_required
def MovieReview(request, id):
    if request.method == 'GET':
        user = request.user.is_authenticated
        movie = movieModel.objects.get(movieId = id)

        if user:
            return render(request, 'review.html', {'user':user, 'movie':movie})



@login_required
def movie_favorite(request, id):
    user = request.user
    movie = movieModel.objects.get(movieId = id)
    is_favorite = favorite.objects.filter(author=user, movie=movie)

    if is_favorite:
        favorite.delete()
    else:
        favorite.objects.create(author=user, movie=movie)
    return redirect('/postbox')


# 현재상영작 특정링크
@login_required
def detail(request, preview_id):
    user = request.user.is_authenticated
    if user:
        movie_list = MovieData.objects.get(id=preview_id)
        review_list = crawlReview.objects.filter(title=movie_list.title)
        context = {'movie_list':movie_list, 'review_list': review_list}
        print('1234')
        return render(request, 'review2.html', context)
    else:
        redirect('/postbox')


# 현재상영작에서 리뷰작성
@login_required
def crawlreview(request, review_id):
    if request.method == 'POST':
        user = request.user

        review = crawlReview()
        review.author = user

        review.title = MovieData.objects.get(id=review_id).title
        review.review = request.POST.get('Movie-Review', '')
        review.score = request.POST.get('my-score')

        review.save()
        return redirect(request.META['HTTP_REFERER'])