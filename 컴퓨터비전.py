import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import openai
from PIL import Image
import base64
from io import BytesIO
import requests

# OpenAI API 키 설정
# 나중에 본인 키로 수정하여 사용용
openai.api_key = ''

# 이 이미지에는 전통적인 동양 수묵화 스타일의 풍경이 그려져 있습니다. 

# - 강이나 호수 같은 물이 흐르고 있으며, 물 위에는 작은 배가 떠 있습니다.
# - 나무들이 물가와 언덕에 심어져 있어 자연스럽고 평화로운 느낌을 줍니다.
# - 오른쪽에는 집이나 건물이 언덕 위에 위치하고 있으며, 주변에는 숲과 산이 있습니다.
# - 전반적으로 자연 풍경이 조화롭게 그려져 있으며, 고유한 회화적 분위기를 자아냅니다.
class ImageDescriptionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('컴퓨터비전으로 이미지 분석하는 앱')

        self.layout = QVBoxLayout()

        self.image_label = QLabel('이미지 분석에 필요한 사진을 업로드하세요.')
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.upload_button = QPushButton('이미지 업로드')
        self.upload_button.clicked.connect(self.upload_image)
        self.layout.addWidget(self.upload_button)

        self.description_edit = QTextEdit()
        self.layout.addWidget(self.description_edit)

        self.setLayout(self.layout)

    def upload_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.xpm *.jpg)', options=options)
        if file_name:
            self.display_image(file_name)
            self.get_image_description(file_name)

    def display_image(self, file_name):
        pixmap = QPixmap(file_name)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    # Function to encode the image
    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
  
    def get_image_description(self, file_name):
        # Getting the base64 string
        base64_image = self.encode_image(file_name)

        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
        }

        payload = {
        "model": "gpt-4o",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "이 이미지에 무엇이 있는지 한글로 설명해줘?"
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        data = response.json() 
        print(data['choices'][0]['message']['content'])
        self.description_edit.setPlainText(data['choices'][0]['message']['content'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageDescriptionApp()
    ex.show()
    sys.exit(app.exec_())
