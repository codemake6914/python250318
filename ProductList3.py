import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic

# 데이터베이스 관리 클래스
class DatabaseManager:
    def __init__(self, db_name="ProductList.db"):
        self.db_name = db_name
        self.connect_db()
        self.create_table()

    # 데이터베이스 연결 함수
    def connect_db(self):
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()

    # 제품 정보를 저장할 테이블 생성 함수
    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Price INTEGER
            );
        """)
        self.con.commit()

    # 모든 제품 정보를 가져오는 함수
    def get_all_products(self):
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

    # 새로운 제품 정보를 추가하는 함수
    def add_product(self, name, price):
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    # 데이터베이스 연결을 종료하는 함수
    def close_connection(self):
        self.con.close()

# UI 클래스
class ProductManagerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()  # 데이터베이스 객체 생성
        self.setup_ui()  # UI 설정 함수 호출

    # UI 설정 함수
    def setup_ui(self):
        self.ui = uic.loadUi("ProductList3.ui", self)
        
        # QTableWidget 설정 (컬럼 크기 및 헤더 설정)
        self.tableWidget.setColumnWidth(0, 100)  # 제품ID 열 너비
        self.tableWidget.setColumnWidth(1, 200)  # 제품명 열 너비
        self.tableWidget.setColumnWidth(2, 100)  # 가격 열 너비
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])  # 테이블 헤더 설정
        self.tableWidget.setTabKeyNavigation(False)  # Tab 키 네비게이션 비활성화
        self.tableWidget.doubleClicked.connect(self.double_click)  # 더블 클릭 이벤트 연결
        
        # 버튼 클릭 시 제품 추가 함수 연결
        self.addButton.clicked.connect(self.addProduct)
        
        # 초기 데이터 로딩
        self.get_products()

    # 데이터베이스에서 제품 정보를 가져와 테이블에 표시하는 함수
    def get_products(self):
        self.tableWidget.clearContents()  # 기존 데이터 초기화
        products = self.db.get_all_products()  # 데이터베이스에서 모든 제품 정보 가져오기
        self.tableWidget.setRowCount(len(products))  # 행 개수 설정
        
        # 제품 정보를 테이블에 추가
        for row, item in enumerate(products):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))  # 제품 ID
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))  # 제품명
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item[2])))  # 가격

    # 테이블에서 행을 더블 클릭하면 해당 데이터를 입력 필드에 표시하는 함수
    def double_click(self):
        row = self.tableWidget.currentRow()  # 현재 선택된 행 가져오기
        self.prodID.setText(self.tableWidget.item(row, 0).text())  # 제품 ID 설정
        self.prodName.setText(self.tableWidget.item(row, 1).text())  # 제품명 설정
        self.prodPrice.setText(self.tableWidget.item(row, 2).text())  # 가격 설정

    # 제품 추가 함수
    def addProduct(self):
        name = self.prodName.text().strip()  # 입력된 제품명
        price = self.prodPrice.text().strip()  # 입력된 가격

        # 입력값이 비어 있는 경우 경고 메시지 출력
        if not name:
            QMessageBox.warning(self, "입력 오류", "제품명을 입력하세요.")
            return
        
        # 가격이 숫자가 아닌 경우 경고 메시지 출력
        if not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "가격은 숫자로 입력하세요.")
            return
        
        # 데이터베이스에 제품 추가
        self.db.add_product(name, int(price))
        self.get_products()  # 테이블 갱신
        QMessageBox.information(self, "완료", "제품이 추가되었습니다.")

# 실행 부분
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductManagerGUI()
    window.show()
    sys.exit(app.exec_())