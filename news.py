import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001"
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for title in soup.select(".type06_headline a"):
            print(title.get_text(strip=True))
    else:
        print(f"HTTP 요청 실패 코드: {response.status_code}")
