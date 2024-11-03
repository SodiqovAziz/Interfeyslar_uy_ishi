import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
win = QWidget()
hbox = QHBoxLayout()
vbox = QVBoxLayout()
a = 1

def save_file1(name, surname):
    with open('Login.txt', 'r', encoding='utf-8') as ing_file:
        ing_words = ing_file.read().splitlines()

    with open('Parol.txt', 'r', encoding='utf-8') as uzb_file:
        uzb_words = uzb_file.read().splitlines()

    dict(zip(ing_words, uzb_words))
    d = 0
    k = 0
    ingliz = open("Login.txt", "a")
    ing = name
    for i in ing_words:
        if i == ing:
            d = d + 1

    uzbek = open("Parol.txt", "a")
    uzb = surname
    for j in uzb_words:
        if j == uzb:
            k = k + 1

    if d == 0 and k == 0:
        ingliz.write(ing + '\n')
        ingliz.close()
        uzbek.write(uzb + '\n')
        uzbek.close()
        print('Faylga qoshildi.')
    elif d > 0 or k > 0:
        print('Bu soz Faylda bor.')


def save_file2(name, surname):
    with open('Login.txt', 'r', encoding='utf-8') as ing_file:
        ing_words = ing_file.read().splitlines()

    with open('Parol.txt', 'r', encoding='utf-8') as uzb_file:
        uzb_words = uzb_file.read().splitlines()

    dict(zip(ing_words, uzb_words))
    d = 0
    k = 0

    ing = name
    for i in ing_words:
        if i == ing:
            d = d + 1

    uzb = surname
    for j in uzb_words:
        if j == uzb:
            k = k + 1

    if d == 0 or k == 0:
        print('Faylda bunday soz yoq.')
    elif d > 0 and k > 0:
        print('Bu soz Faylda bor.')



def window():
    b1 = QLabel("Login:")
    b2 = QLineEdit()
    hbox1 = QHBoxLayout()
    hbox1.addWidget(b1)
    hbox1.addWidget(b2)
    vbox.addLayout(hbox1)

    b3 = QLabel("Parol:")
    b4 = QLineEdit()
    b4.setEchoMode(QLineEdit.Password)
    hbox2 = QHBoxLayout()
    hbox2.addWidget(b3)
    hbox2.addWidget(b4)
    vbox.addLayout(hbox2)
    button1 = QPushButton("Sign in")
    button2 = QPushButton("Sign up")
    vbox.addWidget(button1)
    vbox.addWidget(button2)

    def save_1():
        name = b2.text()
        surname = b4.text()
        save_file1(name, surname)

    def save_2():
        name = b2.text()
        surname = b4.text()
        save_file2(name, surname)

    button1.clicked.connect(save_1)
    button2.clicked.connect(save_2)
    win.setLayout(vbox)
    win.setWindowTitle("registratsiya")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
