import requests
from bs4 import BeautifulSoup

def genie():

    inssa = list()
    url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N'

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        rank = 1
        for tr in soup.select("tbody > tr.list > td.info"):
            title = tr.select_one("a.title.ellipsis").text
            artist = tr.select_one("a.artist.ellipsis").text
            inssa.append((title.strip(), artist.strip()))
            rank += 1
    else:
            print(f"HTTP 요청 실패 코드: {response.status_code}")
        
    return inssa