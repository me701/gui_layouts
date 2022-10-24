import PyQt5
import PyQt5.QtWidgets
import sys

app = PyQt5.QtWidgets.QApplication(sys.argv) # the application

widget = PyQt5.QtWidgets.QDialog()

button = PyQt5.QtWidgets.QPushButton("Button")
text = PyQt5.QtWidgets.QLineEdit("Text")
def update_text():                          # notice that this slot function
    text.setText("button was clicked!")     # depends on the text widget!
button.clicked.connect(update_text)         
hbox = PyQt5.QtWidgets.QHBoxLayout()
hbox.addWidget(button)
hbox.addWidget(text)

widget.setLayout(hbox)
widget.show()                                # show the main widget
app.exec_()                                  # start the event loop