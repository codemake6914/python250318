#DemoForm.py
#DemoForm.ui + DemoForm.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹크롤링
from bs4 import BeautifulSoup
#웹서버에 요청청
import urllib.request
#특정 문자열을 검색
import re 

#디자인 파일을 로딩: 파일명 수정
form_class = uic.loadUiType("DemoForm2.ui")[0]

#윈도우 클래스 정의: 상속받는 클래스명 변경
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드 추가
    def firstClick(self):
        #User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
        hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

        #파일에 쓰기
        f = open('c:\\work\\clien.txt', 'w', encoding='utf-8')

        #페이징하는 URL주소를 조립립
        for n in range(0,11):
                #클리앙의 중고장터 주소 
                data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest?page=' + str(n)
                #웹브라우져 헤더 추가 
                req = urllib.request.Request(data, \
                                            headers = hdr)
                data = urllib.request.urlopen(req).read()
                page = data.decode('utf-8', 'ignore')
                soup = BeautifulSoup(page, 'html.parser')
                list = soup.findAll('td', attrs={'class':'subject'})
        # <td class="subject">
        # <a href="/board/view.php?table=bestofbest&amp;no=479073&amp;s_no=479073&amp;page=1" target="_top">
        # 라떼 러닝크루</a><span class="list_memo_count_span"> [22]</span>  
        # <span style="margin-left:4px;">
        # <img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> </td>


        # <span class="category fixed" title="판매">판매</span>
        # <span class="subject_fixed" data-role="list-title-text" title="플레이스테이션5 (PS5) 슬림 디지털 에디션 팝니다. (택포 40만원)">
        # 플레이스테이션5 (PS5) 슬림 디지털 에디션 팝니다. (택포 40만원)
        # </span>



                for item in list:
                        try:
                                title = item.find('a').text.strip()
                                # print(title)
                                #<a class='list_subject'><span>text</span><span>text</span>
                                # span = item.contents[1]
                                # span2 = span.nextSibling.nextSibling
                                # title = span2.text 
                                if (re.search('전남', title)):
                                        print(title.strip())
                                        # print('https://www.clien.net'  + item['href'])
                                        f.write(title.strip() + '\n')
                        except:
                                pass
                
        #파일닫기
        f.close()

        self.label.setText("중고장터 검색 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번쩨 버튼을 클릭")
#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()
    