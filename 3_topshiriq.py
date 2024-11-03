from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
import sys

class NumberDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("1 dan 1000 gacha son kiriting")
        layout.addWidget(self.input_line)

        self.ok_button = QPushButton("Ok")
        self.ok_button.clicked.connect(self.display_number)
        layout.addWidget(self.ok_button)

        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)
        self.setWindowTitle("Sonni ko'rsatish")
        self.show()

    def display_number(self):
        try:
            number = int(self.input_line.text())
            if 1 <= number <= 1000:
                n = number // 100
                m = number // 10 % 10
                r = number % 10
                self.button1.setText(str(n))
                self.button2.setText(str(m))
                self.button3.setText(str(r))
            else:
                QMessageBox.warning(self, "Xato", "Iltimos, 1 dan 1000 gacha bo'lgan son kiriting.")
        except ValueError:
            QMessageBox.warning(self, "Xato", "Faqat raqam kiriting.")

app = QApplication(sys.argv)
ex = NumberDisplay()
sys.exit(app.exec_())
