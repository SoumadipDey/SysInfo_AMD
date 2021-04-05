# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainXEDALX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(780, 450)
        MainWindow.setMinimumSize(QSize(780, 450))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(780, 450))
        self.centralwidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.base_frame_layout = QVBoxLayout(self.centralwidget)
        self.base_frame_layout.setObjectName(u"base_frame_layout")
        self.base_frame = QFrame(self.centralwidget)
        self.base_frame.setObjectName(u"base_frame")
        self.base_frame.setMinimumSize(QSize(760, 380))
        self.base_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(self.base_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.title_bar = QFrame(self.base_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_3 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.app_title = QLabel(self.title_bar)
        self.app_title.setObjectName(u"app_title")
        font = QFont()
        font.setFamily(u"Comfortaa")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.app_title.setFont(font)
        self.app_title.setStyleSheet(u"QLabel {\n"
"	color: rgb(205, 205, 205);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"")
        self.app_title.setScaledContents(True)
        self.app_title.setAlignment(Qt.AlignCenter)
        self.app_title.setMargin(0)

        self.horizontalLayout_3.addWidget(self.app_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.control_layout = QFrame(self.title_bar)
        self.control_layout.setObjectName(u"control_layout")
        self.control_layout.setMinimumSize(QSize(150, 0))
        self.control_layout.setMaximumSize(QSize(150, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.control_layout)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.minimize_btn = QPushButton(self.control_layout)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy)
        self.minimize_btn.setMinimumSize(QSize(20, 20))
        self.minimize_btn.setMaximumSize(QSize(20, 20))
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(85, 255, 0,1);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 255, 0,0.7);\n"
"}")

        self.horizontalLayout_4.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.control_layout)
        self.maximize_btn.setObjectName(u"maximize_btn")
        sizePolicy.setHeightForWidth(self.maximize_btn.sizePolicy().hasHeightForWidth())
        self.maximize_btn.setSizePolicy(sizePolicy)
        self.maximize_btn.setMinimumSize(QSize(20, 20))
        self.maximize_btn.setMaximumSize(QSize(20, 20))
        self.maximize_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 170, 0, 0.7);\n"
"}")

        self.horizontalLayout_4.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.control_layout)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(20, 20))
        self.close_btn.setMaximumSize(QSize(20, 20))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 0, 0, 0.7);\n"
"	\n"
"}")

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.horizontalLayout_3.addWidget(self.control_layout)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.base_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color:none;")
        self.horizontalLayout = QHBoxLayout(self.content_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.circularProgressBar_Main_1 = QFrame(self.content_bar)
        self.circularProgressBar_Main_1.setObjectName(u"circularProgressBar_Main_1")
        sizePolicy.setHeightForWidth(self.circularProgressBar_Main_1.sizePolicy().hasHeightForWidth())
        self.circularProgressBar_Main_1.setSizePolicy(sizePolicy)
        self.circularProgressBar_Main_1.setMinimumSize(QSize(240, 240))
        self.circularProgressBar_Main_1.setMaximumSize(QSize(240, 240))
        self.circularProgressBar_Main_1.setStyleSheet(u"background-color:none;")
        self.circularProgressBar_Main_1.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_1.setFrameShadow(QFrame.Raised)
        self.circularBg_CPU = QFrame(self.circularProgressBar_Main_1)
        self.circularBg_CPU.setObjectName(u"circularBg_CPU")
        self.circularBg_CPU.setGeometry(QRect(10, 10, 220, 220))
        sizePolicy.setHeightForWidth(self.circularBg_CPU.sizePolicy().hasHeightForWidth())
        self.circularBg_CPU.setSizePolicy(sizePolicy)
        self.circularBg_CPU.setMinimumSize(QSize(220, 220))
        self.circularBg_CPU.setMaximumSize(QSize(220, 220))
        self.circularBg_CPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_CPU.setFrameShape(QFrame.StyledPanel)
        self.circularBg_CPU.setFrameShadow(QFrame.Raised)
        self.circularProgress_CPU = QFrame(self.circularProgressBar_Main_1)
        self.circularProgress_CPU.setObjectName(u"circularProgress_CPU")
        self.circularProgress_CPU.setGeometry(QRect(10, 10, 220, 220))
        sizePolicy.setHeightForWidth(self.circularProgress_CPU.sizePolicy().hasHeightForWidth())
        self.circularProgress_CPU.setSizePolicy(sizePolicy)
        self.circularProgress_CPU.setMinimumSize(QSize(220, 220))
        self.circularProgress_CPU.setMaximumSize(QSize(220, 220))
        self.circularProgress_CPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.799 rgba(255, 0, 127, 0), stop:0.800 rgba(85, 170, 255, 255));\n"
