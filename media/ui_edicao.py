# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EdicaosHMIWJ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import media.resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1255, 809)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none")

        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Titulo = QFrame(Form)
        self.Titulo.setObjectName(u"Titulo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Titulo.sizePolicy().hasHeightForWidth())
        self.Titulo.setSizePolicy(sizePolicy)
        self.Titulo.setMaximumSize(QSize(16777215, 60))
        self.Titulo.setStyleSheet(u"background-color: rgb(109, 49, 162);")
        self.Titulo.setFrameShape(QFrame.StyledPanel)
        self.Titulo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Titulo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_voltar = QPushButton(self.Titulo)
        self.btn_voltar.setObjectName(u"btn_voltar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_voltar.sizePolicy().hasHeightForWidth())
        self.btn_voltar.setSizePolicy(sizePolicy1)
        self.btn_voltar.setMinimumSize(QSize(50, 0))
        self.btn_voltar.setMaximumSize(QSize(50, 16777215))
        self.btn_voltar.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	image: url(:/icons/drop-down-esq.png);\n"
"	padding: 3px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: none;\n"
"	image: url(:/icons/drop-down-esq.png);\n"
"	padding: 1px\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: none;\n"
"	image: url(:/icons/drop-down-esq.png);\n"
"	padding: 2px\n"
"}")
        self.btn_voltar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_voltar)

        self.lb_tituloPrincipal = QLabel(self.Titulo)
        self.lb_tituloPrincipal.setObjectName(u"lb_tituloPrincipal")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(True)
        self.lb_tituloPrincipal.setFont(font)
        self.lb_tituloPrincipal.setStyleSheet(u"color: white;")
        self.lb_tituloPrincipal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_tituloPrincipal)


        self.verticalLayout.addWidget(self.Titulo)

        self.Content = QFrame(Form)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Content)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setStyleSheet(u"QFrame {\n"
"background-color: rgb(238, 233, 243);\n"
"border-right: 1px solid rgb(190, 186, 194);\n"
"}\n"
"\n"
"QLabel {\n"
"border: none;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: rgb(238, 233, 243);\n"
"border:none;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 232, 856))
        self.verticalLayout_27 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 24)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_decreto_titulo = QLabel(self.frame_3)
        self.lb_decreto_titulo.setObjectName(u"lb_decreto_titulo")
        sizePolicy.setHeightForWidth(self.lb_decreto_titulo.sizePolicy().hasHeightForWidth())
        self.lb_decreto_titulo.setSizePolicy(sizePolicy)
        self.lb_decreto_titulo.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.lb_decreto_titulo.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_decreto_titulo)

        self.lb_decreto_info = QLabel(self.frame_3)
        self.lb_decreto_info.setObjectName(u"lb_decreto_info")
        sizePolicy.setHeightForWidth(self.lb_decreto_info.sizePolicy().hasHeightForWidth())
        self.lb_decreto_info.setSizePolicy(sizePolicy)
        self.lb_decreto_info.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.lb_decreto_info.setFont(font2)
        self.lb_decreto_info.setStyleSheet(u"margin-left: 20px")
        self.lb_decreto_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lb_decreto_info)


        self.verticalLayout_27.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_dataDecreto_titulo = QLabel(self.frame_4)
        self.lb_dataDecreto_titulo.setObjectName(u"lb_dataDecreto_titulo")
        sizePolicy.setHeightForWidth(self.lb_dataDecreto_titulo.sizePolicy().hasHeightForWidth())
        self.lb_dataDecreto_titulo.setSizePolicy(sizePolicy)
        self.lb_dataDecreto_titulo.setMaximumSize(QSize(16777215, 20))
        self.lb_dataDecreto_titulo.setFont(font1)

        self.verticalLayout_4.addWidget(self.lb_dataDecreto_titulo)

        self.lb_dataDecreto_info = QLabel(self.frame_4)
        self.lb_dataDecreto_info.setObjectName(u"lb_dataDecreto_info")
        sizePolicy.setHeightForWidth(self.lb_dataDecreto_info.sizePolicy().hasHeightForWidth())
        self.lb_dataDecreto_info.setSizePolicy(sizePolicy)
        self.lb_dataDecreto_info.setMaximumSize(QSize(16777215, 25))
        self.lb_dataDecreto_info.setFont(font2)
        self.lb_dataDecreto_info.setStyleSheet(u"margin-left: 20px")
        self.lb_dataDecreto_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.lb_dataDecreto_info)


        self.verticalLayout_27.addWidget(self.frame_4)

        self.lb_origem_titulo = QLabel(self.scrollAreaWidgetContents)
        self.lb_origem_titulo.setObjectName(u"lb_origem_titulo")
        sizePolicy.setHeightForWidth(self.lb_origem_titulo.sizePolicy().hasHeightForWidth())
        self.lb_origem_titulo.setSizePolicy(sizePolicy)
        self.lb_origem_titulo.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(13)
        font3.setBold(False)
        self.lb_origem_titulo.setFont(font3)
        self.lb_origem_titulo.setStyleSheet(u"margin-left: 5px")

        self.verticalLayout_27.addWidget(self.lb_origem_titulo)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(16777215, 60))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, -1, -1, -1)
        self.lb_origem_orgao_titulo = QLabel(self.frame_5)
        self.lb_origem_orgao_titulo.setObjectName(u"lb_origem_orgao_titulo")
        sizePolicy.setHeightForWidth(self.lb_origem_orgao_titulo.sizePolicy().hasHeightForWidth())
        self.lb_origem_orgao_titulo.setSizePolicy(sizePolicy)
        self.lb_origem_orgao_titulo.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.lb_origem_orgao_titulo.setFont(font4)

        self.verticalLayout_5.addWidget(self.lb_origem_orgao_titulo)

        self.lb_origem_orgao_info = QLabel(self.frame_5)
        self.lb_origem_orgao_info.setObjectName(u"lb_origem_orgao_info")
        sizePolicy.setHeightForWidth(self.lb_origem_orgao_info.sizePolicy().hasHeightForWidth())
        self.lb_origem_orgao_info.setSizePolicy(sizePolicy)
        self.lb_origem_orgao_info.setMaximumSize(QSize(16777215, 25))
        self.lb_origem_orgao_info.setFont(font2)
        self.lb_origem_orgao_info.setStyleSheet(u"margin-left: 20px")
        self.lb_origem_orgao_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.lb_origem_orgao_info)


        self.verticalLayout_27.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, -1, -1, -1)
        self.lb_origem_programa_titulo = QLabel(self.frame_6)
        self.lb_origem_programa_titulo.setObjectName(u"lb_origem_programa_titulo")
        sizePolicy.setHeightForWidth(self.lb_origem_programa_titulo.sizePolicy().hasHeightForWidth())
        self.lb_origem_programa_titulo.setSizePolicy(sizePolicy)
        self.lb_origem_programa_titulo.setMaximumSize(QSize(16777215, 20))
        self.lb_origem_programa_titulo.setFont(font4)

        self.verticalLayout_6.addWidget(self.lb_origem_programa_titulo)

        self.lb_origem_programa_info = QLabel(self.frame_6)
        self.lb_origem_programa_info.setObjectName(u"lb_origem_programa_info")
        sizePolicy.setHeightForWidth(self.lb_origem_programa_info.sizePolicy().hasHeightForWidth())
        self.lb_origem_programa_info.setSizePolicy(sizePolicy)
        self.lb_origem_programa_info.setMaximumSize(QSize(16777215, 40))
        self.lb_origem_programa_info.setFont(font2)
        self.lb_origem_programa_info.setStyleSheet(u"margin-left: 20px")
        self.lb_origem_programa_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_origem_programa_info.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.lb_origem_programa_info)


        self.verticalLayout_27.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, -1, -1, -1)
        self.lb_origem_acao_titulo = QLabel(self.frame_7)
        self.lb_origem_acao_titulo.setObjectName(u"lb_origem_acao_titulo")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_titulo.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_titulo.setSizePolicy(sizePolicy)
        self.lb_origem_acao_titulo.setMaximumSize(QSize(16777215, 20))
        self.lb_origem_acao_titulo.setFont(font4)

        self.verticalLayout_7.addWidget(self.lb_origem_acao_titulo)

        self.lb_origem_acao_info = QLabel(self.frame_7)
        self.lb_origem_acao_info.setObjectName(u"lb_origem_acao_info")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_info.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_info.setSizePolicy(sizePolicy)
        self.lb_origem_acao_info.setMaximumSize(QSize(16777215, 40))
        self.lb_origem_acao_info.setFont(font2)
        self.lb_origem_acao_info.setStyleSheet(u"margin-left: 20px")
        self.lb_origem_acao_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_origem_acao_info.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.lb_origem_acao_info)


        self.verticalLayout_27.addWidget(self.frame_7)

        self.frame_25 = QFrame(self.scrollAreaWidgetContents)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMaximumSize(QSize(16777215, 100))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_25)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(20, -1, -1, -1)
        self.lb_origem_acao_titulo_13 = QLabel(self.frame_25)
        self.lb_origem_acao_titulo_13.setObjectName(u"lb_origem_acao_titulo_13")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_titulo_13.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_titulo_13.setSizePolicy(sizePolicy)
        self.lb_origem_acao_titulo_13.setMaximumSize(QSize(16777215, 20))
        self.lb_origem_acao_titulo_13.setFont(font4)

        self.verticalLayout_29.addWidget(self.lb_origem_acao_titulo_13)

        self.lb_origem_acao_info_13 = QLabel(self.frame_25)
        self.lb_origem_acao_info_13.setObjectName(u"lb_origem_acao_info_13")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_info_13.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_info_13.setSizePolicy(sizePolicy)
        self.lb_origem_acao_info_13.setMaximumSize(QSize(16777215, 40))
        self.lb_origem_acao_info_13.setFont(font2)
        self.lb_origem_acao_info_13.setStyleSheet(u"margin-left: 20px")
        self.lb_origem_acao_info_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_origem_acao_info_13.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.lb_origem_acao_info_13)


        self.verticalLayout_27.addWidget(self.frame_25)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setMaximumSize(QSize(16777215, 100))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_21)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(20, -1, -1, -1)
        self.lb_origem_acao_titulo_3 = QLabel(self.frame_21)
        self.lb_origem_acao_titulo_3.setObjectName(u"lb_origem_acao_titulo_3")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_titulo_3.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_titulo_3.setSizePolicy(sizePolicy)
        self.lb_origem_acao_titulo_3.setMaximumSize(QSize(16777215, 20))
        self.lb_origem_acao_titulo_3.setFont(font4)

        self.verticalLayout_18.addWidget(self.lb_origem_acao_titulo_3)

        self.lb_origem_acao_info_3 = QLabel(self.frame_21)
        self.lb_origem_acao_info_3.setObjectName(u"lb_origem_acao_info_3")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_info_3.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_info_3.setSizePolicy(sizePolicy)
        self.lb_origem_acao_info_3.setMaximumSize(QSize(16777215, 40))
        self.lb_origem_acao_info_3.setFont(font2)
        self.lb_origem_acao_info_3.setStyleSheet(u"margin-left: 20px")
        self.lb_origem_acao_info_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_origem_acao_info_3.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.lb_origem_acao_info_3)


        self.verticalLayout_27.addWidget(self.frame_21)

        self.lb_destino_titulo = QLabel(self.scrollAreaWidgetContents)
        self.lb_destino_titulo.setObjectName(u"lb_destino_titulo")
        sizePolicy.setHeightForWidth(self.lb_destino_titulo.sizePolicy().hasHeightForWidth())
        self.lb_destino_titulo.setSizePolicy(sizePolicy)
        self.lb_destino_titulo.setMaximumSize(QSize(16777215, 30))
        self.lb_destino_titulo.setFont(font3)
        self.lb_destino_titulo.setStyleSheet(u"margin-left: 5px")

        self.verticalLayout_27.addWidget(self.lb_destino_titulo)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMaximumSize(QSize(16777215, 60))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.lb_destino_orgao_titulo = QLabel(self.frame_8)
        self.lb_destino_orgao_titulo.setObjectName(u"lb_destino_orgao_titulo")
        sizePolicy.setHeightForWidth(self.lb_destino_orgao_titulo.sizePolicy().hasHeightForWidth())
        self.lb_destino_orgao_titulo.setSizePolicy(sizePolicy)
        self.lb_destino_orgao_titulo.setMaximumSize(QSize(16777215, 20))
        self.lb_destino_orgao_titulo.setFont(font4)

        self.verticalLayout_8.addWidget(self.lb_destino_orgao_titulo)

        self.lb_destino_orgao_info = QLabel(self.frame_8)
        self.lb_destino_orgao_info.setObjectName(u"lb_destino_orgao_info")
        sizePolicy.setHeightForWidth(self.lb_destino_orgao_info.sizePolicy().hasHeightForWidth())
        self.lb_destino_orgao_info.setSizePolicy(sizePolicy)
        self.lb_destino_orgao_info.setMaximumSize(QSize(16777215, 25))
        self.lb_destino_orgao_info.setFont(font2)
        self.lb_destino_orgao_info.setStyleSheet(u"margin-left: 20px")
        self.lb_destino_orgao_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lb_destino_orgao_info)


        self.verticalLayout_27.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMaximumSize(QSize(16777215, 100))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.lb_destino_acao_titulo = QLabel(self.frame_10)
        self.lb_destino_acao_titulo.setObjectName(u"lb_destino_acao_titulo")
        sizePolicy.setHeightForWidth(self.lb_destino_acao_titulo.sizePolicy().hasHeightForWidth())
        self.lb_destino_acao_titulo.setSizePolicy(sizePolicy)
        self.lb_destino_acao_titulo.setMaximumSize(QSize(16777215, 20))
        self.lb_destino_acao_titulo.setFont(font4)

        self.verticalLayout_10.addWidget(self.lb_destino_acao_titulo)

        self.lb_destino_acao_info = QLabel(self.frame_10)
        self.lb_destino_acao_info.setObjectName(u"lb_destino_acao_info")
        sizePolicy.setHeightForWidth(self.lb_destino_acao_info.sizePolicy().hasHeightForWidth())
        self.lb_destino_acao_info.setSizePolicy(sizePolicy)
        self.lb_destino_acao_info.setMaximumSize(QSize(16777215, 40))
        self.lb_destino_acao_info.setFont(font2)
        self.lb_destino_acao_info.setStyleSheet(u"margin-left: 20px")
        self.lb_destino_acao_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_destino_acao_info.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.lb_destino_acao_info)


        self.verticalLayout_27.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMaximumSize(QSize(16777215, 100))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.lb_destino_programa_titulo = QLabel(self.frame_9)
        self.lb_destino_programa_titulo.setObjectName(u"lb_destino_programa_titulo")
        sizePolicy.setHeightForWidth(self.lb_destino_programa_titulo.sizePolicy().hasHeightForWidth())
        self.lb_destino_programa_titulo.setSizePolicy(sizePolicy)
        self.lb_destino_programa_titulo.setMaximumSize(QSize(16777215, 20))
        self.lb_destino_programa_titulo.setFont(font4)

        self.verticalLayout_9.addWidget(self.lb_destino_programa_titulo)

        self.lb_destino_programa_info = QLabel(self.frame_9)
        self.lb_destino_programa_info.setObjectName(u"lb_destino_programa_info")
        sizePolicy.setHeightForWidth(self.lb_destino_programa_info.sizePolicy().hasHeightForWidth())
        self.lb_destino_programa_info.setSizePolicy(sizePolicy)
        self.lb_destino_programa_info.setMaximumSize(QSize(16777215, 40))
        self.lb_destino_programa_info.setFont(font2)
        self.lb_destino_programa_info.setStyleSheet(u"margin-left: 20px")
        self.lb_destino_programa_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_destino_programa_info.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.lb_destino_programa_info)


        self.verticalLayout_27.addWidget(self.frame_9)

        self.frame_26 = QFrame(self.scrollAreaWidgetContents)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMaximumSize(QSize(16777215, 100))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_26)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(20, -1, -1, -1)
        self.lb_origem_acao_titulo_15 = QLabel(self.frame_26)
        self.lb_origem_acao_titulo_15.setObjectName(u"lb_origem_acao_titulo_15")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_titulo_15.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_titulo_15.setSizePolicy(sizePolicy)
        self.lb_origem_acao_titulo_15.setMaximumSize(QSize(16777215, 20))
        self.lb_origem_acao_titulo_15.setFont(font4)

        self.verticalLayout_31.addWidget(self.lb_origem_acao_titulo_15)

        self.lb_origem_acao_info_15 = QLabel(self.frame_26)
        self.lb_origem_acao_info_15.setObjectName(u"lb_origem_acao_info_15")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_info_15.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_info_15.setSizePolicy(sizePolicy)
        self.lb_origem_acao_info_15.setMaximumSize(QSize(16777215, 40))
        self.lb_origem_acao_info_15.setFont(font2)
        self.lb_origem_acao_info_15.setStyleSheet(u"margin-left: 20px")
        self.lb_origem_acao_info_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_origem_acao_info_15.setWordWrap(True)

        self.verticalLayout_31.addWidget(self.lb_origem_acao_info_15)


        self.verticalLayout_27.addWidget(self.frame_26)

        self.frame_22 = QFrame(self.scrollAreaWidgetContents)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMaximumSize(QSize(16777215, 100))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_22)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(20, -1, -1, -1)
        self.lb_origem_acao_titulo_11 = QLabel(self.frame_22)
        self.lb_origem_acao_titulo_11.setObjectName(u"lb_origem_acao_titulo_11")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_titulo_11.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_titulo_11.setSizePolicy(sizePolicy)
        self.lb_origem_acao_titulo_11.setMaximumSize(QSize(16777215, 20))
        self.lb_origem_acao_titulo_11.setFont(font4)

        self.verticalLayout_26.addWidget(self.lb_origem_acao_titulo_11)

        self.lb_origem_acao_info_11 = QLabel(self.frame_22)
        self.lb_origem_acao_info_11.setObjectName(u"lb_origem_acao_info_11")
        sizePolicy.setHeightForWidth(self.lb_origem_acao_info_11.sizePolicy().hasHeightForWidth())
        self.lb_origem_acao_info_11.setSizePolicy(sizePolicy)
        self.lb_origem_acao_info_11.setMaximumSize(QSize(16777215, 40))
        self.lb_origem_acao_info_11.setFont(font2)
        self.lb_origem_acao_info_11.setStyleSheet(u"margin-left: 20px")
        self.lb_origem_acao_info_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_origem_acao_info_11.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.lb_origem_acao_info_11)


        self.verticalLayout_27.addWidget(self.frame_22)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lb_valor_titulo = QLabel(self.frame_11)
        self.lb_valor_titulo.setObjectName(u"lb_valor_titulo")
        sizePolicy.setHeightForWidth(self.lb_valor_titulo.sizePolicy().hasHeightForWidth())
        self.lb_valor_titulo.setSizePolicy(sizePolicy)
        self.lb_valor_titulo.setMaximumSize(QSize(16777215, 60))
        self.lb_valor_titulo.setFont(font4)

        self.verticalLayout_11.addWidget(self.lb_valor_titulo)

        self.lb_valor_info = QLabel(self.frame_11)
        self.lb_valor_info.setObjectName(u"lb_valor_info")
        sizePolicy.setHeightForWidth(self.lb_valor_info.sizePolicy().hasHeightForWidth())
        self.lb_valor_info.setSizePolicy(sizePolicy)
        self.lb_valor_info.setMaximumSize(QSize(16777215, 25))
        self.lb_valor_info.setFont(font2)
        self.lb_valor_info.setStyleSheet(u"margin-left: 20px")
        self.lb_valor_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.lb_valor_info)


        self.verticalLayout_27.addWidget(self.frame_11)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.frame_23 = QFrame(self.frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_email = QPushButton(self.frame_23)
        self.btn_email.setObjectName(u"btn_email")
        self.btn_email.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_email.sizePolicy().hasHeightForWidth())
        self.btn_email.setSizePolicy(sizePolicy2)
        self.btn_email.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setFamilies([u"Calibri"])
        font5.setPointSize(15)
        font5.setBold(True)
        self.btn_email.setFont(font5)
        self.btn_email.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"background-color: rgb(136, 50, 101);\n"
