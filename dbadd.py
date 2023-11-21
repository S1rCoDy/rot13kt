from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import sys

def rot13(text, direction=1):
    result = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            symbols = LATIN_SYMBOLS if char.isascii() else CYRILLIC_SYMBOLS
            index = symbols.find(char.lower())
            
            # Применяем шифр ROT13 в зависимости от направления (шифровка или расшифровка)
            new_index = (index + direction * 13) % len(symbols)
            
            result += symbols[new_index].upper() if is_upper else symbols[new_index]
        else:
            result += char
    return result

LATIN_SYMBOLS = "abcdefghijklmnopqrstuvwxyz"
LATIN_LARGE_SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CYRILLIC_SYMBOLS = "бвгдёжзийклмнптфцчшщъыьэюя"
CYRILLIC_LARGE_SYMBOLS = "БГДЁЖЗИЙЛНПУФЦЧШЩЪЫЬЭЮЯ"
SYMBOLS = LATIN_SYMBOLS + CYRILLIC_SYMBOLS + CYRILLIC_LARGE_SYMBOLS + LATIN_LARGE_SYMBOLS

# Функция для шифровки текста
def encrypt(text):
    return rot13(text, direction=1)

# Функция для расшифровки текста
def decrypt(text):
    return rot13(text, direction=-1)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 500, 161, 41))

        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 111, 21))
        self.label.setMaximumSize(QtCore.QSize(151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 10, 141, 21))
        self.label_2.setMaximumSize(QtCore.QSize(151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        # Заменили QLineEdit на QTextEdit
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 59, 311, 411))
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.textEdit.setObjectName("textEdit")
        
        # Заменили QLineEdit на QTextEdit
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(450, 60, 311, 411))
        self.textEdit_2.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.textEdit_2.setObjectName("textEdit_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rot13 TK"))
        self.pushButton.setText(_translate("MainWindow", "Запуск"))
        self.label.setText(_translate("MainWindow", "Шифровка"))
        self.label_2.setText(_translate("MainWindow", "Разшифровка"))

    def add_functions(self):
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        input_text = self.textEdit.toPlainText().strip()
        output_text = self.textEdit_2.toPlainText().strip()

        if input_text and output_text:
            QtWidgets.QMessageBox.critical(
                self.pushButton,
                "Ошибка",
                "Только одно поле ввода должно быть заполнено.",
                QtWidgets.QMessageBox.StandardButton.Ok,
            )
            return

        if input_text:
            result = encrypt(input_text)
            self.textEdit_2.setText(result)
        elif output_text:
            result = decrypt(output_text)
            self.textEdit.setText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
