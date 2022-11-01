from django.http import HttpResponse
import csv
import pandas as pd
from postbox.models import movieModel


def inputData(requests):
    with open('moviesmovies.csv', 'r', encoding='utf-8') as f: # moviesmovies 파일 경로지정해주세요
        dr = csv.DictReader(f)
        df = pd.DataFrame(dr)
    dataSet = []

    for i in range(len(df)):
        tmp = (df['movieId'][i], df['title'][i], df['genre'][i], df['Poster'][i])
        dataSet.append(tmp)

    for i in range(len(dataSet)):
        movieModel.objects.create(movieId=dataSet[i][0], title=dataSet[i][1], genre=dataSet[i][2], Poster=dataSet[i][3])

    return HttpResponse('성공')