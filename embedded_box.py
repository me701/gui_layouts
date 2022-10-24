import PyQt5
import PyQt5.QtWidgets
import sys

app = PyQt5.QtWidgets.QApplication(sys.argv) # the application

widget = PyQt5.QtWidgets.QDialog()

button = PyQt5.QtWidgets.QPushButton("Button")
text1 = PyQt5.QtWidgets.QLineEdit("Text 1")
text2 = PyQt5.QtWidgets.QLineEdit("Text 2")
def update_text():                          # notice that this slot function
    s = text1.text()
    text2.setText(s)                        # depends on the text widgets!
button.clicked.connect(update_text)   

text_widget = PyQt5.QtWidgets.QWidget()
vbox = PyQt5.QtWidgets.QVBoxLayout()
vbox.addWidget(text1)
vbox.addWidget(text2)
text_widget.setLayout(vbox)

hbox = PyQt5.QtWidgets.QHBoxLayout()
hbox.addWidget(button)
hbox.addWidget(text_widget)

widget.setLayout(hbox)
widget.show()                                # show the main widget
app.exec_()                                  # start the event loop