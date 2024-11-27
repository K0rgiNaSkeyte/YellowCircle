from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class CircleUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Генерация окружностей")
        self.setGeometry(100, 100, 400, 400)
        self.createCircleButton = QPushButton("Создать окружность", self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.createCircleButton)
        self.setLayout(self.layout)
