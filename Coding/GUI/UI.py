#!/usr/bin/python3
from PyQt5 import QtWidgets, uic,QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import pandas as pd

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi('/home/pi/Desktop/Ventilator/Coding/GUI/Readings.ui', self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # setting Timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.display)
        self.timer.start()

    def reset(self):
        os.system('systemctl reboot -i')
    


    def display(self):
        live = pd.read_csv('/home/pi/Desktop/Ventilator/Coding/Database/live.csv')
      
        self.ECG1.plotItem.clear()
        self.ECG2.plotItem.clear()
        self.SpO2_Graph.plotItem.clear()
        
        self.PR.setDigitCount(3)
        self.SpO2.setDigitCount(3)
        self.PIP.setDigitCount(3)
        self.PEEP.setDigitCount(3)
        self.RR.setDigitCount(3)
        self.TV.setDigitCount(3)
        self.Sys.setDigitCount(3)
        self.Dia.setDigitCount(3)

        self.PR.display(live['PR'].tail(1))
        self.SpO2.display(live['SpO2'].tail(1))
        self.PIP.display(live['PIP'].tail(1))
        self.PEEP.display(live['PEEP'].tail(1))
        self.RR.display(live['RR'].tail(1))
        self.TV.display(live['TV'].tail(1))
        self.Sys.display(live['Sys'].tail(1))
        self.Dia.display(live['Dia'].tail(1))

        self.ECG1.plotItem.hideAxis('left')
        self.ECG1.plotItem.hideAxis('bottom')
        self.ECG2.plotItem.hideAxis('left')
        self.ECG2.plotItem.hideAxis('bottom')
        self.SpO2_Graph.plotItem.hideAxis('left')
        self.SpO2_Graph.plotItem.hideAxis('bottom')
        
        self.ECG1.plot(live['Time'],live['ECG1'])
        self.ECG2.plot(live['Time'],live['ECG2'])
        self.SpO2_Graph.plot(live['Time'],live['SpO2'])
        self.Reset.clicked.connect(self.reset)
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':      
    main()