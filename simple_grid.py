import PyQt5
from PyQt5.QtWidgets import (QDialog, QPushButton, QGridLayout)
import sys

app = PyQt5.QtWidgets.QApplication(sys.argv) # the application

widget = QDialog()

buttons = [] 
for i in range(1, 10):
    buttons.append(QPushButton(str(i)))
buttons.append(QPushButton(str(0)))

grid = QGridLayout()
for i in range(9):
    grid.addWidget(buttons[i], i//3, i%3)
grid.addWidget(buttons[-1], 3, 1)

widget.setLayout(grid)
widget.show()                                # show the main widget
app.exec_()                                  # start the event loop