import sys
from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu
from PyQt5.QtGui import QKeySequence, QCursor, QPen, QColor
from PyQt5.QtCore import Qt

def create_action(parent, text, slot=None,
                  shortcut=None, shortcuts=None, shortcut_context=None,
                  icon=None, tooltip=None,
                  checkable=False, checked=False):
    action = QtWidgets.QAction(text, parent)

    if icon is not None:
        action.setIcon(QIcon(':/%s.png' % icon))
    if shortcut is not None:
        action.setShortcut(shortcut)
    if shortcuts is not None:
        action.setShortcuts(shortcuts)
    if shortcut_context is not None:
        action.setShortcutContext(shortcut_context)
    if tooltip is not None:
        action.setToolTip(tooltip)
        action.setStatusTip(tooltip)
    if checkable:
        action.setCheckable(True)
    if checked:
        action.setChecked(True)
    if slot is not None:
        action.triggered.connect(slot)

    return action


class Settings():

    WIDTH = 20
    HEIGHT = 15
    NUM_BLOCKS_X = 10
    NUM_BLOCKS_Y = 14
    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600


class QScene(QtWidgets.QGraphicsScene):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.lines = []

        self.draw_grid()
        self.set_opacity(0.3)
        # self.set_visible(False)
        # self.delete_grid()

    def draw_grid(self):
        width = Settings.NUM_BLOCKS_X * Settings.WIDTH
        height = Settings.NUM_BLOCKS_Y * Settings.HEIGHT
        self.setSceneRect(0, 0, width, height)
        self.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)

        pen = QPen(QColor(255,0,100), 1, Qt.SolidLine)

        for x in range(0,Settings.NUM_BLOCKS_X+1):
            xc = x * Settings.WIDTH
            self.lines.append(self.addLine(xc,0,xc,height,pen))

        for y in range(0,Settings.NUM_BLOCKS_Y+1):
            yc = y * Settings.HEIGHT
            self.lines.append(self.addLine(0,yc,width,yc,pen))

    def set_visible(self,visible=True):
        for line in self.lines:
            line.setVisible(visible)

    def delete_grid(self):
        for line in self.lines:
            self.removeItem(line)
        del self.lines[:]

    def set_opacity(self,opacity):
        for line in self.lines:
            line.setOpacity(opacity)


class QView(QtWidgets.QGraphicsView):
    clicked = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.dragstart = None

        self.view_menu = QMenu(self)
        self.create_actions()

    def create_actions(self):
        act = create_action(self.view_menu, "Zoom in",
                            slot=self.on_zoom_in,
                            shortcut=QKeySequence("+"), shortcut_context=Qt.WidgetShortcut)
        self.view_menu.addAction(act)

        act = create_action(self.view_menu, "Zoom out",
                            slot=self.on_zoom_out,
                            shortcut=QKeySequence("-"), shortcut_context=Qt.WidgetShortcut)
        self.view_menu.addAction(act)
        self.addActions(self.view_menu.actions())

    def on_zoom_in(self):
        if not self.scene():
            return

        self.scale(1.5, 1.5)

    def on_zoom_out(self):
        if not self.scene():
            return

        self.scale(1.0 / 1.5, 1.0 / 1.5)

    # def toggleDrageMode(self):
    #     if self.dragMode() == ScrollHandDrag:
    #         self.setDragMode(NoDrag)
    #     elif not self.

    def mousePressEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            print(event.pos())
            self.dragstart = event.pos()
            self.clicked.emit()

    def mouseReleaseEvent(self, event):
        self.dragstart = None

    def mouseMoveEvent(self, event):
        # if event.buttons() and Qt.LeftButton:
        if event.buttons() == Qt.LeftButton and event.key() == Qt.Key_Control:
            print(event.pos())
            # painter.
        # if (self.dragstart is not None and
        #     event.buttons() & QtCore.Qt.LeftButton and
        #     (event.pos() - self.dragstart).manhattanLength() >
        #      QtWidgets.qApp.startDragDistance()):
        #     self.dragstart = None
        #     drag = QtGui.QDrag(self)
        #     drag.setMimeData(QtCore.QMimeData())
        #     drag.exec_(QtCore.Qt.LinkAction)

    # def mouseMoveEvent(self, event):
    #     if (self.dragstart is not None and
    #         event.buttons() & Qt.LeftButton and)

    def drawBackground(self, painter, rect):
        gr = rect.toRect()
        start_x = gr.left() + Settings.WIDTH - (gr.left() % Settings.WIDTH)
        start_y = gr.top() + Settings.HEIGHT - (gr.top() % Settings.HEIGHT)
        # painter.save()
        # painter.setPen(QtGui.QColor(60, 70, 80).lighter(90))
        # painter.setOpacity(0.7)

        # for x in range(start_x, gr.right(), Settings.WIDTH):
        #     painter.drawLine(x, gr.top(), x, gr.bottom())

        # for y in range(start_y, gr.bottom(), Settings.HEIGHT):
        #     painter.drawLine(gr.left(), y, gr.right(), y)

        # painter.restore()

        # super().drawBackground(painter, rect)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    scene = QScene()
    view = QView()
    view.setFixedSize(Settings.DISPLAY_WIDTH, Settings.DISPLAY_HEIGHT)
    view.setScene(scene)
    view.show()
    sys.exit(app.exec_())
    