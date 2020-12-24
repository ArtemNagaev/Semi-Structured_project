from PyQt5 import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import json
from pathlib import Path


app = Qt.QApplication([])

layout = Qt.QGridLayout()

txt = Path('items.json').read_text()
data = json.loads(txt)
print(txt)

i = 0
for item in data.values():
    
    group = Qt.QGroupBox("item")

    
    VerticalLayout = Qt.QVBoxLayout(group)

    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    group.setSizePolicy(sizePolicy)
    
    layout.addWidget(group, i, 1)

    print(item['name'])
    #label = Qt.QLabel("tesesdasfasf")
    #VerticalLayout.addWidget(label)
    
    try:
        group.setTitle(item['name'])
        print(item['name'])
    except:
        print("no name")
    try:
        print(item['stat'])
        label = Qt.QLabel(item['stat'])
        VerticalLayout.addWidget(label)

        i=i+1
    except:
        print("no stat")        
    try:
        print(item['icon'])
        label = Qt.QLabel(item['icon'])
        VerticalLayout.addWidget(label)

        i=i+1
    except:
        print("no icon")
    print("\n")
    i=i+1

#for i in range(10):
#    for j in range(5):
#        label = Qt.QLabel("tesesdasfasf")
#        layout.addWidget(label, i, j)
        #button = Qt.QPushButton('{}x{}'.format(i, j))
        #layout.addWidget(button, i, j)
        
w = Qt.QWidget()
w.setLayout(layout)

mw = Qt.QScrollArea()
mw.setWidget(w)
mw.show()

app.exec()
