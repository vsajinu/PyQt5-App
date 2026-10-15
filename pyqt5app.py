'''
10/12/2026
pip install PyQt5
'''
import os
import sys

from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                             QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QSizePolicy, QStackedWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #window settings
        self.setWindowTitle("Jimmy's Introduction!")
        self.setGeometry(800, 450, 1000, 650)
        
        app_icon = os.path.join(os.path.dirname(__file__), "pyqt5introapplogo.jpg")
        self.setWindowIcon(QIcon(app_icon))

        self.setStyleSheet("QMainWindow { background-color: #D3D3D3; }")

        #title
        title = QLabel("First Year Comp Sci Major at UF")
        title.setFont(QFont("Times New Roman", 30))
        title.setStyleSheet("color: #000000;")
        title.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        #pic
        image = QLabel()
        image.setFixedSize(400, 400)
        holder = os.path.join(os.path.dirname(__file__), "pyqt5introimage.png")
        pixmap = QPixmap(holder)
        image.setPixmap(pixmap)
        image.setScaledContents(True)

        self.initUI(title, image)

    def initUI(self, title, image):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        centralWidget = QWidget()

        layout = QVBoxLayout()
        centralWidget.setLayout(layout)

        layout.addWidget(title)
        layout.addWidget(image, alignment=Qt.AlignCenter)

        h_layout = QHBoxLayout()

        #buttons 1, 3, 5
        white_button_style = """
            QPushButton {
                background-color: white;
                color: black;
                border: none;
            }
            QPushButton:hover {
                background-color: #F0F0F0;
            }
            QPushButton:pressed {
                background-color: #CCCCCC;
            }
        """
        #buttons 1, 2
        dark_button_style = """
            QPushButton {
                background-color: #D3D3D3;
                color: black;
                border: none;
            }
            QPushButton:hover {
                background-color: #ECECEC;
                color: black;
            }
            QPushButton:pressed {
                background-color: white;
                color: black;
            }
        """

        number_font = QFont("Times New Roman", 24)

        #buttons
        self.buttons = []
        for i in range(1, 6):
            btn = QPushButton(str(i))
            btn.setFont(number_font)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            if i in (1, 3, 5):
                btn.setStyleSheet(white_button_style)
            else:
                btn.setStyleSheet(dark_button_style)

            btn.clicked.connect(lambda checked, num=i: self.on_button_clicked(num))

            h_layout.addWidget(btn)
            self.buttons.append(btn)

        layout.addLayout(h_layout)

        self.stack.addWidget(centralWidget)

        #create pages 1 to 5
        page_titles = {
            1: "Who Am I...",
            2: "Stats...",
            3: "Interests...",
            4: "Hobbies...",
            5: "Socials...",
        }

        for i in range(1, 6):
            page = QWidget()
            page_layout = QVBoxLayout()
            page.setLayout(page_layout)

            page_label = QLabel(page_titles[i])
            page_label.setFont(QFont("Times New Roman", 30))
            page_label.setAlignment(Qt.AlignCenter)
            page_layout.addWidget(page_label)

            back_button = QPushButton("Back")
            back_button.setFont(QFont("Times New Roman", 20))
            back_button.setFixedSize(120, 50)
            back_button.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: black;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #F0F0F0;
                }
                QPushButton:pressed {
                    background-color: #CCCCCC;
                }
            """)
            back_button.clicked.connect(lambda: self.stack.setCurrentIndex(0))
            page_layout.addWidget(back_button, alignment=Qt.AlignCenter)

            self.stack.addWidget(page)

    def on_button_clicked(self, number):
        messages = {
            1: "Who Am I...",
            2: "Stats...",
            3: "Interests...",
            4: "Hobbies...",
            5: "Socials...",
        }
        
        print(messages.get(number, f"Button {number} clicked!"))

        self.stack.setCurrentIndex(number)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()