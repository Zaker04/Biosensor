# Biosensor
##		Prerequisites
Before running the code, make sure you have the following libraries installed:
- Busio
- Digitalio
- Board
- PyQt5
- Adafruit_mcp3xxx

```Read Getting started to see how to download the necessaary libraries```

##		Overview
This repository contains a Graphical User Interface (GUI) developed in Python using PyQt5 
to interface with a biosensor. The GUI utilizes the MCP3008 ADC with a Raspberry Pi to read 
analog sensor data and displays the values in real-time.


##		Features


- Real-time Data Display: Visualize sensor data in real-time on the GUI.

- Easy to Use: The user-friendly interface allows for seamless interaction with the biosensor.

- Portable: The setup, including an LCD screen with the Raspberry Pi, 
can be used anywhere with access to electricity.

##		Getting Started
```
To run the code, ensure you have the required libraries installed.
You can install them using the following commands:
```
```
pip install pyqt5
```
For detailed instructions on how to install the libraries for MCP, 
please visit this [webpage](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008)

##		Usage
Clone this repository and navigate to the project directory.
```
# Clone this repository
$ git clone https://github.com/Zaker04/Biosensor.git
```
 Run the main script to launch the GUI:
```
python UI_Sensor_6.0.py
```

## Important Note
Note for Raspberry Pi Users: Some lines of code need to be uncommented to run 
on the Raspberry Pi. For testing on other operating systems, these lines should remain commented.

### Import Section
In this section `Uncomment the #` like
```
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
```

### Variables Section
In this section `Uncommnetn the #`
```    
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
```

### Function Section
In this section be very careful:
- First `Uncomment the #`.
- Second `Comment the line nuevoDato=float(np.random.rand(1))`.
- Third you can change the number of data to red modifiying the number in this line `if len(self.dataX) > 49:`.

```
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
            if len(self.dataX) > 49:
                self.dataX = []
                self.dataY = []
                self.lastY=0
            QApplication.processEvents()
        self.finished.emit()
```

##		License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.