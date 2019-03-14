# -*- coding:utf8 -*-

import sys, time

from PyQt5 import QtWidgets, QtCore

#每个 PyQt5对象必须有一个 QApplication 对象，并且传入启动参数。
app = QtWidgets.QApplication(sys.argv)

try:
    due = QtCore.QTime()
    message = "Usage: alert.py %s:%s [optional message]"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(':')
    due = QtCore.QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = ' '.join(sys.argv[2:])
    message = message % (hours, mins)
except ValueError:
    message = 'Usage: alert.py HH:MM [optional message]' #24hr clock

while QtCore.QTime.currentTime() < due:
    time.sleep(20) # 20 seconds

#QLabel 可以接受HTML对象并正确的渲染
label = QtWidgets.QLabel('<font color=red size=72><b>' + message + '</b></font>')
label.show()
#发送一次信号，参数为(time, action)
QtCore.QTimer.singleShot(60000, app.quit) # 1 minute
app.exec_()