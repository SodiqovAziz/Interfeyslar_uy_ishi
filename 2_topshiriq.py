from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout
import sys


class TetrisShapes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        self.buttons = []

        for i in range(1, 5):
            btn = QPushButton(str(i))
            btn.clicked.connect(lambda checked, idx=i: self.show_shape(idx))
            button_layout.addWidget(btn)
            self.buttons.append(btn)

        main_layout.addLayout(button_layout)

        self.shape_layout = QGridLayout()
        main_layout.addLayout(self.shape_layout)

        self.colors = {
            1: "#00CCCC",
            2: "#B200FF",
            3: "#4D4DFF",
            4: "#CC0000"
        }

        self.setLayout(main_layout)
        self.setWindowTitle('Tetris Shapes on Button Click')
        self.show()

    def clear_shape(self):
        for i in reversed(range(self.shape_layout.count())):
            widget_to_remove = self.shape_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

    def show_shape(self, shape_id):
        self.clear_shape()

        if shape_id == 1:
            self.draw_shape_L(self.shape_layout, self.colors[shape_id], 0, 0)
        elif shape_id == 2:
            self.draw_shape_square(self.shape_layout, self.colors[shape_id], 0, 4)
        elif shape_id == 3:
            self.draw_shape_line(self.shape_layout, self.colors[shape_id], 2, 0)
        elif shape_id == 4:
            self.draw_shape_s(self.shape_layout, self.colors[shape_id], 2, 4)

    def draw_shape_L(self, layout, color, row, col):
        positions = [(0, 0), (1, 0), (2, 0), (2, 1)]
        self.add_buttons(layout, color, positions, row, col)

    def draw_shape_square(self, layout, color, row, col):
        positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.add_buttons(layout, color, positions, row, col)

    def draw_shape_line(self, layout, color, row, col):
        positions = [(0, 0), (0, 1), (0, 2), (0, 3)]
        self.add_buttons(layout, color, positions, row, col)

    def draw_shape_s(self, layout, color, row, col):
        positions = [(0, 1), (0, 2), (1, 0), (1, 1)]
        self.add_buttons(layout, color, positions, row, col)

    def add_buttons(self, layout, color, positions, row_offset, col_offset):
        for r, c in positions:
            btn = QPushButton()
            btn.setStyleSheet(f"background-color: {color}; border: none;")
            layout.addWidget(btn, row_offset + r, col_offset + c)


app = QApplication(sys.argv)
ex = TetrisShapes()
sys.exit(app.exec_())
