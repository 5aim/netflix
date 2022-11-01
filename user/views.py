from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model  # 회원가입 중복확인
from django.contrib import auth  # 로그인 중복확인
from django.contrib.auth.decorators import login_required


# 로그인
def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in', {'error': '아이디와 비밀번호를 확인해주세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            return redirect('/')
        else:
            return render(request, 'signin.html')


# 회원가입
def sign_up_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        genre = request.POST.getlist('genre[]', '')
        introduce = request.POST.get('introduce', '')

        if password != password2:
            return render(request, 'signup.html', {'error': '패스워드를 확인해주세요'})

        else:
            if username == '' or password == '':
                return render(request, 'signup.html', {'error': 'Id와 Pw는 필수입니다'})

            exist_user = get_user_model().objects.filter(username=username)

            if exist_user:
                return render(request, 'signup.html', {'error': '존재하는 Id입니다'})

            else:
                UserModel.objects.create_user(username=username, password=password, introduce=introduce, genre=genre)
                return redirect('/sign-in')

    elif request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            return redirect('/')
        else:
            return render(request, 'signup.html')


# 로그아웃
@login_required
def logout(request):
    auth.logout(request)  # 인증 되어있는 정보를 없애기
    return redirect("/")