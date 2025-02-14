# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:32:16 2022

@author: turtw
"""
# from os import getcwd,sep
from PyQt5 import QtGui
import pyqtgraph as pg
from PyQt5.QtCore import Qt, QThread, pyqtSignal,QObject
from PyQt5.QtWidgets import (QAction, qApp, QApplication, QDialog, QInputDialog,
                             QGridLayout, QLabel,QMainWindow, QMessageBox, QPushButton, 
                              QStyleFactory, QTextEdit, QWidget)
import sys
import numpy as np
import time
# import busio
# import digitalio
# import board
# import adafruit_mcp3xxx.mcp3008 as MCP
# from adafruit_mcp3xxx.analog_in import AnalogIn
#********************************************************************
'''Inicio User Interface'''
class Display(QMainWindow):
    def __init__(self, parent=None):
        super(Display, self).__init__(parent)                   #'Permite Iniciar GUI'
        self.originalPalette = QApplication.palette()           #'Estilo de la GUI'
        self.setWindowTitle("Biosensor Detect")                 #'Nombre de la Ventana (Aplicacion)'
        self.setGeometry(200, 150, 600, 400)                    #'Tamaño y posicion'
        self.setWindowIcon(QtGui.QIcon('pokeball.png'))         #'Icono de la APP'
        self.initUI()
        self.Widgett = WidgetG(self)
        self.setCentralWidget(self.Widgett)
        self.setStyleSheet("""QToolTip { 
                           background-color: black; 
                           color: white; 
                           border: black solid 1px
                           }""")
    #************************************************************
    '''Barra de Menu'''
    def initUI(self):
        '''Salir App'''
        self.exitAction = QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(qApp.quit)
        '''Ayuda'''
        self.helpAction = QAction(QtGui.QIcon('pokeball.png'), '&Info', self)
        self.helpAction.setShortcut('Ctrl+H')
        self.helpAction.setStatusTip('Created By Max Campos')
        '''Comite'''
        self.DrChanona= QAction(QtGui.QIcon('jorgChan.png'), '&Dr. JoseJorge', self)
        self.DrLopez=QAction(QtGui.QIcon('rubenLpe.png'), '&Dr. RubenLopez', self)
        self.DrMendoza=QAction(QtGui.QIcon('DrMendoza.png'), '&Dr. JorgeMendoza', self)
        self.DrVicente=QAction(QtGui.QIcon('DrVicente.png'), '&Dr. JuanVicente', self)
        self.DrHaydee=QAction(QtGui.QIcon('DrHaydde.png'), '&Dra. HaydeeMartinez', self)
        #helpMenu.addAction(self.aboutAction)
        self.DrChanona.triggered.connect(self.P1)
        self.DrLopez.triggered.connect(self.P1)
        self.DrMendoza.triggered.connect(self.P1)
        self.DrVicente.triggered.connect(self.P1)
        self.DrHaydee.triggered.connect(self.P1)
        #************************************************************
        '''Menu'''
        StatusBar = self.statusBar()
        MenuBar = self.menuBar()
        FileMenu = MenuBar.addMenu('&File')
        EditMenu = MenuBar.addMenu('Edit')
        ViewMenu = MenuBar.addMenu('View')
        SearchMenu = MenuBar.addMenu('Search')
        ToolsMenu = MenuBar.addMenu('Tools')
        HelpMenu = MenuBar.addMenu('Help')
        StatusBar.showMessage('ENCB IPN 2022')
        #************************************************************
        '''Acciones del menu'''
        FileMenu.addAction(self.exitAction)
        HelpMenu.addAction(self.helpAction)
        HelpMenu.addAction(self.DrChanona)
        HelpMenu.addAction(self.DrLopez)
        HelpMenu.addAction(self.DrMendoza)
        HelpMenu.addAction(self.DrVicente)
        HelpMenu.addAction(self.DrHaydee)
        self.show()    
    #************************************************************
    '''Funiciones del menu'''
    def P1(self):
        # QMessageBox.about(self, "DraHaydee", "3er Sinodal")
        method_name = self.sender()
        Jurado=method_name.text()
        msg = QMessageBox()
        if Jurado == '&Dr. JoseJorge':
            msg.setIconPixmap(QtGui.QPixmap('jorgChan.png'))
            msg.setText("Asesor 1")
        elif Jurado =='&Dr. RubenLopez':
            msg.setIconPixmap(QtGui.QPixmap('rubenLpe.png'))
            msg.setText("Asesor 2")
        elif Jurado =='&Dr. JorgeMendoza':
            msg.setIconPixmap(QtGui.QPixmap('DrMendoza.png'))
            msg.setText("1er Sinodal")
        elif Jurado =='&Dr. JuanVicente':
            msg.setIconPixmap(QtGui.QPixmap('DrVicente.png'))
            msg.setText("2do Sinodal")
        elif Jurado =='&Dra. HaydeeMartinez':
            msg.setIconPixmap(QtGui.QPixmap('DrHaydde.png'))
            msg.setText("3er Sinodal")
        msg.exec_()
#********************************************************************
'''Thread Worker'''
class Worker(QObject):
    '''Variables'''
    # Array's para guardar los datos
    finished = pyqtSignal()
    Result=pyqtSignal(list,list)
    # create the spi bus
    # self.spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    
    # # create the cs (chip select)
    # self.cs = digitalio.DigitalInOut(board.D5)
    
    # # create the mcp object
    # self.mcp = MCP.MCP3008(self.spi, self.cs)
    
    # create an analog input channel on pin 0
    '''Funciones'''     
    def UpdatePlot(self):
        self.dataX = [] 
        self.dataY = []
        self.lastY = 0
        self.T_step=0.1
        # global curva, dataX, dataY
        # Leemos la nueva línea
        # nuevoDato = float(chan.voltage)
        for i in range(50):
            nuevoDato=float(np.random.rand(1))
            # chan = AnalogIn(self.mcp, MCP.P0)
            # nuevoDato=float(chan.voltage)
            time.sleep(self.T_step)
            self.lastY=self.lastY+self.T_step
            #Agregamos los datos al array
            self.dataX.append(self.lastY)
            self.dataY.append(nuevoDato)
            #Actualizamos los datos y refrescamos la gráfica.
            self.Result.emit(self.dataX, self.dataY)
            # self.curva.setData(self.dataX, self.dataY)
            # Limitamos a mostrar solo 300 muestras
            # print(i)
            # print(len(self.dataX))
            if len(self.dataX) > 49:
                self.dataX = []
                self.dataY = []
                self.lastY=0
            QApplication.processEvents()
        self.finished.emit()

#********************************************************************        
'''Cosas Dentro'''
class WidgetG(QWidget):
    def __init__(self,parent):
        super(WidgetG, self).__init__(parent)                   #'Permite Iniciar GUI'   
        self.originalPalette = QApplication.palette()           #'Estilo de la GUI'
         #************************************************************
        '''Lectura Sensor'''
        self.Read_Sensor = QPushButton("Read")
        self.Read_Sensor.setDefault(True)
        self.Read_Sensor.clicked.connect(self.Leer) #**********************************************************
        # self.Read_Sensor.clicked.connect(self.UpdatePlot)
        self.Read_Sensor.setToolTip("Click to Read sensor")
        #************************************************************
        #************************************************************
        '''Posicion de los Objetos'''
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.setSpacing(5)
        self.mainLayout.columnMinimumWidth(10)
        self.canv = pg.plot(title="Grafica en tiempo real", pen='y')
        self.canv.showGrid(x=True,y=True)
        self.curva = self.canv.plot(pen='y')
        self.canv.setRange(yRange=[0, 1])
        self.canv.addLegend()
        #************************************************************
        '''Propiedades'''        
        self.canv.setLabel('left', 'Voltage', units='V')
        self.canv.setLabel('bottom', 'Time', units='s')
        self.mainLayout.addWidget(self.canv,1,1,Qt.AlignLeft)
        self.mainLayout.addWidget(self.Read_Sensor, 2, 1, Qt.AlignCenter)
        '''Apariencia'''
        QApplication.setStyle(QStyleFactory.create('Fusion'))   #Estilo de la ventana
        QApplication.setPalette(self.originalPalette)
    #************************************************************
    def Leer(self):
        '''Create a QThread object'''
        self.thread = QThread()
        '''Create a worker object'''
        self.worker = Worker()
        '''Move worker to the thread'''
        self.worker.moveToThread(self.thread)
        '''Connect signals and slots'''
        self.thread.started.connect(self.worker.UpdatePlot)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.Result.connect(self.curva.setData)
        # QApplication.processEvents()
        '''Start the thread'''
        self.thread.start()
        # Final resets
        self.Read_Sensor.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.Read_Sensor.setEnabled(True))
#************************************************************        
'''Inicia GUI'''
#app=QApplication.instance() # checks if QApplication already exists 
#if not app: # create QApplication if it doesnt exist 
#app.aboutToQuit.connect(app.deleteLater)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWi = Display()
    MainWi.show()
    sys.exit(app.exec_())             