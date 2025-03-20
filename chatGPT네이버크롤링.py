import requests
from bs4 import BeautifulSoup
import pandas as pd

# 크롤링할 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# HTTP 요청
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)

# 응답 확인
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 기사 제목 크롤링 (예제: 뉴스 제목이 있는 태그 찾기)
    titles = soup.select(".news_tit")  # 네이버 검색 결과에서 뉴스 제목을 포함하는 클래스명
    
    data = []
    for idx, title in enumerate(titles, 1):
        text = title.get_text()
        print(f"{idx}. {text}")
        data.append([idx, text])
    
    # 엑셀 파일로 저장
    df = pd.DataFrame(data, columns=["번호", "기사 제목"])
    df.to_excel("result.xlsx", index=False)
    print("\n결과가 result.xlsx 파일로 저장되었습니다.")
else:
    print("페이지를 가져오는 데 실패했습니다.")
