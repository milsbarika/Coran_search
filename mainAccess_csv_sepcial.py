# -*- coding: utf-8 -*-
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtWidgets, QtCore, QtGui
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
import sys
import os
from os import path
import pandas as pd

import csv
WINDOW_SIZE = 0;
global df

#import UI file
FORM_CLASS,_ =loadUiType(path.join(path.dirname(__file__),'coran_csv.ui'))	

class MyProject(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MyProject, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.maFenetre()
        self.getCoran()
        global df
        # canvas here
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        # end of canvas

        self.horizontalLayout_7.addWidget(self.canvas)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.closeButton.clicked.connect(lambda: self.close())       
        self.btn_csv.clicked.connect(self.getCSV)
        self.btn_coran.clicked.connect(self.getCoran)
        self.btn_describe.clicked.connect(self.describe) 
        self.btn_ToutGraphe.clicked.connect(self.plotTout)
        self.listSowar.itemClicked.connect(self.select_listSowar) 
        self.btn_view.clicked.connect(self.plotOnCanvas)
        self.btn_view_2.clicked.connect(self.plotOnCanvas2)
        
   
 
    def select_listSowar(self):
        global NomSorat   
       	NomSorat=str(self.listSowar.currentItem().text())
        self.df = pd.read_csv('./allFiles/'+NomSorat+'.csv', encoding='utf8')
        self.openFile() 
                           
    def openFile(self): 
        global NomSorat        
        f = open(('./allFiles/'+NomSorat+'.txt'), 'r')          
        with f:
            
            data = f.read()
            self.textEdit.setText(data) 

    def describe(self):
        afficher = "Description de la Colonne: "+'(( '+str(self.comboEtat.currentText())+' ))'+'\n' +str(self.df[self.comboEtat.currentText()].describe())
       # afficher = "Description de la Colonne: \n"+str(self.df['col2'].describe())
        self.textEdit_Descrip.setText(afficher) 
        self.plotUnSeul()
        
################ Ploting 2 Variables ###################           
#######################Canvas##############"  
        
    def plotOnCanvas2(self):
        
        maListe1=['El fatiha', 'El bakara', 'Al imrane', 'El nissae', 'El maida', 'El anaame', 'El araffe', 'El anfale', 'El taouba', 'Younes', 'Houd', 'Youssef', 'El raade', 'Ibrahim', 'El hajar', 'El nahle', 'El issrae', 'El kahaf', 'Mariam', 'taha', 'El anbiae', 'El hadj', 'El mouminoun', 'El nour', 'El fourkane', 'El chouaarae', 'El namel', 'El kassasse', 'El ankabout', 'El roum', 'Lokmane', 'El sajda', 'El ahzabe', 'Sabae', 'Fater', 'Yassine', 'El saffate', 'Sad', 'El zoumar', 'Ghafer', 'Fossilate', 'El choura', 'El zoukhrouf', 'El doukhane', 'El jathia', 'El ahkhafe', 'Mohamed(alihiSalatwaSalam)', 'El fatah', 'El houjarate', 'khafe', 'El dhariyate', 'El thour', 'El nadjme', 'El khamar', 'El rahmane', 'El wakhiaate', 'El hadid', 'El moujadala', 'El hacher', 'El moumtahina', 'El saffe', 'El djoumouaa', 'El mounafikoune', 'El taghaboun', 'El talakh', 'El tahrim', 'El moulk', 'El kalam', 'El hakhat', 'El maarej', 'Nouh', 'El djin', 'El mouzamil', 'El moudathir', 'El kiyama', 'El inssane', 'El mourssalate', 'El nabae', 'El naziaate', 'Aabassa', 'El takouir', 'El infitar', 'El moutafifine', 'El inchikake', 'El bourouj', 'El tarek', 'El aalaee', 'El ghachiya', 'El fadjer', 'El balad', 'El chamsse', 'El laiile', 'El doha', 'El charah', 'El tine', 'El aalak', 'El kadar', 'El baiina', 'El zalzala', 'El adiyate', 'El kariaa', 'El takathour', 'El asser', 'El hamza', 'El file', 'Koreich', 'El maoune', 'El kaoutar', 'El kafiroune', 'El nasser', 'El massad', 'El ikhlasse', 'El falagh', 'El nasse']

        x=self.df[self.comboX.currentText()]
        y=self.df[self.comboY.currentText()]
        indice1=self.comboX.currentIndex()
        indice2=self.comboY.currentIndex()
        # fig, axes = plt.subplots()


        if self.comboBox.currentText() == 'bar':
            # clear canvas
            self.figure.clear()
            # self.figure.add_subplot(1,1,1)
            axes = self.figure.add_subplot(1,1,1)
            # axes = self.figure.add_subplot(1,1,1, projection='3d')

            
            x = np.linspace(-5,5,10)
            y = np.linspace(-5,5,10)
            
            x,y=np.meshgrid(x,y)
            z = x**2 + y**2
            
            plt.contour(x,y,z, levels=50, cmap='coolwarm')
            plt.colorbar()
            axes.set_xlabel("X axis")
            axes.set_ylabel("Y axis")
            # axes.set_zlabel("Z axis")
            axes.set_title('AXES Ma fonction')
            
            self.canvas.draw()
            
        if self.comboBox.currentText() == 'scatter':
            # clear canvas
            self.figure.clear()
            fig, axes = plt.subplots()
            # create scatter plot
            axes.scatter(x,y)
            axes.set_xlabel(str(maListe1[indice1]))
            axes.set_ylabel(str(maListe1[indice2]))
            axes.set_title('AXES Corrélation entre Les 2 sourates')
            # refresh canvas
            self.canvas.draw()           
                                   
                    
################ Ploting 2 Variables ###################             
        
    def plotOnCanvas(self):
        
        maListe1=['El fatiha', 'El bakara', 'Al imrane', 'El nissae', 'El maida', 'El anaame', 'El araffe', 'El anfale', 'El taouba', 'Younes', 'Houd', 'Youssef', 'El raade', 'Ibrahim', 'El hajar', 'El nahle', 'El issrae', 'El kahaf', 'Mariam', 'taha', 'El anbiae', 'El hadj', 'El mouminoun', 'El nour', 'El fourkane', 'El chouaarae', 'El namel', 'El kassasse', 'El ankabout', 'El roum', 'Lokmane', 'El sajda', 'El ahzabe', 'Sabae', 'Fater', 'Yassine', 'El saffate', 'Sad', 'El zoumar', 'Ghafer', 'Fossilate', 'El choura', 'El zoukhrouf', 'El doukhane', 'El jathia', 'El ahkhafe', 'Mohamed(alihiSalatwaSalam)', 'El fatah', 'El houjarate', 'khafe', 'El dhariyate', 'El thour', 'El nadjme', 'El khamar', 'El rahmane', 'El wakhiaate', 'El hadid', 'El moujadala', 'El hacher', 'El moumtahina', 'El saffe', 'El djoumouaa', 'El mounafikoune', 'El taghaboun', 'El talakh', 'El tahrim', 'El moulk', 'El kalam', 'El hakhat', 'El maarej', 'Nouh', 'El djin', 'El mouzamil', 'El moudathir', 'El kiyama', 'El inssane', 'El mourssalate', 'El nabae', 'El naziaate', 'Aabassa', 'El takouir', 'El infitar', 'El moutafifine', 'El inchikake', 'El bourouj', 'El tarek', 'El aalaee', 'El ghachiya', 'El fadjer', 'El balad', 'El chamsse', 'El laiile', 'El doha', 'El charah', 'El tine', 'El aalak', 'El kadar', 'El baiina', 'El zalzala', 'El adiyate', 'El kariaa', 'El takathour', 'El asser', 'El hamza', 'El file', 'Koreich', 'El maoune', 'El kaoutar', 'El kafiroune', 'El nasser', 'El massad', 'El ikhlasse', 'El falagh', 'El nasse']

        x=self.df[self.comboX.currentText()]
        y=self.df[self.comboY.currentText()]
        indice1=self.comboX.currentIndex()
        indice2=self.comboY.currentIndex()
        


        if self.comboBox.currentText() == 'bar':
            # clear canvas
            self.figure.clear()
            
            # create scatter plot
            plt.scatter(x,y)
            plt.bar(x,y, color='yellow', width=0.4)
            plt.xlabel(str(maListe1[indice1]))
            plt.ylabel(str(maListe1[indice2]))
            plt.title('Correlation entre Les 2 sourates')
            # refresh canvas
            self.canvas.draw()
            
        if self.comboBox.currentText() == 'scatter':
            # clear canvas
            self.figure.clear()
            
            # create bar plot
            plt.scatter(x,y)
            # plt.bar(monthOfTheYear,values, color='yellow', width=0.4)
            plt.xlabel(str(maListe1[indice1]))
            plt.ylabel(str(maListe1[indice2]))
            plt.title('Corrélation entre Les 2 sourates')
            # refresh canvas
            self.canvas.draw()           
                                                       
################ Ploting Un Variable ###################
        
    def plotUnSeul(self):
        maListe1=['El fatiha', 'El bakara', 'Al imrane', 'El nissae', 'El maida', 'El anaame', 'El araffe', 'El anfale', 'El taouba', 'Younes', 'Houd', 'Youssef', 'El raade', 'Ibrahim', 'El hajar', 'El nahle', 'El issrae', 'El kahaf', 'Mariam', 'taha', 'El anbiae', 'El hadj', 'El mouminoun', 'El nour', 'El fourkane', 'El chouaarae', 'El namel', 'El kassasse', 'El ankabout', 'El roum', 'Lokmane', 'El sajda', 'El ahzabe', 'Sabae', 'Fater', 'Yassine', 'El saffate', 'Sad', 'El zoumar', 'Ghafer', 'Fossilate', 'El choura', 'El zoukhrouf', 'El doukhane', 'El jathia', 'El ahkhafe', 'Mohamed(alihiSalatwaSalam)', 'El fatah', 'El houjarate', 'khafe', 'El dhariyate', 'El thour', 'El nadjme', 'El khamar', 'El rahmane', 'El wakhiaate', 'El hadid', 'El moujadala', 'El hacher', 'El moumtahina', 'El saffe', 'El djoumouaa', 'El mounafikoune', 'El taghaboun', 'El talakh', 'El tahrim', 'El moulk', 'El kalam', 'El hakhat', 'El maarej', 'Nouh', 'El djin', 'El mouzamil', 'El moudathir', 'El kiyama', 'El inssane', 'El mourssalate', 'El nabae', 'El naziaate', 'Aabassa', 'El takouir', 'El infitar', 'El moutafifine', 'El inchikake', 'El bourouj', 'El tarek', 'El aalaee', 'El ghachiya', 'El fadjer', 'El balad', 'El chamsse', 'El laiile', 'El doha', 'El charah', 'El tine', 'El aalak', 'El kadar', 'El baiina', 'El zalzala', 'El adiyate', 'El kariaa', 'El takathour', 'El asser', 'El hamza', 'El file', 'Koreich', 'El maoune', 'El kaoutar', 'El kafiroune', 'El nasser', 'El massad', 'El ikhlasse', 'El falagh', 'El nasse']

        self.df = pd.read_csv('./allFiles/Coranxat5.csv')

        indiceEtat=self.comboEtat.currentIndex()
        x=self.df[self.comboEtat.currentText()]
        
                                        #####################
        self.graphicsView.clear()
     
        self.graphicsView.setBackground('#000000')
        
        styles = {"color": "#fff", "font-size": "8px"}
        self.graphicsView.setLabel('left', maListe1[indiceEtat])
        self.graphicsView.setLabel('bottom', "<span style=\"color:orange;font-size:10px\">Les lettres</span>")
        
        #Add legend
        # self.graphicsView.addLegend()
        #Add grid
        self.graphicsView.showGrid(x=True, y=True)
    
        self.graphicsView.setXRange(0, 35, padding=0)
#        self.graphicsView.setYRange(0, 20, padding=0)
        pen = pg.mkPen(color=(255, 255, 0), width=1)
#        self.graphicsView.plot(x, pen=pen, symbol='+', symbolSize=8, symbolBrush=('r'))
        self.graphicsView.plot(x, name="flag",  pen=pen, symbol='o', symbolSize=2, symbolBrush=('#ff0000'))
        # self.label_3.setText(NomSorat) 
#       PlotWidget.plot(x,y[i],pen=(i,3))  
        
############################

    def plotTout(self):
        self.graphicsView.clear()
        self.df = pd.read_csv('./allFiles/Coranxat5.csv')

             
        self.graphicsView.setBackground('#000000')
        
        styles = {"color": "#fff", "font-size": "8px"}
        self.graphicsView.setLabel('left', "<span style=\"color:orange;font-size:10px\">Tout les Sowars</span>")
        self.graphicsView.setLabel('bottom', "<span style=\"color:orange;font-size:10px\">Les lettres</span>")
        
        #Add legend
        # self.graphicsView.addLegend()
        #Add grid
        self.graphicsView.showGrid(x=True, y=True)
    
        self.graphicsView.setXRange(0, 35, padding=0)
        pen = pg.mkPen(color=(0, 255, 0), width=1)
        for sora in self.df:
            # plt.plot(self.df.index,self.df[sora], marker='.')
            self.graphicsView.plot(self.df[sora], name="flag",  pen=pen, symbol='o', symbolSize=2, symbolBrush=('#ff0000'))
        # self.label_3.setText(NomSorat) 
#            PlotWidget.plot(x,y[i],pen=(i,3))
            
     
################# GET CORAN et FILES#####
            
    def getCoran(self):
        self.graphicsView.clear()
        self.textEdit_Base.setText('') 
        self.textEdit_Descrip.setText('')
        self.comboX.clear()
        self.comboY.clear()
        self.comboEtat.clear()
        self.df = pd.read_csv('./allFiles/Coranxat5.csv')
        # print("maListe= ",self.df.columns.tolist()) 
        # global df
        self.comboX.addItems(list(self.df.columns.values))
        self.comboY.addItems(list(self.df.columns.values))
        self.comboEtat.addItems(list(self.df.columns.values)) 
        
        afficher = "Description de la Base: \n"+str(self.df.describe())
        self.textEdit_Base.setText(afficher)
        
        
    def getCSV(self):
        self.graphicsView.clear()
        self.textEdit_Descrip.setText('')
        self.textEdit_Base.setText('') 
        self.comboX.clear()
        self.comboY.clear()
        self.comboEtat.clear()
        filePath, _  = QtWidgets.QFileDialog.getOpenFileName(self, 'Open CSV', 'HOME', 'CSV(*.csv)')
        if filePath != "":
            print("Direction", filePath)
            self.df = pd.read_csv(str(filePath))
            afficher = "Description de la Base: \n"+str(self.df.describe())
            self.textEdit_Base.setText(afficher)
            # print(self.df)
            self.comboX.addItems(list(self.df.columns.values))
            self.comboY.addItems(list(self.df.columns.values))
            self.comboEtat.addItems(list(self.df.columns.values)) 
                        
########################################################################
      
    def maFenetre(self):            
        self.setFixedSize(1200,700)
        # self.setWindowIcon(QIcon('chat.png'))     
  

def main():            
    app = QApplication(sys.argv)
    window = MyProject()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
        
    
