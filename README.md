# Qalculator
A simple calculator built using object-oriented programing and PyQt5
The design of the calculator uses Model-View-Controller (MVC) pattern. 

This repository contains 4 files:
* settings.py contains the Settings class which includes basic Qalculator settings such as height and width of the program's window.
* GUI.py contains the class UI which implements the user interface. This class inherits QMainWindow class from PyQt5.QWidgets and builds upon it to the display and layout of the Qalculator.
* control.py contains the QControl class which is responsible for connecting the signals emitted from the GUI, building the mathematical expression and evaluating it using the basic eval() function in python.
