'''
Created on 16 Apr 2013

@author: jrem
'''
from PySide.QtGui import QFrame, QGridLayout
from org.muscat.staldates.aldatesx.ui.widgets.Buttons import OutputButton

class OutputsGrid(QFrame):
    '''
    Grid of output buttons.
    '''

    def __init__(self):
        QFrame.__init__(self)
        layout = QGridLayout()

        self.btnProjectors = OutputButton(ID=2)
        self.btnProjectors.setText("Projectors")
        layout.addWidget(self.btnProjectors, 0, 1)

        self.btnChurch = OutputButton(ID=4)
        self.btnChurch.setText("Church")
        layout.addWidget(self.btnChurch, 1, 0)
        self.btnSpecial = OutputButton(ID=7)
        self.btnSpecial.setText("Special")
        layout.addWidget(self.btnSpecial, 1, 1)

        self.btnGallery = OutputButton(ID=6)
        self.btnGallery.setText("Gallery")
        layout.addWidget(self.btnGallery, 2, 0)
        self.btnWelcome = OutputButton(ID=5)
        self.btnWelcome.setText("Welcome")
        layout.addWidget(self.btnWelcome, 2, 1)

        self.btnFont = OutputButton(ID=3)
        self.btnFont.setText("Font")
        layout.addWidget(self.btnFont, 3, 0)
        self.btnRecord = OutputButton(ID=8)
        self.btnRecord.setText("Record")
        layout.addWidget(self.btnRecord, 3, 1)

        self.btnPCMix = OutputButton(ID=2)
        self.btnPCMix.setText("PC Mix")
        layout.addWidget(self.btnPCMix, 4, 0)
        self.btnAll = OutputButton(ID=0)
        self.btnAll.setText("All")
        layout.addWidget(self.btnAll, 4, 1)

        layout.setColumnMinimumWidth(0, 100)
        layout.setColumnMinimumWidth(1, 100)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        self.setLayout(layout)
        
    def connectMainOutputs(self, function):
        self.btnProjectors.clicked.connect(function)
        self.btnChurch.clicked.connect(function)
        self.btnSpecial.clicked.connect(function)
        self.btnGallery.clicked.connect(function)
        self.btnWelcome.clicked.connect(function)
        self.btnFont.clicked.connect(function)
        self.btnRecord.clicked.connect(function)
        self.btnAll.clicked.connect(function)
        
    def connectPreviewOutputs(self, function):
        self.btnPCMix.clicked.connect(function)
