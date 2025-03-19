import os
import shutil

# 경로 설정
downloads_folder = r"C:\Users\user\Downloads"
images_folder = r"C:\Users\user\images"
data_folder = r"C:\Users\user\data"
docs_folder = r"C:\Users\user\docs"
archive_folder = r"C:\Users\user\archive"

# 각 폴더가 없다면 생성
for folder in [images_folder, data_folder, docs_folder, archive_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 다운로드 폴더에서 모든 파일 가져오기
for file_name in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, file_name)

    if os.path.isfile(file_path):  # 파일인지 확인
        # 확장자에 따라 이동
        if file_name.lower().endswith(('.jpg', '.jpeg')):
            destination = images_folder
        elif file_name.lower().endswith(('.csv', '.xlsx')):
            destination = data_folder
        elif file_name.lower().endswith(('.txt', '.doc', '.pdf')):
            destination = docs_folder
        elif file_name.lower().endswith('.zip'):
            destination = archive_folder
        else:
            continue  # 해당하지 않으면 이동하지 않음

        # 파일 이동
        shutil.move(file_path, os.path.join(destination, file_name))
        print(f"{file_name}이(가) {destination} 폴더로 이동되었습니다.")
