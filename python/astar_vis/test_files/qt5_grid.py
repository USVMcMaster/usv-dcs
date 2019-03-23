import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QGraphicsRectItem
# from PyQt5 import QGraphicsRectItem
class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        width, height = 10,10
        for x in range(3):
            for y in range(3):
                # button = QPushButton(str(str(3*x+y)))
                # grid_layout.addWidget(button, x, y)
                setRect(QRectF(x,y,width,height))
        
        self.setWindowTitle('Basic Grid Layout')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())