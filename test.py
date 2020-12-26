from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import json
from pathlib import Path
from PyQt5.QtGui import QPixmap 

app = Qt.QApplication([])

layout = Qt.QGridLayout()


txt = Path('items.json').read_text()
data = json.loads(txt)
print(txt)

def indexChange(i, j):
    i=i+1
    if(i>=4):
        i=0
        j=j+1
    return i,j


i = 0
j = 0
    
for item in data.values():

    #for key in item['stat']:
    #    print(key)
    
    group = Qt.QGroupBox("Item")

    
    VerticalLayout = Qt.QVBoxLayout(group)

    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(1)
    group.setSizePolicy(sizePolicy)

    
    layout.addWidget(group, j, i)
    i,j = indexChange(i,j)
    
    #Название
    try:
        group.setTitle(item['name'])
        print(item['name'])
    except:
        print("no name")
        
    #Иконка
    try:
        print(item['icon'])
        # creating label 
        label = Qt.QLabel("") 
          
        # loading image 
        pixmap = QPixmap('images/'+item['icon']) 
  
        # adding image to label
        
        label.setPixmap(pixmap.scaled(200,200))
        label.resize(50, 50)
        VerticalLayout.addWidget(label)

    except:
        print("no icon")

    #Один или массив статов
    try:
        print(item['stat'])
        if(isinstance(item['stat'], list)):
            for stat in item['stat']:
                label = Qt.QLabel(stat)
                VerticalLayout.addWidget(label)
        else:
            label = Qt.QLabel(item['stat'])
            VerticalLayout.addWidget(label)
        
    except:
        print("no stat")
    
    #Один или массив двойных статов
    print('statFloat')
    #if(isinstance(item['statFloat'], list)):
        #for statFloat in item['statFloat']:
            #print(statFloat.get('statValue'))
    
    try:
        if(isinstance(item['statFloat'], list)):
            for statFloat in item['statFloat']:
                group2 = Qt.QGroupBox("")
                VerticalLayout2 = Qt.QHBoxLayout(group2)
                label1 = Qt.QLabel(statFloat.get('statLabel')+": ")
                label2 = Qt.QLabel(str(statFloat.get('statValue')))
                VerticalLayout2.addWidget(label1)
                VerticalLayout2.addWidget(label2)
                VerticalLayout.addWidget(group2)
                    
            for statFloat in item['statFloat']:
                print(statFloat['statLabel'])

        else:
            group2 = Qt.QGroupBox("")
            VerticalLayout2 = Qt.QHBoxLayout(group2)
            label1 = Qt.QLabel(item['statFloat'].get('statLabel')+": ")
            label2 = Qt.QLabel(str(item['statFloat'].get('statValue')))
            VerticalLayout2.addWidget(label1)
            VerticalLayout2.addWidget(label2)
            VerticalLayout.addWidget(group2)
    except:
        print("can't do statFloat")
        
             
    try:
        if(isinstance(item['about'], list)):
            for statFloat in item['about']:
                group2 = Qt.QGroupBox(statFloat.get('title'))
                group2.setAlignment(QtCore.Qt.AlignHCenter)
                VerticalLayout2 = Qt.QHBoxLayout(group2)
                label = Qt.QLabel(statFloat.get('text'))
                label.setWordWrap(True)
                VerticalLayout2.addWidget(label)
                VerticalLayout.addWidget(group2)
                    
            for statFloat in item['about']:
                print(statFloat.get('title'))

        else:
            group2 = Qt.QGroupBox(item['about'].get('title'))
            group2.setAlignment(QtCore.Qt.AlignHCenter)
            VerticalLayout2 = Qt.QHBoxLayout(group2)
            label = Qt.QLabel(str(item['about'].get('text')))
            label.setWordWrap(True)
            VerticalLayout2.addWidget(label)
            VerticalLayout.addWidget(group2)
    except:
        print("can't do about")
        
    print("\n")
    
    #indexChange(i,j)
        
w = Qt.QWidget()

w.setLayout(layout)

mw = Qt.QScrollArea()
mw.setAlignment(QtCore.Qt.AlignCenter)
#mw.resize(260, 900)
mw.setWidget(w)
mw.showMaximized()

app.exec()
