import json
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from PyQt5.QtGui import QPixmap 
import sys
import urllib

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
        self.show()


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
                            try:
                                pixmap = QPixmap('images/'+each)  
                                label.setPixmap(pixmap.scaled(100,100))
                                #label.resize(25, 25)
                                layout.addWidget(label)
                                print("added icon")
                                if(pixmap.isNull()):
                                    raise ValueError('A very specific bad thing happened.')
                            except:
                                try:
                                    o = urllib.parse.urlparse(each).netloc
                                    if (o == ''):
                                        raise ValueError('A very specific bad thing happened.')
                                    else:
                                        label.setObjectName("label")
                                        label.setText('<a href="'+str(each)+'">'+ str(each) +'</a>')
                                        label.setOpenExternalLinks(True)
                                        label.setWordWrap(True)
                                        layout.addWidget(label) 
                                except:
                                    label.setObjectName("label")
                                    label.setText(str(each))
                                    label.setWordWrap(True)
                                    layout.addWidget(label)
                else:
                    print(data[item])
                    label = QtWidgets.QLabel(u"Кириллица")
                    #label = QtWidgets.QLineEdit()
                    
                    try:
                        pixmap = QPixmap('images/'+data[item])  
                        label.setPixmap(pixmap.scaled(100,100))
                        #label.resize(25, 25)
                        layout.addWidget(label)
                        if(pixmap.isNull()):
                            raise ValueError('A very specific bad thing happened.')
                    except:
                        try:
                            o = urllib.parse.urlparse(data[item]).netloc
                            if (o == ''):
                                raise ValueError('A very specific bad thing happened.')
                            else:
                                label.setObjectName("label")
                                label.setText('<a href="'+str(data[item])+'">'+ str(data[item]) +'</a>')
                                label.setOpenExternalLinks(True)
                                label.setWordWrap(True)
                                layout.addWidget(label)
                            print("url" + data[item])
                        except:
                            label.setObjectName("label")
                            label.setText(str(data[item]))
                            label.setWordWrap(True)
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
