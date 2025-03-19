#DemoSQL.py
#SQLite3를 사용하는 데모
import sqlite3

#연결객체를 생성
con = sqlite3.connect(':memory:')
#커서 객체를 생성
cur = con.cursor()
#테이블을 생성
cur.execute('CREATE TABLE PhoneBook(Name text, PhoneNum text);')
#1건 데이터를 입력
cur.execute("INSERT INTO PhoneBook VALUES('Derick', '010-1234-5678');")
#입력 파라미터 처리
name = '홍길동'
phoneNumber = '010-1234-5678'
cur.execute("INSERT INTO PhoneBook VALUES(?, ?);", (name, phoneNumber))

#다중 데이터를 입력
#여러건 입력: 2차원 데이터 - 2행2열
datalist = (('이순신', '010-1234-5678'), ('전우치', '010-1234-5678'))
cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", datalist)

#데이터를 조회
cur.execute("SELECT * FROM PhoneBook;")
#선택한 블럭을 주석 처리: Ctrl + /
# for row in cur:
#     print(row) 
#한 건 조회
print("--한건 출력--")
print(cur.fetchone())
#다중조회
print("--2건 출력--")
print(cur.fetchmany(2))
#모두 조회
print("--모두 출력--")
cur.execute("SELECT * FROM PhoneBook;")
print(cur.fetchall())