"}\n"
"")
        self.circularProgress_CPU.setFrameShape(QFrame.StyledPanel)
        self.circularProgress_CPU.setFrameShadow(QFrame.Raised)
        self.circularContainer_CPU = QFrame(self.circularProgressBar_Main_1)
        self.circularContainer_CPU.setObjectName(u"circularContainer_CPU")
        self.circularContainer_CPU.setGeometry(QRect(25, 25, 190, 190))
        sizePolicy.setHeightForWidth(self.circularContainer_CPU.sizePolicy().hasHeightForWidth())
        self.circularContainer_CPU.setSizePolicy(sizePolicy)
        self.circularContainer_CPU.setMinimumSize(QSize(190, 190))
        self.circularContainer_CPU.setMaximumSize(QSize(190, 190))
        self.circularContainer_CPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgb(58, 58, 102);\n"
"	border: 1px solid rgba(85, 170, 255, 255);\n"
"}")
        self.circularContainer_CPU.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_CPU.setFrameShadow(QFrame.Raised)
        self.container_layout_cpu = QFrame(self.circularContainer_CPU)
        self.container_layout_cpu.setObjectName(u"container_layout_cpu")
        self.container_layout_cpu.setGeometry(QRect(30, 30, 130, 130))
        self.container_layout_cpu.setMinimumSize(QSize(130, 130))
        self.container_layout_cpu.setMaximumSize(QSize(130, 130))
        self.container_layout_cpu.setStyleSheet(u"border:none;")
        self.verticalLayout_3 = QVBoxLayout(self.container_layout_cpu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title_label_cpu = QLabel(self.container_layout_cpu)
        self.title_label_cpu.setObjectName(u"title_label_cpu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label_cpu.sizePolicy().hasHeightForWidth())
        self.title_label_cpu.setSizePolicy(sizePolicy1)
        self.title_label_cpu.setMinimumSize(QSize(0, 22))
        self.title_label_cpu.setMaximumSize(QSize(16777215, 22))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.title_label_cpu.setFont(font1)
        self.title_label_cpu.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.title_label_cpu.setScaledContents(True)
        self.title_label_cpu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.title_label_cpu)

        self.usage_label_cpu = QLabel(self.container_layout_cpu)
        self.usage_label_cpu.setObjectName(u"usage_label_cpu")
        self.usage_label_cpu.setMinimumSize(QSize(0, 40))
        self.usage_label_cpu.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamily(u"MS Sans Serif")
        font2.setPointSize(28)
        font2.setBold(True)
        font2.setWeight(75)
        self.usage_label_cpu.setFont(font2)
        self.usage_label_cpu.setStyleSheet(u"color: rgba(85, 170, 255, 255);")
        self.usage_label_cpu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.usage_label_cpu)

        self.freq_label_cpu = QLabel(self.container_layout_cpu)
        self.freq_label_cpu.setObjectName(u"freq_label_cpu")
        self.freq_label_cpu.setMinimumSize(QSize(0, 22))
        self.freq_label_cpu.setMaximumSize(QSize(16777215, 22))
        self.freq_label_cpu.setFont(font1)
        self.freq_label_cpu.setStyleSheet(u"color:#ffffff;")
        self.freq_label_cpu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.freq_label_cpu)

        self.temp_label_cpu = QLabel(self.container_layout_cpu)
        self.temp_label_cpu.setObjectName(u"temp_label_cpu")
        self.temp_label_cpu.setMinimumSize(QSize(0, 15))
        self.temp_label_cpu.setMaximumSize(QSize(16777215, 15))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        self.temp_label_cpu.setFont(font3)
        self.temp_label_cpu.setStyleSheet(u"color: #ffffff;")
        self.temp_label_cpu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.temp_label_cpu)


        self.horizontalLayout.addWidget(self.circularProgressBar_Main_1)

        self.circularProgressBar_Main_2 = QFrame(self.content_bar)
        self.circularProgressBar_Main_2.setObjectName(u"circularProgressBar_Main_2")
        sizePolicy.setHeightForWidth(self.circularProgressBar_Main_2.sizePolicy().hasHeightForWidth())
        self.circularProgressBar_Main_2.setSizePolicy(sizePolicy)
        self.circularProgressBar_Main_2.setMinimumSize(QSize(240, 240))
        self.circularProgressBar_Main_2.setMaximumSize(QSize(240, 240))
        self.circularProgressBar_Main_2.setStyleSheet(u"background-color:none;")
        self.circularProgressBar_Main_2.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_2.setFrameShadow(QFrame.Raised)
        self.circularContainer_GPU = QFrame(self.circularProgressBar_Main_2)
        self.circularContainer_GPU.setObjectName(u"circularContainer_GPU")
        self.circularContainer_GPU.setGeometry(QRect(25, 25, 190, 190))
        sizePolicy.setHeightForWidth(self.circularContainer_GPU.sizePolicy().hasHeightForWidth())
        self.circularContainer_GPU.setSizePolicy(sizePolicy)
        self.circularContainer_GPU.setMinimumSize(QSize(190, 190))
        self.circularContainer_GPU.setMaximumSize(QSize(190, 190))
        self.circularContainer_GPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgba(58, 58, 102,255);\n"
