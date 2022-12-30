
import sys
import os
from typing import Self

from main import current_date
from main import current_time

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

QQuickWindow.setSceneGraphBackend('software')
app = QApplication(sys.argv)


def button1_clicked():
   dlg = QMessageBox
   dlg.information(widget, "Here's the current date", current_date)
def button2_clicked():
   dlg = QMessageBox
   dlg.information(widget, "Here's the time", current_time)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/Main.qml')

widget = QWidget()
   
button1 = QPushButton(widget)
button1.setText("Data")
button1.move(200,32)
button1.clicked.connect(button1_clicked)

button2 = QPushButton(widget)
button2.setText("Time")
button2.move(90,32)
button2.clicked.connect(button2_clicked)

widget.setGeometry(250,300,300,200)
widget.setWindowTitle("Select one of the following")
widget.show()
   
sys.exit(app.exec())