"color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(156, 58, 117)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(143, 53, 107)\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_email)


        self.verticalLayout_2.addWidget(self.frame_23)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.Content)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"  	height: 30px;\n"
"  	width: 100px;\n"
"  	color: black;\n"
"  	font-size: 13px;\n"
"  	icon-size: 20px;\n"
"	border: none;\n"
"\n"
"	background-color: rgb(238, 233, 243);\n"
"  }\n"
"\n"
"QCalendarWidget QMenu {\n"
"  	width: 100px;\n"
"  	left: 20px;\n"
"  	color: black;\n"
"  	font-size: 15px;\n"
"  	background-color:   rgb(238, 233, 243);\n"
"  }\n"
"\n"
"QCalendarWidget QWidget { alternate-background-color:rgb(238, 233, 243); }\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled  {\n"
"  	font-size:15px;\n"
"  	color: black;\n"
"  	background-color:  rgb(238, 233, 243);\n"
"  	selection-background-color: rgb(250, 245, 255);\n"
"  	selection-color:rgb(0, 163, 0)\n"
"  }\n"
"\n"
"QCalendarWidget QWidget{\n"
"  background-color: rgb(238, 233, 243);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMaximumSize(QSize(16777215, 60))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_19)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lb_metaAnulado_titulo = QLabel(self.frame_19)
        self.lb_metaAnulado_titulo.setObjectName(u"lb_metaAnulado_titulo")
        sizePolicy.setHeightForWidth(self.lb_metaAnulado_titulo.sizePolicy().hasHeightForWidth())
        self.lb_metaAnulado_titulo.setSizePolicy(sizePolicy)
        self.lb_metaAnulado_titulo.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setFamilies([u"Calibri"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.lb_metaAnulado_titulo.setFont(font6)

        self.verticalLayout_16.addWidget(self.lb_metaAnulado_titulo)

        self.input_metaAnulado = QLineEdit(self.frame_19)
        self.input_metaAnulado.setObjectName(u"input_metaAnulado")
        self.input_metaAnulado.setMinimumSize(QSize(0, 25))
        font7 = QFont()
        font7.setFamilies([u"Calibri"])
        font7.setPointSize(10)
        self.input_metaAnulado.setFont(font7)
        self.input_metaAnulado.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.verticalLayout_16.addWidget(self.input_metaAnulado)


        self.gridLayout.addWidget(self.frame_19, 6, 0, 1, 1)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMaximumSize(QSize(16777215, 60))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_16)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, 0, 0, 0)
        self.lb_dataInicial_titulo = QLabel(self.frame_16)
        self.lb_dataInicial_titulo.setObjectName(u"lb_dataInicial_titulo")
        sizePolicy.setHeightForWidth(self.lb_dataInicial_titulo.sizePolicy().hasHeightForWidth())
        self.lb_dataInicial_titulo.setSizePolicy(sizePolicy)
        self.lb_dataInicial_titulo.setMaximumSize(QSize(16777215, 20))
        self.lb_dataInicial_titulo.setFont(font6)

        self.gridLayout_4.addWidget(self.lb_dataInicial_titulo, 0, 0, 1, 1)

        self.inputDate_emailInicial = QDateEdit(self.frame_16)
        self.inputDate_emailInicial.setObjectName(u"inputDate_emailInicial")
        self.inputDate_emailInicial.setMinimumSize(QSize(0, 25))
        self.inputDate_emailInicial.setMaximumSize(QSize(150, 16777215))
        self.inputDate_emailInicial.setStyleSheet(u"QDateEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}\n"
"")
        self.inputDate_emailInicial.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(15, 0, 0)))
        self.inputDate_emailInicial.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.inputDate_emailInicial, 2, 0, 1, 1)

        self.input_origem_contato1_2 = QLineEdit(self.frame_16)
        self.input_origem_contato1_2.setObjectName(u"input_origem_contato1_2")
        self.input_origem_contato1_2.setMinimumSize(QSize(0, 25))
        self.input_origem_contato1_2.setFont(font7)
        self.input_origem_contato1_2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_4.addWidget(self.input_origem_contato1_2, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_16, 2, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMaximumSize(QSize(16777215, 60))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lb_metaOrigemAtual_titulo = QLabel(self.frame_14)
        self.lb_metaOrigemAtual_titulo.setObjectName(u"lb_metaOrigemAtual_titulo")
        sizePolicy.setHeightForWidth(self.lb_metaOrigemAtual_titulo.sizePolicy().hasHeightForWidth())
        self.lb_metaOrigemAtual_titulo.setSizePolicy(sizePolicy)
        self.lb_metaOrigemAtual_titulo.setMaximumSize(QSize(16777215, 20))
        font8 = QFont()
        font8.setFamilies([u"Calibri"])
        font8.setPointSize(12)
        font8.setBold(False)
        self.lb_metaOrigemAtual_titulo.setFont(font8)

        self.verticalLayout_13.addWidget(self.lb_metaOrigemAtual_titulo)

        self.input_metaOrigemAtual = QLineEdit(self.frame_14)
        self.input_metaOrigemAtual.setObjectName(u"input_metaOrigemAtual")
        self.input_metaOrigemAtual.setMinimumSize(QSize(0, 25))
        self.input_metaOrigemAtual.setFont(font7)
        self.input_metaOrigemAtual.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.verticalLayout_13.addWidget(self.input_metaOrigemAtual)


        self.gridLayout.addWidget(self.frame_14, 1, 0, 1, 1)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMaximumSize(QSize(16777215, 60))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lb_metaDestinoAtual_titulo = QLabel(self.frame_15)
        self.lb_metaDestinoAtual_titulo.setObjectName(u"lb_metaDestinoAtual_titulo")
        sizePolicy.setHeightForWidth(self.lb_metaDestinoAtual_titulo.sizePolicy().hasHeightForWidth())
        self.lb_metaDestinoAtual_titulo.setSizePolicy(sizePolicy)
        self.lb_metaDestinoAtual_titulo.setMaximumSize(QSize(16777215, 20))
        self.lb_metaDestinoAtual_titulo.setFont(font8)

        self.verticalLayout_14.addWidget(self.lb_metaDestinoAtual_titulo)

        self.input_metaOrigemAtual_2 = QLineEdit(self.frame_15)
        self.input_metaOrigemAtual_2.setObjectName(u"input_metaOrigemAtual_2")
        self.input_metaOrigemAtual_2.setMinimumSize(QSize(0, 25))
        self.input_metaOrigemAtual_2.setFont(font7)
        self.input_metaOrigemAtual_2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.verticalLayout_14.addWidget(self.input_metaOrigemAtual_2)


        self.gridLayout.addWidget(self.frame_15, 1, 1, 1, 1)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.inputCheck_emailEnviado = QCheckBox(self.frame_13)
        self.inputCheck_emailEnviado.setObjectName(u"inputCheck_emailEnviado")
        font9 = QFont()
        font9.setFamilies([u"Calibri"])
        font9.setPointSize(13)
        self.inputCheck_emailEnviado.setFont(font9)

        self.horizontalLayout_3.addWidget(self.inputCheck_emailEnviado)

        self.inputCheck_inseridoMetas = QCheckBox(self.frame_13)
        self.inputCheck_inseridoMetas.setObjectName(u"inputCheck_inseridoMetas")
        self.inputCheck_inseridoMetas.setFont(font9)

        self.horizontalLayout_3.addWidget(self.inputCheck_inseridoMetas)

        self.inputCheck_atualizadoSistema = QCheckBox(self.frame_13)
        self.inputCheck_atualizadoSistema.setObjectName(u"inputCheck_atualizadoSistema")
        self.inputCheck_atualizadoSistema.setFont(font9)

        self.horizontalLayout_3.addWidget(self.inputCheck_atualizadoSistema)


        self.gridLayout.addWidget(self.frame_13, 10, 0, 1, 2)

        self.frame_20 = QFrame(self.frame_12)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMaximumSize(QSize(16777215, 60))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lb_metaSuplementado_titulo = QLabel(self.frame_20)
        self.lb_metaSuplementado_titulo.setObjectName(u"lb_metaSuplementado_titulo")
        sizePolicy.setHeightForWidth(self.lb_metaSuplementado_titulo.sizePolicy().hasHeightForWidth())
        self.lb_metaSuplementado_titulo.setSizePolicy(sizePolicy)
        self.lb_metaSuplementado_titulo.setMaximumSize(QSize(16777215, 20))
        self.lb_metaSuplementado_titulo.setFont(font6)

        self.verticalLayout_17.addWidget(self.lb_metaSuplementado_titulo)

        self.input_metaSuplementado = QLineEdit(self.frame_20)
        self.input_metaSuplementado.setObjectName(u"input_metaSuplementado")
        self.input_metaSuplementado.setMinimumSize(QSize(0, 25))
        self.input_metaSuplementado.setFont(font7)
        self.input_metaSuplementado.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.verticalLayout_17.addWidget(self.input_metaSuplementado)


        self.gridLayout.addWidget(self.frame_20, 7, 0, 1, 1)

        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMaximumSize(QSize(16777215, 250))
        font10 = QFont()
        font10.setPointSize(8)
        self.frame_18.setFont(font10)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_18)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(30)
        self.gridLayout_3.setContentsMargins(30, 0, 0, 0)
        self.inputDate_destino1 = QDateEdit(self.frame_18)
        self.inputDate_destino1.setObjectName(u"inputDate_destino1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.inputDate_destino1.sizePolicy().hasHeightForWidth())
        self.inputDate_destino1.setSizePolicy(sizePolicy3)
        self.inputDate_destino1.setMinimumSize(QSize(0, 25))
        self.inputDate_destino1.setMaximumSize(QSize(100, 16777215))
        self.inputDate_destino1.setStyleSheet(u"QDateEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")
        self.inputDate_destino1.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(15, 0, 0)))
        self.inputDate_destino1.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.inputDate_destino1, 1, 0, 1, 1)

        self.input_destino_contato1 = QLineEdit(self.frame_18)
        self.input_destino_contato1.setObjectName(u"input_destino_contato1")
        self.input_destino_contato1.setMinimumSize(QSize(0, 25))
        self.input_destino_contato1.setFont(font7)
        self.input_destino_contato1.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_3.addWidget(self.input_destino_contato1, 1, 1, 1, 1)

        self.input_destino_status3 = QLineEdit(self.frame_18)
        self.input_destino_status3.setObjectName(u"input_destino_status3")
        self.input_destino_status3.setMinimumSize(QSize(0, 25))
        self.input_destino_status3.setFont(font7)
        self.input_destino_status3.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_3.addWidget(self.input_destino_status3, 4, 2, 1, 1)

        self.input_destino_status1 = QLineEdit(self.frame_18)
        self.input_destino_status1.setObjectName(u"input_destino_status1")
        self.input_destino_status1.setMinimumSize(QSize(0, 25))
        self.input_destino_status1.setFont(font7)
        self.input_destino_status1.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_3.addWidget(self.input_destino_status1, 1, 2, 1, 1)

        self.input_destino_contato2 = QLineEdit(self.frame_18)
        self.input_destino_contato2.setObjectName(u"input_destino_contato2")
        self.input_destino_contato2.setMinimumSize(QSize(0, 25))
        self.input_destino_contato2.setFont(font7)
        self.input_destino_contato2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_3.addWidget(self.input_destino_contato2, 3, 1, 1, 1)

        self.input_destino_status2 = QLineEdit(self.frame_18)
        self.input_destino_status2.setObjectName(u"input_destino_status2")
        self.input_destino_status2.setMinimumSize(QSize(0, 25))
        self.input_destino_status2.setFont(font7)
        self.input_destino_status2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_3.addWidget(self.input_destino_status2, 3, 2, 1, 1)

        self.inputDate_destino2 = QDateEdit(self.frame_18)
        self.inputDate_destino2.setObjectName(u"inputDate_destino2")
        sizePolicy3.setHeightForWidth(self.inputDate_destino2.sizePolicy().hasHeightForWidth())
        self.inputDate_destino2.setSizePolicy(sizePolicy3)
        self.inputDate_destino2.setMinimumSize(QSize(0, 25))
        self.inputDate_destino2.setMaximumSize(QSize(100, 16777215))
        self.inputDate_destino2.setStyleSheet(u"QDateEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")
        self.inputDate_destino2.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(15, 0, 0)))
        self.inputDate_destino2.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.inputDate_destino2, 3, 0, 1, 1)

        self.input_destino_contato3 = QLineEdit(self.frame_18)
        self.input_destino_contato3.setObjectName(u"input_destino_contato3")
        self.input_destino_contato3.setMinimumSize(QSize(0, 25))
        self.input_destino_contato3.setFont(font7)
        self.input_destino_contato3.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_3.addWidget(self.input_destino_contato3, 4, 1, 1, 1)

        self.label_24 = QLabel(self.frame_18)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMaximumSize(QSize(16777215, 20))
        self.label_24.setFont(font3)

        self.gridLayout_3.addWidget(self.label_24, 0, 0, 1, 1)

        self.inputDate_destino3 = QDateEdit(self.frame_18)
        self.inputDate_destino3.setObjectName(u"inputDate_destino3")
        sizePolicy3.setHeightForWidth(self.inputDate_destino3.sizePolicy().hasHeightForWidth())
        self.inputDate_destino3.setSizePolicy(sizePolicy3)
        self.inputDate_destino3.setMinimumSize(QSize(0, 25))
        self.inputDate_destino3.setMaximumSize(QSize(100, 16777215))
        self.inputDate_destino3.setStyleSheet(u"QDateEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")
        self.inputDate_destino3.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(15, 0, 0)))
        self.inputDate_destino3.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.inputDate_destino3, 4, 0, 1, 1)

        self.inputCheck_geraEmailDestino = QCheckBox(self.frame_18)
        self.inputCheck_geraEmailDestino.setObjectName(u"inputCheck_geraEmailDestino")
        self.inputCheck_geraEmailDestino.setFont(font9)

        self.gridLayout_3.addWidget(self.inputCheck_geraEmailDestino, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_18, 5, 0, 1, 2)

        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMaximumSize(QSize(16777215, 250))
        self.frame_17.setFont(font10)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_17)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setContentsMargins(30, 0, 0, 0)
        self.input_origem_status3 = QLineEdit(self.frame_17)
        self.input_origem_status3.setObjectName(u"input_origem_status3")
        self.input_origem_status3.setMinimumSize(QSize(0, 25))
        self.input_origem_status3.setFont(font7)
        self.input_origem_status3.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_status3, 3, 2, 1, 1)

        self.inputDate_origem1 = QDateEdit(self.frame_17)
        self.inputDate_origem1.setObjectName(u"inputDate_origem1")
        self.inputDate_origem1.setMinimumSize(QSize(0, 25))
        self.inputDate_origem1.setMaximumSize(QSize(100, 16777215))
        self.inputDate_origem1.setStyleSheet(u"QDateEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")
        self.inputDate_origem1.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(15, 0, 0)))
        self.inputDate_origem1.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.inputDate_origem1, 1, 0, 1, 1)

        self.label_23 = QLabel(self.frame_17)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMaximumSize(QSize(16777215, 20))
        self.label_23.setFont(font3)

        self.gridLayout_2.addWidget(self.label_23, 0, 0, 1, 1)

        self.input_origem_contato3 = QLineEdit(self.frame_17)
        self.input_origem_contato3.setObjectName(u"input_origem_contato3")
        self.input_origem_contato3.setMinimumSize(QSize(0, 25))
        self.input_origem_contato3.setFont(font7)
        self.input_origem_contato3.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_contato3, 3, 1, 1, 1)

        self.inputDate_origem3 = QDateEdit(self.frame_17)
        self.inputDate_origem3.setObjectName(u"inputDate_origem3")
        sizePolicy3.setHeightForWidth(self.inputDate_origem3.sizePolicy().hasHeightForWidth())
        self.inputDate_origem3.setSizePolicy(sizePolicy3)
        self.inputDate_origem3.setMinimumSize(QSize(0, 25))
        self.inputDate_origem3.setMaximumSize(QSize(100, 16777215))
        self.inputDate_origem3.setStyleSheet(u"QDateEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")
        self.inputDate_origem3.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(15, 0, 0)))
        self.inputDate_origem3.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.inputDate_origem3, 3, 0, 1, 1)

        self.input_origem_status1 = QLineEdit(self.frame_17)
        self.input_origem_status1.setObjectName(u"input_origem_status1")
        self.input_origem_status1.setMinimumSize(QSize(0, 25))
        self.input_origem_status1.setFont(font7)
        self.input_origem_status1.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_status1, 1, 2, 1, 1)

        self.input_origem_contato2 = QLineEdit(self.frame_17)
        self.input_origem_contato2.setObjectName(u"input_origem_contato2")
        self.input_origem_contato2.setMinimumSize(QSize(0, 25))
        self.input_origem_contato2.setFont(font7)
        self.input_origem_contato2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_contato2, 2, 1, 1, 1)

        self.input_origem_status2 = QLineEdit(self.frame_17)
        self.input_origem_status2.setObjectName(u"input_origem_status2")
        self.input_origem_status2.setMinimumSize(QSize(0, 25))
        self.input_origem_status2.setFont(font7)
        self.input_origem_status2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_status2, 2, 2, 1, 1)

        self.inputDate_origem2 = QDateEdit(self.frame_17)
        self.inputDate_origem2.setObjectName(u"inputDate_origem2")
        sizePolicy3.setHeightForWidth(self.inputDate_origem2.sizePolicy().hasHeightForWidth())
        self.inputDate_origem2.setSizePolicy(sizePolicy3)
        self.inputDate_origem2.setMinimumSize(QSize(0, 25))
        self.inputDate_origem2.setMaximumSize(QSize(100, 16777215))
        self.inputDate_origem2.setStyleSheet(u"QDateEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")
        self.inputDate_origem2.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(15, 0, 0)))
        self.inputDate_origem2.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.inputDate_origem2, 2, 0, 1, 1)

        self.input_origem_contato1 = QLineEdit(self.frame_17)
        self.input_origem_contato1.setObjectName(u"input_origem_contato1")
        self.input_origem_contato1.setMinimumSize(QSize(0, 25))
        self.input_origem_contato1.setFont(font7)
        self.input_origem_contato1.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_contato1, 1, 1, 1, 1)

        self.inputCheck_geraEmailOrigem = QCheckBox(self.frame_17)
        self.inputCheck_geraEmailOrigem.setObjectName(u"inputCheck_geraEmailOrigem")
        self.inputCheck_geraEmailOrigem.setFont(font9)

        self.gridLayout_2.addWidget(self.inputCheck_geraEmailOrigem, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_17, 4, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 11, 0, 1, 1)

        self.inputCheck_permaneceMetaOrigem = QCheckBox(self.frame_12)
        self.inputCheck_permaneceMetaOrigem.setObjectName(u"inputCheck_permaneceMetaOrigem")
        self.inputCheck_permaneceMetaOrigem.setFont(font9)

        self.gridLayout.addWidget(self.inputCheck_permaneceMetaOrigem, 6, 1, 1, 1)

        self.inputCheck_permaneceMetaDestino = QCheckBox(self.frame_12)
        self.inputCheck_permaneceMetaDestino.setObjectName(u"inputCheck_permaneceMetaDestino")
        self.inputCheck_permaneceMetaDestino.setFont(font9)

        self.gridLayout.addWidget(self.inputCheck_permaneceMetaDestino, 7, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.frame_24 = QFrame(self.frame_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_salvar = QPushButton(self.frame_24)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setMinimumSize(QSize(0, 40))
        self.btn_salvar.setFont(font5)
        self.btn_salvar.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"background-color: rgb(136, 50, 101);\n"
"color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(156, 58, 117)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(143, 53, 107)\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_salvar)

        self.btn_salvar_espelhado = QPushButton(self.frame_24)
        self.btn_salvar_espelhado.setObjectName(u"btn_salvar_espelhado")
        self.btn_salvar_espelhado.setMinimumSize(QSize(0, 40))
        self.btn_salvar_espelhado.setFont(font5)
        self.btn_salvar_espelhado.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"background-color: rgb(136, 50, 101);\n"
"color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(156, 58, 117)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(143, 53, 107)\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_salvar_espelhado)


        self.verticalLayout_12.addWidget(self.frame_24)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.Content)

        #Form.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.lb_metaAnulado_titulo.setBuddy(self.input_metaOrigemAtual)
        self.lb_dataInicial_titulo.setBuddy(self.input_metaOrigemAtual)
        self.lb_metaOrigemAtual_titulo.setBuddy(self.input_metaOrigemAtual)
        self.lb_metaDestinoAtual_titulo.setBuddy(self.input_metaOrigemAtual_2)
        self.lb_metaSuplementado_titulo.setBuddy(self.input_metaOrigemAtual)
        self.label_24.setBuddy(self.input_metaOrigemAtual)
        self.label_23.setBuddy(self.input_metaOrigemAtual)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MainWindow", None))
        self.btn_voltar.setText("")
        self.lb_tituloPrincipal.setText(QCoreApplication.translate("Form", u"Monitoramento", None))
        self.lb_decreto_titulo.setText(QCoreApplication.translate("Form", u"N\u00famero Decreto / Portaria:", None))
        self.lb_decreto_info.setText(QCoreApplication.translate("Form", u"57816", None))
        self.lb_dataDecreto_titulo.setText(QCoreApplication.translate("Form", u"Data do Decreto:", None))
        self.lb_dataDecreto_info.setText(QCoreApplication.translate("Form", u"19/05/2022", None))
        self.lb_origem_titulo.setText(QCoreApplication.translate("Form", u"Origem:", None))
        self.lb_origem_orgao_titulo.setText(QCoreApplication.translate("Form", u"Org\u00e3o:", None))
        self.lb_origem_orgao_info.setText(QCoreApplication.translate("Form", u"11 - SEMGOV", None))
        self.lb_origem_programa_titulo.setText(QCoreApplication.translate("Form", u"Programa:", None))
        self.lb_origem_programa_info.setText(QCoreApplication.translate("Form", u"0229 - GEST\u00c3O PARTICIPATIVA E CIDADANIA", None))
        self.lb_origem_acao_titulo.setText(QCoreApplication.translate("Form", u"A\u00e7\u00e3o:", None))
        self.lb_origem_acao_info.setText(QCoreApplication.translate("Form", u"2033 - APIO AS DEMANDAS DA SOCIEDADE CIVIL", None))
        self.lb_origem_acao_titulo_13.setText(QCoreApplication.translate("Form", u"Produto:", None))
        self.lb_origem_acao_info_13.setText(QCoreApplication.translate("Form", u"A\u00c7\u00d5ES CULTURAIS REALIZADAS", None))
        self.lb_origem_acao_titulo_3.setText(QCoreApplication.translate("Form", u"Meta F\u00edsica:", None))
        self.lb_origem_acao_info_3.setText("")
        self.lb_destino_titulo.setText(QCoreApplication.translate("Form", u"Destino:", None))
        self.lb_destino_orgao_titulo.setText(QCoreApplication.translate("Form", u"\u00d3rg\u00e3o:", None))
        self.lb_destino_orgao_info.setText(QCoreApplication.translate("Form", u"31 - SECULT", None))
        self.lb_destino_acao_titulo.setText(QCoreApplication.translate("Form", u"A\u00e7\u00e3o:", None))
        self.lb_destino_acao_info.setText(QCoreApplication.translate("Form", u"2006 - PROMOVER E DESENVOLVER O AMBIENTE CULTURAL", None))
        self.lb_destino_programa_titulo.setText(QCoreApplication.translate("Form", u"Programa:", None))
        self.lb_destino_programa_info.setText(QCoreApplication.translate("Form", u"201 - CULTURA PATRIM\u00d4NIO CULTURAL E TURISMO", None))
        self.lb_origem_acao_titulo_15.setText(QCoreApplication.translate("Form", u"Produto:", None))
        self.lb_origem_acao_info_15.setText(QCoreApplication.translate("Form", u"EMENDAS PARLAMENTARES", None))
        self.lb_origem_acao_titulo_11.setText(QCoreApplication.translate("Form", u"Meta F\u00edsica:", None))
        self.lb_origem_acao_info_11.setText("")
        self.lb_valor_titulo.setText(QCoreApplication.translate("Form", u"Valor Remanejado:", None))
        self.lb_valor_info.setText(QCoreApplication.translate("Form", u"R$ 200.000,00", None))
        self.btn_email.setText(QCoreApplication.translate("Form", u"Copiar Email", None))
        self.lb_metaAnulado_titulo.setText(QCoreApplication.translate("Form", u"Nova Meta F\u00edsica Anulado (Origem)", None))
        self.lb_dataInicial_titulo.setText(QCoreApplication.translate("Form", u"Data Email Inicial", None))
        self.input_origem_contato1_2.setText("")
        self.input_origem_contato1_2.setPlaceholderText(QCoreApplication.translate("Form", u"Destinat\u00e1rios", None))
        self.lb_metaOrigemAtual_titulo.setText(QCoreApplication.translate("Form", u"Meta F\u00cdSICA de Origem ATUAL", None))
        self.lb_metaDestinoAtual_titulo.setText(QCoreApplication.translate("Form", u"Meta F\u00cdSICA de Destino ATUAL", None))
        self.inputCheck_emailEnviado.setText(QCoreApplication.translate("Form", u"E-mail Enviado", None))
        self.inputCheck_inseridoMetas.setText(QCoreApplication.translate("Form", u"Inserido Metas", None))
        self.inputCheck_atualizadoSistema.setText(QCoreApplication.translate("Form", u"Atualizado Sistema", None))
        self.lb_metaSuplementado_titulo.setText(QCoreApplication.translate("Form", u"Nova Meta F\u00edsica Suplementado (Destino)", None))
        self.input_destino_contato1.setText("")
        self.input_destino_contato1.setPlaceholderText(QCoreApplication.translate("Form", u"Contato 1", None))
        self.input_destino_status3.setPlaceholderText(QCoreApplication.translate("Form", u"Status 3", None))
        self.input_destino_status1.setPlaceholderText(QCoreApplication.translate("Form", u"Status 1", None))
        self.input_destino_contato2.setText("")
        self.input_destino_contato2.setPlaceholderText(QCoreApplication.translate("Form", u"Contato 2", None))
        self.input_destino_status2.setPlaceholderText(QCoreApplication.translate("Form", u"Status 2", None))
        self.input_destino_contato3.setText("")
        self.input_destino_contato3.setPlaceholderText(QCoreApplication.translate("Form", u"Contato 3", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Destino", None))
        self.inputCheck_geraEmailDestino.setText(QCoreApplication.translate("Form", u"N\u00e3o gera email", None))
        self.input_origem_status3.setPlaceholderText(QCoreApplication.translate("Form", u"Status 3", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Origem", None))
        self.input_origem_contato3.setText("")
        self.input_origem_contato3.setPlaceholderText(QCoreApplication.translate("Form", u"Contato 3", None))
        self.input_origem_status1.setPlaceholderText(QCoreApplication.translate("Form", u"Status 1", None))
        self.input_origem_contato2.setText("")
        self.input_origem_contato2.setPlaceholderText(QCoreApplication.translate("Form", u"Contato 2", None))
        self.input_origem_status2.setPlaceholderText(QCoreApplication.translate("Form", u"Status 2", None))
        self.input_origem_contato1.setText("")
        self.input_origem_contato1.setPlaceholderText(QCoreApplication.translate("Form", u"Contato 1", None))
        self.inputCheck_geraEmailOrigem.setText(QCoreApplication.translate("Form", u"N\u00e3o gera email", None))
        self.inputCheck_permaneceMetaOrigem.setText(QCoreApplication.translate("Form", u"Permanece a mesma meta", None))
        self.inputCheck_permaneceMetaDestino.setText(QCoreApplication.translate("Form", u"Permanece a mesma meta", None))
        self.btn_salvar.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.btn_salvar_espelhado.setText(QCoreApplication.translate("Form", u"Salvar com Espelhamento", None))
    # retranslateUi

