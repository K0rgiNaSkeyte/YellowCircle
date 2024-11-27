import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit
from PyQt6.QtGui import QPainter, QColor
from circle_ui import Ui_Form


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.radius = 0
        self.ui.pushButton.clicked.connect(self.generate_circle)
        self.setWindowTitle("Генерация окружностей")
        self.setGeometry(100, 100, 400, 400)

    def generate_circle(self):
        self.radius = random.randint(10, 100)
        self.update()

    def paintCircle(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        width = self.width()
        height = self.height()
        x = (width - self.radius) // 2
        y = (height - self.radius) // 2
        painter.drawEllipse(x, y, self.radius, self.radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.show()
    sys.exit(app.exec_())
