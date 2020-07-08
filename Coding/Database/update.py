#!/usr/bin/python3
import time
import csv
import random
import pandas as pd

Time = 0
ECG1 = 1
ECG2 = 1
SpO2 = 1
PR = 1
PIP = 1
PEEP = 1
RR = 1
TV = 1
Sys = 1
Dia = 1

args = ["Time", "ECG1", "ECG2", "SpO2", "PR", "PIP", "PEEP", "RR", "TV", "Sys", "Dia"]

with open('/home/pi/Ventilator/Coding/Database/live.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = args)
    csv_writer.writeheader()

while True:
    with open('/home/pi/Ventilator/Coding/Database/live.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = args)

        info = {
            "Time" : Time,
            "ECG1" : ECG1,
            "ECG2" : ECG2,
            "SpO2" : SpO2,
            "PR"   : PR,
            "PIP"  : PIP,
            "PEEP" : PEEP,
            "RR"   : RR,
            "TV"   : TV,
            "Sys"  : Sys,
            "Dia"  : Dia
        }

        csv_writer.writerow(info)
        print(Time, ECG1, ECG2, SpO2, PR, PIP, PEEP, RR, TV, Sys, Dia)

        Time += 1
        ECG1 = random.randint(3,10)
        ECG2 = random.randint(3,10)
        SpO2 = random.randint(60,90)
        PR   = random.randint(60,90)
        PIP  = random.randint(60,90)
        PEEP = random.randint(60,90)
        RR   = random.randint(60,90)
        TV   = random.randint(60,90)
        Sys  = random.randint(60,90)
        Dia  = random.randint(100,130)

        lines = list()

    

    with open('/home/pi/Ventilator/Coding/Database/live.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
        if int(lines[-1][0]) > 30:
            lines.remove(lines[1])

    with open('/home/pi/Ventilator/Coding/Database/live.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


    time.sleep(.5)