"	border: 1px solid rgba(255,40, 90, 255);\n"
"}")
        self.circularContainer_GPU.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_GPU.setFrameShadow(QFrame.Raised)
        self.container_layout_gpu = QFrame(self.circularContainer_GPU)
        self.container_layout_gpu.setObjectName(u"container_layout_gpu")
        self.container_layout_gpu.setGeometry(QRect(30, 30, 130, 130))
        self.container_layout_gpu.setMinimumSize(QSize(130, 130))
        self.container_layout_gpu.setMaximumSize(QSize(130, 130))
        self.container_layout_gpu.setStyleSheet(u"border:none;")
        self.verticalLayout_5 = QVBoxLayout(self.container_layout_gpu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.title_label_gpu = QLabel(self.container_layout_gpu)
        self.title_label_gpu.setObjectName(u"title_label_gpu")
        sizePolicy1.setHeightForWidth(self.title_label_gpu.sizePolicy().hasHeightForWidth())
        self.title_label_gpu.setSizePolicy(sizePolicy1)
        self.title_label_gpu.setMinimumSize(QSize(0, 22))
        self.title_label_gpu.setMaximumSize(QSize(16777215, 22))
        self.title_label_gpu.setFont(font1)
        self.title_label_gpu.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.title_label_gpu.setScaledContents(True)
        self.title_label_gpu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.title_label_gpu)

        self.usage_label_gpu = QLabel(self.container_layout_gpu)
        self.usage_label_gpu.setObjectName(u"usage_label_gpu")
        self.usage_label_gpu.setMinimumSize(QSize(0, 40))
        self.usage_label_gpu.setMaximumSize(QSize(16777215, 40))
        self.usage_label_gpu.setFont(font2)
        self.usage_label_gpu.setStyleSheet(u"color: rgba(255, 40, 90, 255);")
        self.usage_label_gpu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.usage_label_gpu)

        self.freq_label_gpu = QLabel(self.container_layout_gpu)
        self.freq_label_gpu.setObjectName(u"freq_label_gpu")
        self.freq_label_gpu.setMinimumSize(QSize(0, 22))
        self.freq_label_gpu.setMaximumSize(QSize(16777215, 22))
        self.freq_label_gpu.setFont(font1)
        self.freq_label_gpu.setStyleSheet(u"color:#ffffff;")
        self.freq_label_gpu.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.freq_label_gpu)

        self.temp_label_gpu = QLabel(self.container_layout_gpu)
        self.temp_label_gpu.setObjectName(u"temp_label_gpu")
        self.temp_label_gpu.setMinimumSize(QSize(0, 15))
        self.temp_label_gpu.setMaximumSize(QSize(16777215, 15))
        self.temp_label_gpu.setFont(font3)
        self.temp_label_gpu.setStyleSheet(u"color: #ffffff;")

        self.verticalLayout_5.addWidget(self.temp_label_gpu)

        self.circularProgress_GPU = QFrame(self.circularProgressBar_Main_2)
        self.circularProgress_GPU.setObjectName(u"circularProgress_GPU")
        self.circularProgress_GPU.setGeometry(QRect(10, 10, 220, 220))
        sizePolicy.setHeightForWidth(self.circularProgress_GPU.sizePolicy().hasHeightForWidth())
        self.circularProgress_GPU.setSizePolicy(sizePolicy)
        self.circularProgress_GPU.setMinimumSize(QSize(220, 220))
        self.circularProgress_GPU.setMaximumSize(QSize(220, 220))
        self.circularProgress_GPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.799 rgba(255, 0, 127, 0), stop:0.800 rgba(255, 40, 90, 255));\n"
