import requests
from bs4 import BeautifulSoup

def get_dmv():

    inssa = list()

    url = "https://movie.daum.net/ranking/reservation"

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    response = requests.get(url, headers=headers)


    if response.status_code == 200:
   
        soup = BeautifulSoup(response.text, "html.parser")
      
        rank = 0
        movie_list = soup.select(".thumb_cont")
        for tr in movie_list:
            rank = rank + 1
            a_tag = tr.select_one("a")
            print(f'{rank}위 {a_tag.text}')
            txt_grade = tr.select_one("span.txt_grade")
            print(f'평점: {txt_grade.text}')
            txt_num = tr.select_one("span.txt_num")
            print(f'예매율: {txt_num.text}')
            txt_date = tr.select_one(".txt_info > span.txt_num")
            print(f'개봉날짜:4 {txt_date.text}')
    else:
        print("HTTP 요청 실패")
    
    return inssa