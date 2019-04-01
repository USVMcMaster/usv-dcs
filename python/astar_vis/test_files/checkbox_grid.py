import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QCheckBox)
from PyQt5.QtCore import Qt
import numpy as np

class Example(QWidget):


    def __init__(self):
        super().__init__()
        self.grid =np.zeros([5,5], dtype=bool)
        self.initUI()

    def initUI(self):
        for i in range(5):
            for j in range(5):
                btn = checked(self, i, j)
                btn.move(50+17*i, 50+17*j)
                # btn.toggle()
                btn.stateChanged.connect(lambda state=btn, x=btn.x, y=btn.y: self.click(state, x, y))



        done = QPushButton('Done', self)
        done.clicked.connect(self._print)
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def click(self, state, x, y):
        if state == Qt.Checked:
            self.grid[x][y] = True
        else:
            pass


    def _print(self):
        print(self.grid)


class checked(QCheckBox):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.x = x
        self.y = y


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())