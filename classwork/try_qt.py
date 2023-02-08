import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sosem Bibu?")
        self.button = QPushButton("NO!!!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.setMinimumSize(200, 200)
        self.button.setMaximumSize(200, 200)


        self.setFixedSize(QSize(1280, 720))
        self.setCentralWidget(self.button)

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def the_button_was_clicked(self):
        print("KLASSNAYA BIBA!")
        self.label.setText(self.button.text())



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()