#web1.py
#웹크롤링 코드를 작성
from bs4 import BeautifulSoup

#웹페이지 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")

# #<p>태그를 몽땅 검색
# print(soup.find_all("p"))
#<p>한개 검색
# print(soup.find("p"))
#whrjs: <p class="outer-text">
# print(soup.find_all("p", class_="outer-text"))
#attrs속성 => attributes
# print(soup.find_all(attrs={"class":"outer-text"}))

#태그는 삭제하고 내부 컨텐츠만 가져오기: text속성
f = open("sample.txt", "wt", encoding="utf-8")
for tag in soup.find_all("p"):
    title=tag.text.strip()
    title=title.replace("\n", "")
    print(title)
    f.write(title+"\n")

f.close()

