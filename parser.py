import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject1.settings")
import django
django.setup()
from postbox.models import MovieData

def parse_movie():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4+%EC%88%9C%EC%9C%84',
        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    # select를 이용해서, 크롤링할 범위
    movies = soup.select(
        '#main_pack > div.sc_new.cs_common_module.case_list.color_1._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div.mflick > div._panel_popular._tab_content > div.list_image_info.type_pure_top > div > ul > li')
    movie_list = []  # 크롤링할 것들을 리스트 형태로

    for movie in movies:  # 크롤링할 것들 반복문 사용
        movie_dic = {}
        image = movie.select_one('a > div > div.thumb > img')['src']
        link = movie.select_one('a')['href']
        title = movie.select_one('a > div > div.title_box > strong').text

        movie_dic['image'] = image
        movie_dic['link'] = "https://search.naver.com/search.naver" + link
        movie_dic['title'] = title

        movie_list.append(movie_dic)
    return movie_list

## 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__=='__main__':
    movie_data_list = parse_movie()
    for movie in movie_data_list:
        MovieData(title=movie['title'], link=movie['link'], image=movie['image']).save()