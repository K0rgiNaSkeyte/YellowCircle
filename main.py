import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor
from UI import CircleUI


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = CircleUI()
        self.initUI()

    def initUI(self):
        self.radius = 0
        self.ui.createCircleButton.clicked.connect(self.generate_circle)
        self.setWindowTitle("Генерация окружностей")
        self.setGeometry(100, 100, 400, 400)
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)
        self.radii = []
        self.colors = []

    def generate_circle(self):
        radius = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radii.append(radius)
        self.colors.append(color)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for radius, color in zip(self.radii, self.colors):
            painter.setBrush(color)
            x = (self.width() - radius) // 2
            y = (self.height() - radius) // 2
            painter.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.show()
    sys.exit(app.exec())
