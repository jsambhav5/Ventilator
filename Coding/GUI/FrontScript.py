#!/usr/bin/python3
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import sys

def start():  
    inputs.hide()
    readings.show()
    readings.Reset.clicked.connect(reset)

def reset():
    readings.hide()
    inputs.show()
    inputs.Start.clicked.connect(start)

app = QtWidgets.QApplication([])

inputs = uic.loadUi("/home/pi/Ventilator/Coding/GUI/Inputs.ui")
readings = uic.loadUi("/home/pi/Ventilator/Coding/GUI/Readings.ui")

reset()
app.exec()