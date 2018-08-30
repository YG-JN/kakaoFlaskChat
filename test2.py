import requests
import random
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, 'html.parser')

title_tag = doc.select('dt.tit > a')
star_tag = doc.select('div.star_t1 > a > span.num')
reserve_tag = doc.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dd.star > dl.info_exp > dd > div > span.num')
img_tag = doc.select('div.thum > a > img')

movie_dic = {}
for i in range(0,10):
    movie_dic[i] = {
        "title" : title_tag[i].text,
        "star" : star_tag[i].text,
        "reserve" : reserve_tag[i].text,
        "img" : img_tag[i].get('src')
    }
    
pick_movie = movie_dic[random.randrange(0,10)]
    
print(pick_movie)
    
    
    
    # print(title_tag[i].text)
    # print(star_tag[i].text)
    # print(reserve_tag[i].text)
    
# list_movies = []
# list_stars = []
# list_reserve = []
# for i in return_doc :
#     list_movies.append(i.text)

# for i in return_doc2 :
#     list_stars.append(i.text)

# for i in return_doc3 :
#     list_reserve.append(i.text)
    
# print(list_movies)
# print(list_stars)
# print(list_reserve)