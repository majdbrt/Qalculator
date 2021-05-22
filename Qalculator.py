import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow

# QVBoxLayout for the general layout,
# QGridLayout to arrange buttons,
# QLineEdit for the display and
# QPushButton for buttons.
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtCore import Qt

#
from functools import partial

from settings import Settings


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Settings = Settings()
        self.setWindowTitle(self.Settings.window_title)
        self.setFixedSize(self.Settings.window_width, self.Settings.window_height)
        #self.move(60,15)

        self.general_layout = QVBoxLayout()

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(self.general_layout)

        self.create_display()
        self.create_buttons()

    def create_display(self):
        """create the Qalculator's display"""

        self.display = QLineEdit()

        # set properties
        self.display.setFixedHeight(int(self.Settings.window_height*0.1))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("QLineEdit { background-color: rgb(0, 0, 0) }")


        # add display to general layout
        self.general_layout.addWidget(self.display)

    def create_buttons(self):
        """create the Qalculator's buttons"""

        buttons_layout = QGridLayout()

        # button's symbol | button's position on grid
        buttons = {
            'C' : (0,0),
            '%' : (0,1),
            '+/-' : (0,2),
            '/' : (0,3),
            '7' : (1,0),
            '8' : (1,1),
            '9' : (1,2),
            '*': (1, 3),
            '4': (2, 0),
            '5': (2, 1),
            '6': (2, 2),
            '-': (2, 3),
            '1': (3, 0),
            '2': (3, 1),
            '3': (3, 2),
            '+': (3, 3),
            '.': (4, 0),
            '0': (4, 1),
            'sqrt': (4, 2),
            '=': (4, 3),
        }#dict

        # creating buttons and adding them on grid layout
        for key, value in buttons.items():
            buttons[key] = QPushButton(key)

            buttons[key].setFixedSize(int(self.Settings.window_width*0.2), int(self.Settings.window_width*0.2))

            buttons_layout.addWidget(buttons[key],value[0],value[1])

        self.general_layout.addLayout(buttons_layout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')

class Control:
    def __init__(self, viewUI):
        self.view = viewUI
        self.connectSignals()

    #def buildExpression(self, ):


def main():
    """Qalculator main loop"""
    Qalculator = QApplication(sys.argv)

    #show Qalculator's GUI
    window = UI()
    window.show()

    sys.exit(Qalculator.exec_())

main()
