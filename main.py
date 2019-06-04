from PyQt5 import QtCore, QtGui, QtWidgets

from ui_main import Ui_wMain
from video import wVideo
from empty import wEmpty
import csv
import math


class wMain(QtWidgets.QMainWindow, Ui_wMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initVars() # initialize variables
        self.initUI() # initialize user interface

    #########################################################################################################
    # role : initialize ui
    # param : none
    # return : none
    #########################################################################################################
    def initUI(self):
        # toolbar
        self.tbCamera = self.addToolBar('Camera')
        self.tbCamera.setIconSize(QtCore.QSize(32, 32));
        self.tbCamera.setStyleSheet("""	background : grey;
                                    color : white;
                                    border-top-style: outset;
                                    border-top-width: 1px;
                                    border-top-color: #222222;""")

        # add load csv action to toolbar
        self.actLoadCSV = QtWidgets.QAction(QtGui.QIcon('img/loadcsv.png'), '&Load CSV', self)
        self.actLoadCSV.setShortcut('Ctrl+L')
        self.actLoadCSV.setStatusTip('Load CSV')
        self.actLoadCSV.triggered.connect(self.on_act_LoadCSV)
        self.tbCamera.addAction(self.actLoadCSV)

    #########################################################################################################
    # role : initialize variables
    # param : none
    # return : none
    #########################################################################################################
    def initVars(self):
        self.arrayVideo = []  ## array of wVideo widgets
        self.arrayEmpty = []  ## array of wEmpty widgets
        self.arrayUrl = []  ## array of Url
        self.arrayAlias = []  ## array of Alias

    #########################################################################################################
    # role : load csv file included rtsp urls & alias
    # param : none
    # return : none
    #########################################################################################################
    def on_act_LoadCSV(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load CSV", "./",
                                                            "RTSP URL CSV (*.csv)", options=options)

        print("open stream - " + fileName)

        if fileName == None or not fileName:
            return

        # remove previous wVideo widgets
        for i in reversed(range(self.loGrid.count())):
            self.loGrid.itemAt(i).widget().setParent(None)

        # stop, delete all wVideo
        if self.arrayVideo:
            for wVideoItem in self.arrayVideo:
                wVideoItem.stop() # stop playing in wVideo
                del wVideoItem # delete wVideo

        # delete all wEmpty
        if self.arrayEmpty:
            for wEmptyItem in self.arrayEmpty:
                del wEmptyItem

        # clear previous csv url & alias
        self.arrayVideo = []
        self.arrayEmpty = []
        self.arrayUrl = []
        self.arrayAlias = []

        # load new csv file
        self.count = 0
        with open(fileName) as csvUrl:
            csvReader = csv.reader(csvUrl, delimiter=',')
            for row in csvReader:
                self.count += 1
                self.arrayUrl.append(row[0].strip()) # store new url
                self.arrayAlias.append(row[1].strip()) # stor new alias

        print("total count - " + str(self.count))

        # calculate rows & cols of grid
        self.rows, self.cols = self.arrange(self.count)

        index = 0
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if index < self.count:
                    # create new wVidoe
                    wVideoItem = wVideo(self.arrayUrl[index], self.arrayAlias[index])
                    self.arrayVideo.append(wVideoItem)
                    self.loGrid.addWidget(wVideoItem, row, col)
                else:
                    # create new empty area
                    wEmptyItem = wEmpty()
                    self.loGrid.addWidget(wEmptyItem, row, col)

                index += 1

    #########################################################################################################
    # role : main window close event
    # param : close event
    # return : none
    #########################################################################################################
    def closeEvent(self, *args, **kwargs):
        # stop, delete all wVideo
        if self.arrayVideo:
            for wVideoItem in self.arrayVideo:
                ## stop, delete wVideo
                wVideoItem.stop()
                del wVideoItem

    #########################################################################################################
    # role : calculate rows and cols of gridlayout from total rtsp count
    # param : total rtsp count
    # return : rows, cols
    #########################################################################################################
    def arrange(self, count):
        rows = math.sqrt(count)
        cols = rows
        if rows != int(rows):
            rows = round(rows, 0)
            cols += 1

        rows = int(rows)
        cols = int(cols)

        return rows, cols

#########################################################################################################
# role : entry point
#########################################################################################################
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    wMain = wMain()
    wMain.show()
    sys.exit(app.exec_())