"}\n"
"")
        self.circularProgress_GPU.setFrameShape(QFrame.StyledPanel)
        self.circularProgress_GPU.setFrameShadow(QFrame.Raised)
        self.circularBg_GPU = QFrame(self.circularProgressBar_Main_2)
        self.circularBg_GPU.setObjectName(u"circularBg_GPU")
        self.circularBg_GPU.setGeometry(QRect(10, 10, 220, 220))
        sizePolicy.setHeightForWidth(self.circularBg_GPU.sizePolicy().hasHeightForWidth())
        self.circularBg_GPU.setSizePolicy(sizePolicy)
        self.circularBg_GPU.setMinimumSize(QSize(220, 220))
        self.circularBg_GPU.setMaximumSize(QSize(220, 220))
        self.circularBg_GPU.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_GPU.setFrameShape(QFrame.StyledPanel)
        self.circularBg_GPU.setFrameShadow(QFrame.Raised)
        self.circularBg_GPU.raise_()
        self.circularProgress_GPU.raise_()
        self.circularContainer_GPU.raise_()

        self.horizontalLayout.addWidget(self.circularProgressBar_Main_2)

        self.circularProgressBar_Main_3 = QFrame(self.content_bar)
        self.circularProgressBar_Main_3.setObjectName(u"circularProgressBar_Main_3")
        sizePolicy.setHeightForWidth(self.circularProgressBar_Main_3.sizePolicy().hasHeightForWidth())
        self.circularProgressBar_Main_3.setSizePolicy(sizePolicy)
        self.circularProgressBar_Main_3.setMinimumSize(QSize(240, 240))
        self.circularProgressBar_Main_3.setMaximumSize(QSize(240, 240))
        self.circularProgressBar_Main_3.setStyleSheet(u"background-color:none;")
        self.circularProgressBar_Main_3.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar_Main_3.setFrameShadow(QFrame.Raised)
        self.circularProgress_RAM = QFrame(self.circularProgressBar_Main_3)
        self.circularProgress_RAM.setObjectName(u"circularProgress_RAM")
        self.circularProgress_RAM.setGeometry(QRect(10, 10, 220, 220))
        sizePolicy.setHeightForWidth(self.circularProgress_RAM.sizePolicy().hasHeightForWidth())
        self.circularProgress_RAM.setSizePolicy(sizePolicy)
        self.circularProgress_RAM.setMinimumSize(QSize(220, 220))
        self.circularProgress_RAM.setMaximumSize(QSize(220, 220))
        self.circularProgress_RAM.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.799 rgba(255, 0, 127, 0), stop:0.800 rgba(170, 0, 255, 255));\n"
