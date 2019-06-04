from PyQt5 import QtCore, QtGui, QtWidgets

from ui_video import Ui_wVideo
import threading
import sys
import vlc
import datetime
import time


class wVideo(QtWidgets.QWidget, Ui_wVideo):
    def __init__(self, url, alias):
        super().__init__()
        self.setupUi(self)

        ## init vairables
        self.url = url # rtsp streaming url
        self.alias = alias # alias to rtsp stream url

        self.procFFMpeg = None # process to ffmpeg for recording
        self.fileName = "" # recorded file name from ffmpeg
        self.bConnectedAlertShown = False # check alert state when rtsp reconnected

        # initialize user interface
        self.initUI()

        ## start streaming
        self.openStreaming()

        ## start thread for monitoring disconnected state
        self.bStopThread = False
        self.thread = threading.Thread(target=self.thread_loop)
        self.thread.start()

    #########################################################################################################
    # role : initialize ui
    # param : none
    # return : none
    #########################################################################################################
    def initUI(self):
        # set images on play & pause button
        self.btnResume.setPixmap(
            QtGui.QPixmap("img/resume_normal.png"),
            QtGui.QPixmap("img/resume_normal_hover.png"),
            QtGui.QPixmap("img/resume_pressed.png"),
            QtGui.QPixmap("img/resume_pressed_hover.png"))
        self.btnResume.setCheckable(True) # set button mode to toggle

        # set images on record button
        self.btnRecord.setPixmap(
            QtGui.QPixmap("img/record_normal.png"),
            QtGui.QPixmap("img/record_normal_hover.png"),
            QtGui.QPixmap("img/record_pressed.png"),
            QtGui.QPixmap("img/record_pressed_hover.png"))
        self.btnRecord.setCheckable(True)# set button mode to toggle

        self.lblAlias.setText(self.alias) # show alias on video

        # creating a basic vlc instance
        self.instance = vlc.Instance()
        # creating an empty vlc media player
        self.mediaplayer = self.instance.media_player_new()

        if sys.platform.startswith('linux'):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.frmVideo.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.frmVideo.winId())

        self.isPaused = False

        ## connect signal / slot
        self.btnResume.toggled.connect(self.on_btn_Resume)
        self.btnRecord.toggled.connect(self.on_btn_Record)

    #########################################################################################################
    # role : toggle open & pause
    # param : none
    # return : none
    #########################################################################################################
    def toggleResume(self):
        """Toggle play/pause status
        """
        if self.mediaplayer.is_playing():
            # pause streaming
            self.mediaplayer.pause()
            self.isPaused = True
            self.btnResume.setChecked(True)
        else:
            # resume playing
            if self.mediaplayer.play() == -1:
                self.isPaused = True
                self.btnResume.setChecked(False)
                return

            self.isPaused = False
            self.btnResume.setChecked(False)

    #########################################################################################################
    # role : stop stream playing
    # param : none
    # return : none
    #########################################################################################################
    def stop(self):
        # stop thread
        self.bStopThread = True
        while self.thread.isAlive():
            time.sleep(0.01)

        # stop playing
        self.mediaplayer.stop()
        while self.mediaplayer.is_playing():
            time.sleep(0.01)

        print("stopped - " + self.alias)

    #########################################################################################################
    # role : open streaming
    # param : none
    # return : none
    #########################################################################################################
    def openStreaming(self):
        self.mediaplayer.set_mrl(self.url, "network-caching=300") # set url
        self.mediaplayer.video_set_mouse_input(True) # show mouse on frame
        self.mediaplayer.video_set_key_input(False) # forbiden keyborad event
        self.mediaplayer.audio_set_mute(True)  # mute audio

        # open stream playing
        self.toggleResume()

    #########################################################################################################
    # role : toggle playing stream & pause
    # param : none
    # return : none
    #########################################################################################################
    def on_btn_Resume(self):
        self.toggleResume() # playing & pause

    #########################################################################################################
    # role : check disconnected state of internet & streaming
    # param : none
    # return : none
    #########################################################################################################
    def isAccident(self):
        # when pause event was not occured manually and player is not playing
        if self.isPaused == False and self.mediaplayer.is_playing() == False:
            return True
        return False

    #########################################################################################################
    # role : button toggle event of record button
    # param : bRecord : toggle state
    #                   True : start recording
    #                   False : stop recording
    # return : none
    #########################################################################################################
    def on_btn_Record(self, bRecord):
        if self.isAccident():
            self.btnRecord.setChecked(False)
            print("recording failed due to accident - " + self.alias)

        if bRecord == True:
            ## record start
            # file name to be recorded
            self.fileName = self.alias + datetime.datetime.now().strftime("_%Y%m%d%H%M%S.mp4")

            # process for ffmpeg
            self.procFFMpeg = QtCore.QProcess()
            self.procFFMpeg.setStandardInputFile(self.procFFMpeg.nullDevice())
            self.procFFMpeg.setStandardOutputFile(self.procFFMpeg.nullDevice())
            self.procFFMpeg.setStandardErrorFile(self.procFFMpeg.nullDevice())

            # ffmpeg process finished event
            self.procFFMpeg.finished.connect(self.on_Record_Finished)

            program = "ffmpeg"
            args = ["-i", self.url, "-vcodec", "copy", "-strict", "-2", "-y", self.fileName]

            self.procFFMpeg.setProgram(program)
            self.procFFMpeg.setArguments(args)
            self.procFFMpeg.start()
            self.procFFMpeg.waitForStarted(10000)

            print("started recording - " + self.fileName)
        else:
            # stop recording
            self.procFFMpeg.terminate()
            if not self.procFFMpeg.waitForFinished(10000):
                self.procFFMpeg.kill()

    #########################################################################################################
    # role : recording finished event from ffmpeg process
    # param : none
    # return : none
    #########################################################################################################
    def on_Record_Finished(self):
        self.btnRecord.setChecked(False)
        print("stopped recording - " + self.fileName)

    #########################################################################################################
    # role : loop cycle of thread which monitoring disconnected state
    # param : none
    # return : none
    #########################################################################################################
    def thread_loop(self):
        # check disconnected state
        while True:
            if self.isAccident():
                self.on_Accident()
                self.bConnectedAlertShown = False
            else:
                if self.bConnectedAlertShown == False:
                    print("connected - " + self.alias)

                self.bConnectedAlertShown = True

            if self.bStopThread == True:
                break

            time.sleep(2)

    #########################################################################################################
    # role : event occured on disconneced state
    # param : none
    # return : none
    #########################################################################################################
    def on_Accident(self):
        print("trying connect - " + self.alias)
        # open streaming
        self.openStreaming()
        self.btnResume.setChecked(False)
        self.btnRecord.setChecked(False)
