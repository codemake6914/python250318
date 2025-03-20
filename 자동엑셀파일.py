from openpyxl import Workbook
import random

# 제품명 리스트 생성
products = [
    "스마트폰", "노트북", "태블릿", "스마트워치", "무선이어폰", 
    "블루투스스피커", "모니터", "키보드", "마우스", "프린터",
    "공기청정기", "냉장고", "세탁기", "건조기", "TV"
]

# 엑셀 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = "제품 판매 데이터"

# 헤더 추가
ws.append(["제품ID", "제품명", "수량", "가격"])

# 100개의 데이터 생성 및 추가
for i in range(1, 101):
    product_id = f"P{str(i).zfill(3)}"  # P001, P002, ...
    product_name = random.choice(products)
    quantity = random.randint(1, 100)
    
    # 제품별 가격 범위 설정
    if product_name in ["스마트폰", "노트북", "TV"]:
        price = random.randint(500000, 2000000)
    elif product_name in ["태블릿", "모니터", "냉장고", "세탁기", "건조기"]:
        price = random.randint(300000, 1000000)
    else:
        price = random.randint(50000, 300000)
    
    # 데이터 행 추가
    ws.append([product_id, product_name, quantity, price])

# 열 너비 자동 조정
for column in ws.columns:
    max_length = 0
    column = list(column)
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column[0].column_letter].width = adjusted_width

# 파일 저장
wb.save("products.xlsx")
print("엑셀 파일이 생성되었습니다.")