"}\n"
"")
        self.circularProgress_RAM.setFrameShape(QFrame.StyledPanel)
        self.circularProgress_RAM.setFrameShadow(QFrame.Raised)
        self.circularBg_RAM = QFrame(self.circularProgressBar_Main_3)
        self.circularBg_RAM.setObjectName(u"circularBg_RAM")
        self.circularBg_RAM.setGeometry(QRect(10, 10, 220, 220))
        sizePolicy.setHeightForWidth(self.circularBg_RAM.sizePolicy().hasHeightForWidth())
        self.circularBg_RAM.setSizePolicy(sizePolicy)
        self.circularBg_RAM.setMinimumSize(QSize(220, 220))
        self.circularBg_RAM.setMaximumSize(QSize(220, 220))
        self.circularBg_RAM.setStyleSheet(u"QFrame{\n"
"	border-radius: 110px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_RAM.setFrameShape(QFrame.StyledPanel)
        self.circularBg_RAM.setFrameShadow(QFrame.Raised)
        self.circularContainer_RAM = QFrame(self.circularProgressBar_Main_3)
        self.circularContainer_RAM.setObjectName(u"circularContainer_RAM")
        self.circularContainer_RAM.setGeometry(QRect(25, 25, 190, 190))
        sizePolicy.setHeightForWidth(self.circularContainer_RAM.sizePolicy().hasHeightForWidth())
        self.circularContainer_RAM.setSizePolicy(sizePolicy)
        self.circularContainer_RAM.setMinimumSize(QSize(190, 190))
        self.circularContainer_RAM.setMaximumSize(QSize(190, 190))
        self.circularContainer_RAM.setStyleSheet(u"QFrame{\n"
"	border-radius: 95px;	\n"
"	background-color: rgba(58, 58, 102,255);\n"
"	border: 1px solid rgba(170,0, 255, 255);\n"
"}")
        self.circularContainer_RAM.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_RAM.setFrameShadow(QFrame.Raised)
        self.container_layout_ram = QFrame(self.circularContainer_RAM)
        self.container_layout_ram.setObjectName(u"container_layout_ram")
        self.container_layout_ram.setGeometry(QRect(30, 30, 130, 130))
        self.container_layout_ram.setMinimumSize(QSize(130, 130))
        self.container_layout_ram.setMaximumSize(QSize(130, 130))
        self.container_layout_ram.setStyleSheet(u"border:none;")
        self.verticalLayout_6 = QVBoxLayout(self.container_layout_ram)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.title_label_ram = QLabel(self.container_layout_ram)
        self.title_label_ram.setObjectName(u"title_label_ram")
        sizePolicy1.setHeightForWidth(self.title_label_ram.sizePolicy().hasHeightForWidth())
        self.title_label_ram.setSizePolicy(sizePolicy1)
        self.title_label_ram.setMinimumSize(QSize(0, 22))
        self.title_label_ram.setMaximumSize(QSize(16777215, 22))
        self.title_label_ram.setFont(font1)
        self.title_label_ram.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.title_label_ram.setScaledContents(True)
        self.title_label_ram.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.title_label_ram)

        self.usage_label_ram = QLabel(self.container_layout_ram)
        self.usage_label_ram.setObjectName(u"usage_label_ram")
        self.usage_label_ram.setMinimumSize(QSize(0, 40))
        self.usage_label_ram.setMaximumSize(QSize(16777215, 40))
        self.usage_label_ram.setFont(font2)
        self.usage_label_ram.setStyleSheet(u"color: rgba(170, 0, 255, 255);")
        self.usage_label_ram.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.usage_label_ram)

        self.usedSize_label_ram = QLabel(self.container_layout_ram)
        self.usedSize_label_ram.setObjectName(u"usedSize_label_ram")
        self.usedSize_label_ram.setMinimumSize(QSize(0, 22))
        self.usedSize_label_ram.setMaximumSize(QSize(16777215, 22))
        self.usedSize_label_ram.setFont(font1)
        self.usedSize_label_ram.setStyleSheet(u"color:#ffffff;")
        self.usedSize_label_ram.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.usedSize_label_ram)

        self.totalSize_label_ram = QLabel(self.container_layout_ram)
        self.totalSize_label_ram.setObjectName(u"totalSize_label_ram")
        self.totalSize_label_ram.setMinimumSize(QSize(0, 15))
        self.totalSize_label_ram.setMaximumSize(QSize(16777215, 15))
        self.totalSize_label_ram.setFont(font3)
        self.totalSize_label_ram.setStyleSheet(u"color: #ffffff;")
        self.totalSize_label_ram.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.totalSize_label_ram)

        self.circularBg_RAM.raise_()
        self.circularProgress_RAM.raise_()
        self.circularContainer_RAM.raise_()

        self.horizontalLayout.addWidget(self.circularProgressBar_Main_3)


        self.verticalLayout.addWidget(self.content_bar)

        self.specs_bar = QFrame(self.base_frame)
        self.specs_bar.setObjectName(u"specs_bar")
        self.specs_bar.setMaximumSize(QSize(16777215, 100))
        self.specs_bar.setSizeIncrement(QSize(0, 100))
        self.specs_bar.setStyleSheet(u"background-color:none;")
        self.horizontalLayout_2 = QHBoxLayout(self.specs_bar)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.cpu_specifications = QFrame(self.specs_bar)
        self.cpu_specifications.setObjectName(u"cpu_specifications")
        self.cpu_specifications.setStyleSheet(u"QFrame{\n"
"	border-radius: 5px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"	color: #ffffff;\n"
"}")
        self.cpu_specs = QHBoxLayout(self.cpu_specifications)
        self.cpu_specs.setObjectName(u"cpu_specs")
        self.name_freq_cpu = QFrame(self.cpu_specifications)
        self.name_freq_cpu.setObjectName(u"name_freq_cpu")
        self.name_freq_cpu.setStyleSheet(u"background-color:none;")
        self.verticalLayout_8 = QVBoxLayout(self.name_freq_cpu)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_cpu_name = QLabel(self.name_freq_cpu)
        self.label_cpu_name.setObjectName(u"label_cpu_name")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        self.label_cpu_name.setFont(font4)
        self.label_cpu_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_cpu_name)

        self.label__max_cpu_freq = QLabel(self.name_freq_cpu)
        self.label__max_cpu_freq.setObjectName(u"label__max_cpu_freq")
        self.label__max_cpu_freq.setFont(font4)
        self.label__max_cpu_freq.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label__max_cpu_freq)


        self.cpu_specs.addWidget(self.name_freq_cpu)

        self.cores_cpu = QFrame(self.cpu_specifications)
        self.cores_cpu.setObjectName(u"cores_cpu")
        self.cores_cpu.setStyleSheet(u"background-color: none;")
        self.verticalLayout_7 = QVBoxLayout(self.cores_cpu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_physical_cores = QLabel(self.cores_cpu)
        self.label_physical_cores.setObjectName(u"label_physical_cores")
        self.label_physical_cores.setFont(font4)
        self.label_physical_cores.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_physical_cores)

        self.label_logical_cores = QLabel(self.cores_cpu)
        self.label_logical_cores.setObjectName(u"label_logical_cores")
        self.label_logical_cores.setFont(font4)
        self.label_logical_cores.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_logical_cores)


        self.cpu_specs.addWidget(self.cores_cpu)


        self.horizontalLayout_2.addWidget(self.cpu_specifications)

        self.gpu_specifications = QFrame(self.specs_bar)
        self.gpu_specifications.setObjectName(u"gpu_specifications")
        self.gpu_specifications.setStyleSheet(u"QFrame{\n"
"	border-radius: 5px;	\n"
"	background-color: rgba(85, 85, 127, 100);\n"
"	color: #ffffff;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.gpu_specifications)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.name_freq_gpu = QFrame(self.gpu_specifications)
        self.name_freq_gpu.setObjectName(u"name_freq_gpu")
        self.name_freq_gpu.setStyleSheet(u"background-color:none;")
        self.verticalLayout_10 = QVBoxLayout(self.name_freq_gpu)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_gpu_name = QLabel(self.name_freq_gpu)
        self.label_gpu_name.setObjectName(u"label_gpu_name")
        self.label_gpu_name.setFont(font4)
        self.label_gpu_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_gpu_name)

        self.label_gpu_max_freq = QLabel(self.name_freq_gpu)
        self.label_gpu_max_freq.setObjectName(u"label_gpu_max_freq")
        self.label_gpu_max_freq.setFont(font4)
        self.label_gpu_max_freq.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_gpu_max_freq)


        self.horizontalLayout_5.addWidget(self.name_freq_gpu)

        self.memory_mclock_gpu = QFrame(self.gpu_specifications)
        self.memory_mclock_gpu.setObjectName(u"memory_mclock_gpu")
        self.memory_mclock_gpu.setStyleSheet(u"background-color:none;")
        self.verticalLayout_9 = QVBoxLayout(self.memory_mclock_gpu)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_gpu_max_vram = QLabel(self.memory_mclock_gpu)
        self.label_gpu_max_vram.setObjectName(u"label_gpu_max_vram")
        self.label_gpu_max_vram.setFont(font4)
        self.label_gpu_max_vram.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_gpu_max_vram)

        self.label_gpy_mem_freq = QLabel(self.memory_mclock_gpu)
        self.label_gpy_mem_freq.setObjectName(u"label_gpy_mem_freq")
        self.label_gpy_mem_freq.setFont(font4)
        self.label_gpy_mem_freq.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_gpy_mem_freq)


        self.horizontalLayout_5.addWidget(self.memory_mclock_gpu)


        self.horizontalLayout_2.addWidget(self.gpu_specifications)


        self.verticalLayout.addWidget(self.specs_bar)

        self.horizontalFrame = QFrame(self.base_frame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 20))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 20))
        self.horizontalFrame.setStyleSheet(u"background-color:none;")
        self.horizontalFrame.setFrameShape(QFrame.StyledPanel)
        self.horizontalFrame.setFrameShadow(QFrame.Plain)
        self.stretch_bar = QHBoxLayout(self.horizontalFrame)
        self.stretch_bar.setSpacing(0)
        self.stretch_bar.setObjectName(u"stretch_bar")
        self.stretch_bar.setContentsMargins(1, 1, 1, 1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.stretch_bar.addItem(self.horizontalSpacer_2)

        self.frame_grip = QFrame(self.horizontalFrame)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 20))
        self.frame_grip.setMaximumSize(QSize(30, 20))
        self.frame_grip.setStyleSheet(u"padding:5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.stretch_bar.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.horizontalFrame)


        self.base_frame_layout.addWidget(self.base_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Sys</span>Info</p></body></html>", None))
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
        self.title_label_cpu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CPU</span> Usage</p></body></html>", None))
        self.usage_label_cpu.setText(QCoreApplication.translate("MainWindow", u"20%", None))
        self.freq_label_cpu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Freq: </span>3000 MHz</p></body></html>", None))
        self.temp_label_cpu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperature:</span> 45 \u00b0C</p></body></html>", None))
        self.title_label_gpu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">GPU</span> Usage</p></body></html>", None))
        self.usage_label_gpu.setText(QCoreApplication.translate("MainWindow", u"20%", None))
        self.freq_label_gpu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Freq: </span>540 MHz</p></body></html>", None))
        self.temp_label_gpu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperature:</span> 51 \u00b0C</p></body></html>", None))
        self.title_label_ram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">RAM</span> Usage</p></body></html>", None))
        self.usage_label_ram.setText(QCoreApplication.translate("MainWindow", u"20%", None))
        self.usedSize_label_ram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Used:</span> 1.6 GB</p></body></html>", None))
        self.totalSize_label_ram.setText(QCoreApplication.translate("MainWindow", u"Total: 8 GB", None))
        self.label_cpu_name.setText(QCoreApplication.translate("MainWindow", u"<CPU NAME>", None))
        self.label__max_cpu_freq.setText(QCoreApplication.translate("MainWindow", u"Max frequency: 3500 MHz", None))
        self.label_physical_cores.setText(QCoreApplication.translate("MainWindow", u"Physical Processors: 6", None))
        self.label_logical_cores.setText(QCoreApplication.translate("MainWindow", u"Logical Processors: 12", None))
        self.label_gpu_name.setText(QCoreApplication.translate("MainWindow", u"<GPU NAME>", None))
        self.label_gpu_max_freq.setText(QCoreApplication.translate("MainWindow", u"Max Frequency: 2700 MHz", None))
        self.label_gpu_max_vram.setText(QCoreApplication.translate("MainWindow", u"Total VRAM: 4 GB", None))
        self.label_gpy_mem_freq.setText(QCoreApplication.translate("MainWindow", u"Memory Freq: 1700 MHz", None))
    # retranslateUi

