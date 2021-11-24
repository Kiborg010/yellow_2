import sys
from random import randrange

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow

class Button(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.f = 0
        self.button.clicked.connect(self.draw)

    def draw(self):
        self.f = 1
        self.x = randrange(self.size().width())
        self.y = randrange(self.size().height())
        self.h = randrange(50)

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            self.draw_c(qp)
            self.update()
            qp.end()

    def draw_c(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.x, self.y, self.h, self.h)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = Button()
    b.show()
    sys.exit(app.exec())
