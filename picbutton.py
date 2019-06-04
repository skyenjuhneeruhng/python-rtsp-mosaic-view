from PyQt5 import QtCore, QtGui, QtWidgets

PIC_WIDTH = 30
PIC_HEIGHT = 30
# image button
class PicButton(QtWidgets.QAbstractButton):
    def __init__(self, parent=None):
        super(PicButton, self).__init__(parent)

        self.pix = None

        self.pixNormal = None
        self.pixNormalHover = None
        self.pixPressed = None
        self.pixPressedHover = None

        self.bIsToggle = False

        self.pressed.connect(self.update)
        self.released.connect(self.update)
        self.toggled.connect(self.update)

    #########################################################################################################
    # role : set button mode to toggle & push button
    # param : bToogle : True - toggle mode
    #                   False - push button
    # return : none
    #########################################################################################################
    def setToggle(self, bToggle):
        self.bIsToggle = bToggle

    #########################################################################################################
    # role : set images on button
    # param : pixNormal : pixmap image on normal state
    #         pixNormalHover : pixmap image on normal state when mouse is on button
    #         pixPressed : pixmap image on pressed state
    #         pixPressedHover : pixmap image on pressed state when mouse is on button
    # return : none
    #########################################################################################################
    def setPixmap(self, pixNormal, pixNormalHover, pixPressed, pixPressedHover):
        if not pixNormal or not pixNormalHover or not pixPressed or not pixPressedHover:
            return

        self.pixNormal = pixNormal
        self.pixNormalHover = pixNormalHover
        self.pixPressed = pixPressed
        self.pixPressedHover = pixPressedHover

        self.pix = pixNormal

    #########################################################################################################
    # role : draw picture on button
    # param : paint event
    # return : none
    #########################################################################################################
    def paintEvent(self, event):
        if not self.pix:
            return

        rect = event.rect()
        rectImage = QtCore.QRect()
        rectImage.setWidth(PIC_WIDTH)
        rectImage.setHeight(PIC_HEIGHT)
        rectImage.setLeft(int((rect.width() - PIC_WIDTH) / 2))
        rectImage.setTop(int((rect.height() - PIC_HEIGHT) / 2))

        painter = QtGui.QPainter(self)
        # painter.drawPixmap(rectImage, self.pix)
        painter.drawPixmap(event.rect(), self.pix)

    #########################################################################################################
    # role : event orccured when button was pressed
    # param : mouse event
    # return : none
    #########################################################################################################
    def mousePressEvent(self, QMouseEvent):
        self.pix = self.pixPressed
        self.update()

    #########################################################################################################
    # role : event orccured when button was released
    # param : mouse event
    # return : none
    #########################################################################################################
    def mouseReleaseEvent(self, QMouseEvent):
        if self.isCheckable():
            self.toggle()

            if self.isChecked() == True:
                self.pix = self.pixPressed
            else:
                self.pix = self.pixNormal
        else:
            self.pix = self.pixNormal

        self.update()

    #########################################################################################################
    # role : event orccured when mouse enters in button area
    # param : none
    # return : none
    #########################################################################################################
    def enterEvent(self, event):
        if self.isCheckable():
            if self.isChecked() == True:
                self.pix = self.pixPressedHover
            else:
                self.pix = self.pixNormalHover
        else:
            self.pix = self.pixNormalHover

        self.update()

    #########################################################################################################
    # role : event orccured when mouse leaves button area
    # param : none
    # return : none
    #########################################################################################################
    def leaveEvent(self, event):
        if self.isCheckable():
            if self.isChecked() == True:
                self.pix = self.pixPressed
            else:
                self.pix = self.pixNormal
        else:
            self.pix = self.pixNormal

        self.update()

    #########################################################################################################
    # role : set size
    # param : none
    # return : size of button init state
    #########################################################################################################
    def sizeHint(self):
        return QtCore.QSize(500, 500)