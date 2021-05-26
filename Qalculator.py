import sys

__version__ = '1.0'
__author__ = 'Majd Barakat'

from PyQt5.QtWidgets import QApplication
from GUI import UI
from control import QControl

def evaluateExpresion(expression):
    try:
        result = str(eval(expression, {}, {}))
    except:
        result = 'Error'

    return result

def main():
    """Qalculator main loop"""
    Qalculator = QApplication(sys.argv)

    #show Qalculator's GUI
    window = UI()
    window.show()

    eval = evaluateExpresion

    #create an instance of Qalculator Control
    QControl(viewUI= window, model = eval)
    sys.exit(Qalculator.exec_())

if __name__ == '__main__':
    main()
