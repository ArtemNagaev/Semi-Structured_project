import json
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Списки в QT"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox("Списки")
        self.groupBox.setLayout(self.formLayout)
        scroll = QScrollArea()
        scroll.setWidget(self.groupBox)
        scroll.setWidgetResizable(True)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

        #LineEdit
        #self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        #self.lineEdit.setObjectName("lineEdit")
        #self.formLayout.addWidget(self.lineEdit)
        
        #PushButton
        #self.pushButton = QtWidgets.QPushButton(self.groupBox)
        #self.pushButton.setObjectName("pushButton")
        #self.formLayout.addWidget(self.pushButton)
        #self.pushButton.setText("Добавить")
        #self.pushButton.clicked.connect(lambda: self.handle_item_clicked())
        
        self.show()

    def handle_item_clicked(self):
        if(len(self.lineEdit.text()) > 0):
            groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            #sizePolicy.setHorizontalStretch(1)
            #sizePolicy.setVerticalStretch(1)
            #sizePolicy.setHeightForWidth(groupBox_3.sizePolicy().hasHeightForWidth())
            groupBox_3.setSizePolicy(sizePolicy)
            groupBox_3.setTitle("")
            groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            groupBox_3.setObjectName("groupBox_3")
            horizontalLayout_2 = QtWidgets.QHBoxLayout(groupBox_3)
            horizontalLayout_2.setObjectName("horizontalLayout_2")
            label = QtWidgets.QLabel(groupBox_3)
            label.setObjectName("label")
            horizontalLayout_2.addWidget(label)
            pushButton_2 = QtWidgets.QPushButton(groupBox_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            #sizePolicy.setHorizontalStretch(0)
            #sizePolicy.setVerticalStretch(0)
            #sizePolicy.setHeightForWidth(pushButton_2.sizePolicy().hasHeightForWidth())
            pushButton_2.setSizePolicy(sizePolicy)
            pushButton_2.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
            pushButton_2.setObjectName("pushButton_2")
            pushButton_2.clicked.connect(lambda: self.destroy(groupBox_3))  
            horizontalLayout_2.addWidget(pushButton_2)
            label.setText(self.lineEdit.text())
            label.setWordWrap(True)
            pushButton_2.setText("Удалить")
            self.formLayout.addWidget(groupBox_3)
            self.lineEdit.setText("")
        print(self.lineEdit.text())
        print("Worked")

    def destroy(self,widget):
        widget.setParent(None)

    def jsonIteration(self, data, box, layout):
        for item in data:
            #находим значение для ключа
            print(item)
            #проверяем является ли это значение тоже дикшенери 
            if(isinstance(data[item], dict)):
                groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
                verticalLayout = QtWidgets.QVBoxLayout(groupBox_3)
                layout.addWidget(groupBox_3)
                #print("this is dict")
                #Идём вниз по уровню (обходим этот дикшенери)
                self.jsonIteration(data[item], groupBox_3, verticalLayout)
            else:
                #Если это не дикшенери - значит это массив или конечное значение
                #проверяем если это массив и не строка
                if (isinstance(data[item], list) and not(isinstance(data[item], str))):
                    # если массив то обходим его
                    for each in data[item]:
                        #проверяем на дикшенери (если это массив объектов)
                        if(isinstance(each, dict)):
                            groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
                            verticalLayout = QtWidgets.QVBoxLayout(groupBox_3)
                            layout.addWidget(groupBox_3)
                            #Идём вниз по уровню (обходим этот дикшенери)
                            self.jsonIteration(each, groupBox_3, verticalLayout)
                        else:
                            print(each)
                            label = QtWidgets.QLabel()
                            label.setObjectName("label")
                            label.setText(str(each))
                            layout.addWidget(label)
                else:
                    print(data[item])
                    label = QtWidgets.QLabel()
                    label.setObjectName("label")
                    label.setText(str(data[item]))
                    layout.addWidget(label)
                    if (data[item] == None):
                        print("ай ай ай")
                    
txt = Path('items.json').read_text()
data = json.loads(txt)                   
#test(data)
               
App = QApplication(sys.argv)
window = Window()
window.jsonIteration(data, window.groupBox, window.formLayout)
sys.exit(App.exec())
