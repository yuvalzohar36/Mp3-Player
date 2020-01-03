
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os 
import pygame



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 593)
        self.listofsongs=[]
        self.volume=0.3
        self.index=0
        self.clicktimes=0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(180, -10, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.msg = QtWidgets.QLabel(self.centralwidget)
        self.msg.setGeometry(QtCore.QRect(310, 420, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.msg.setFont(font)
        self.msg.setObjectName("msg")
        self.msg.hide()
        self.ChooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseButton.setGeometry(QtCore.QRect(10, 400, 271, 41))
        self.ChooseButton.setObjectName("ChooseButton")
        self.ChooseButton.clicked.connect(self.choosedirectory)
        self.PreviousButton = QtWidgets.QPushButton(self.centralwidget)
        self.PreviousButton.setGeometry(QtCore.QRect(10, 480, 121, 41))
        self.PreviousButton.setObjectName("PreviousButton")
        self.PreviousButton.clicked.connect(self.previous_song)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setGeometry(QtCore.QRect(490, 480, 101, 41))
        self.NextButton.setObjectName("NextButton")
        self.NextButton.clicked.connect(self.next_song)
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(220, 480, 131, 41))
        self.StopButton.setObjectName("StopButton")
        self.StopButton.clicked.connect(self.play)
        self.SongList = QtWidgets.QListWidget(self.centralwidget)
        self.SongList.setGeometry(QtCore.QRect(10, 90, 271, 281))
        self.SongList.setObjectName("SongList")









        self.PlusVolumeButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlusVolumeButton.setGeometry(QtCore.QRect(530, 320, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PlusVolumeButton.setFont(font)
        self.PlusVolumeButton.setObjectName("PlusVolumeButton")
        self.PlusVolumeButton.clicked.connect(self.plusfunc)
        self.MinusVolumeButton = QtWidgets.QPushButton(self.centralwidget)
        self.MinusVolumeButton.setGeometry(QtCore.QRect(530, 400, 31, 31))
        self.MinusVolumeButton.clicked.connect(self.minusfunc)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MinusVolumeButton.setFont(font)
        self.MinusVolumeButton.setObjectName("MinusVolumeButton")
        self.CurrentVolume = QtWidgets.QLabel(self.centralwidget)
        self.CurrentVolume.setGeometry(QtCore.QRect(535, 360, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CurrentVolume.setFont(font)
        self.CurrentVolume.setObjectName("CurrentVolume")
        




        self.ForwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.ForwardButton.setGeometry(QtCore.QRect(440, 200, 100, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ForwardButton.setFont(font)
        self.ForwardButton.setObjectName("ForwardButton")
        self.ForwardButton.clicked.connect(self.moveforward)
        self.BackwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackwardButton.setGeometry(QtCore.QRect(320, 200, 100, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackwardButton.setFont(font)
        self.BackwardButton.setObjectName("BackwardButton")
        self.BackwardButton.clicked.connect(self.movebackward)









        
    

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.playinglabel = QtWidgets.QLabel(self.centralwidget)
        self.playinglabel.setGeometry(QtCore.QRect(300, 0, 250, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(40)
        self.playinglabel.setFont(font)
        self.playinglabel.setObjectName("playinglabel")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def plusfunc(self):
        if len(self.listofsongs)==0:
            self.msg.show()
        if len(self.listofsongs)>0 :
            self.msg.hide()
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.04)
            print(str(pygame.mixer.music.get_volume()))
            self.CurrentVolume.setText((str(int(((pygame.mixer.music.get_volume()*100))))))
            #print(pygame.mixer.music.get_pos())
            #if pygame.mixer.music.get_busy()==True:
            #    pygame.mixer.music.set_pos((pygame.mixer.music.get_pos()+2000)/1000)
            '''elif len(self.listofsongs)>self.index+1:
                self.index+=1
                pygame.mixer.music.load(self.listofsongs[self.index])
                pygame.mixer.music.play()
                self.playinglabel.setText("Playing Now \n" +self.listofsongs[self.index])'''
    def moveforward(self):
        if len(self.listofsongs)>0 :
                self.msg.hide()
                if pygame.mixer.music.get_busy()==True:
                    pygame.mixer.music.set_pos((pygame.mixer.music.get_pos()+2000)/1000)
                elif len(self.listofsongs)>self.index+1:
                    self.index+=1
                    pygame.mixer.music.load(self.listofsongs[self.index])
                    pygame.mixer.music.play()
                    self.playinglabel.setText("Playing Now \n" +self.listofsongs[self.index])
                    self.SongList.item(self.index).setSelected(True)
                elif len(self.listofsongs)==self.index+1:
                    self.index=0
                    pygame.mixer.music.load(self.listofsongs[self.index])
                    pygame.mixer.music.play()
                    self.playinglabel.setText("Playing Now \n" +self.listofsongs[self.index])
                    self.SongList.item(self.index).setSelected(True)


    def movebackward(self):
         if len(self.listofsongs)>0 :
                self.msg.hide()
                if pygame.mixer.music.get_busy()==True:
                    pygame.mixer.music.set_pos((pygame.mixer.music.get_pos()-2000)/1000)
                elif self.index>=1:
                    self.index-=1
                    pygame.mixer.music.load(self.listofsongs[self.index])
                    pygame.mixer.music.play()
                    self.playinglabel.setText("Playing Now \n" +self.listofsongs[self.index])
                    self.SongList.item(self.index).setSelected(True)





    def minusfunc(self):
        if len(self.listofsongs)==0:
            self.msg.show()
        if len(self.listofsongs)>0 :
            self.msg.hide()
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.04)
            print(str(pygame.mixer.music.get_volume()))
            self.CurrentVolume.setText((str(int(((pygame.mixer.music.get_volume()*100))))))


        
    def play(self):
            if len(self.listofsongs)==0:
                self.msg.show()
            if len(self.listofsongs)>0 :
                self.msg.hide()
                self.clicktimes+=1
                if self.clicktimes%2==0:
                    pygame.mixer.music.pause()
                if self.clicktimes%2!=0:
                    pygame.mixer.music.unpause()
                
    def next_song(self):  
            if len(self.listofsongs)==0:
                self.msg.show()

            if len(self.listofsongs)>self.index+1:
                self.msg.hide()
                self.index+=1
                pygame.mixer.init()
                pygame.mixer.music.load(self.listofsongs[self.index])
                self.SongList.item(self.index).setSelected(True)
                pygame.mixer.music.play()
                self.playinglabel.setText("Playing Now \n" +self.listofsongs[self.index])
          
    def previous_song(self):
            if len(self.listofsongs)==0:
                self.msg.show()
            if self.index>=1:
                self.msg.hide()
                self.index-=1
                pygame.mixer.init()
                pygame.mixer.music.load(self.listofsongs[self.index])
                self.SongList.item(self.index).setSelected(True)
                pygame.mixer.music.play()
                self.playinglabel.setText("Playing Now \n" +self.listofsongs[self.index])


    def choosedirectory(self):
        self.dialog = QtWidgets.QFileDialog()
        folder_path = self.dialog.getExistingDirectory(None, "Select Folder")
        os.chdir(folder_path)
        for files in os.listdir(folder_path):
            if files.endswith(".mp3"):
                self.listofsongs.append(files)
                item = QtWidgets.QListWidgetItem()
                self.SongList.addItem(item)
                item.setText(files)
        self.msg.hide()
        pygame.mixer.init()
        pygame.mixer.music.load(self.listofsongs[self.index])
        self.SongList.item(self.index).setSelected(True)
        #print(os.path.getsize(self.listofsongs[self.index]))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(self.volume)
        self.playinglabel.setText("Playing Now \n" +self.listofsongs[self.index])
        print(str(pygame.mixer.music.get_volume()))
        self.CurrentVolume.setText((str(int(((pygame.mixer.music.get_volume()*100))))))



                




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mp3 Player ---- @yuvalzohar"))
        self.Title.setText(_translate("MainWindow", "Mp3 Player"))
        self.PreviousButton.setText(_translate("MainWindow", "Previous Song"))
        self.NextButton.setText(_translate("MainWindow", "Next Song"))
        self.StopButton.setText(_translate("MainWindow", "Play | Pause"))
        self.ChooseButton.setText(_translate("MainWindow", "Choose Directory"))
        #self.playinglabel.setText(_translate("MainWindow", "Playing now : \n " + " -------"))
        self.msg.setText(_translate("MainWindow", "You must choose directory first !"))
        self.PlusVolumeButton.setText(_translate("MainWindow", "+ "))
        self.MinusVolumeButton.setText(_translate("MainWindow", "-"))
        self.ForwardButton.setText(_translate("MainWindow", "Forward"))
        self.BackwardButton.setText(_translate("MainWindow", "Backward"))
        self.CurrentVolume.setText(_translate("MainWindow", "40"))
        __sortingEnabled = self.SongList.isSortingEnabled()
        self.SongList.setSortingEnabled(False)
        self.SongList.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
