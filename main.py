import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("UI.ui", self)
        self.radius = 0
        self.createCircleButton.clicked.connect(self.generate_circle)
        self.setWindowTitle("Генерация окружностей")
        self.setGeometry(100, 100, 400, 400)
        self.radii = []

    def generate_circle(self):
        radius = random.randint(10, 100)
        self.radii.append(radius)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        width = self.width()
        height = self.height()
        x = (width - self.radius) // 2
        y = (height - self.radius) // 2
        painter.drawEllipse(x, y, self.radius, self.radius)
        for radius in self.radii:
            x = (self.width() - radius) // 2  # Центрируем окружность
            y = (self.height() - radius) // 2
            painter.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.show()
    sys.exit(app.exec())
