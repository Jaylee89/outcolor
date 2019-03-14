# -*- coding:utf8 -*-

import sys

from PyQt5 import QtWidgets

class Form(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.browser = QtWidgets.QTextBrowser()
        self.line_edit = QtWidgets.QLineEdit()
        #文本编辑控件，选中所有文本并聚焦，设置事件监听
        self.line_edit.selectAll()
        self.line_edit.setFocus()
        self.line_edit.returnPressed.connect(self.update_ui)
        #垂直布局，并将两个控价加入到布局中
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.line_edit)
        #设置本窗体的布局
        self.setLayout(layout)
        self.setWindowTitle('Calculate')

    def update_ui(self):
        try:
            expression = self.line_edit.text()
            self.browser.append('%s = <b>%s</b>' % (expression, eval(expression)))
        except:
            self.browser.append('<font color=red>%s is invaild !</font>'%expression)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())