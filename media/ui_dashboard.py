# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardbSJHae.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

import media.resource_rc

class Ui_Form(object):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1143, 739)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none")
        #self.centralwidget = QWidget(MainWindow)
        #self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget = MainWindow
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Titulo = QFrame(self.centralwidget)
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
        self.lb_tituloPrincipal = QLabel(self.Titulo)
        self.lb_tituloPrincipal.setObjectName(u"lb_tituloPrincipal")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloPrincipal.setFont(font)
        self.lb_tituloPrincipal.setStyleSheet(u"color: white;")
        self.lb_tituloPrincipal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_tituloPrincipal)


        self.verticalLayout.addWidget(self.Titulo)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_contador = QFrame(self.frame)
        self.fr_contador.setObjectName(u"fr_contador")
        sizePolicy.setHeightForWidth(self.fr_contador.sizePolicy().hasHeightForWidth())
        self.fr_contador.setSizePolicy(sizePolicy)
        self.fr_contador.setMaximumSize(QSize(16777215, 90))
        self.fr_contador.setFrameShape(QFrame.StyledPanel)
        self.fr_contador.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_contador)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.frame_4 = QFrame(self.fr_contador)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_cont_todos = QLabel(self.frame_4)
        self.lb_cont_todos.setObjectName(u"lb_cont_todos")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setWeight(75)
        self.lb_cont_todos.setFont(font1)
        self.lb_cont_todos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_cont_todos)

        self.lb_titulo_todos = QLabel(self.frame_4)
        self.lb_titulo_todos.setObjectName(u"lb_titulo_todos")
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.lb_titulo_todos.setFont(font2)
        self.lb_titulo_todos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_titulo_todos)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.fr_contador)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setStyleSheet(u"color: rgb(48, 77, 157)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lb_cont_analise = QLabel(self.frame_7)
        self.lb_cont_analise.setObjectName(u"lb_cont_analise")
        self.lb_cont_analise.setFont(font1)
        self.lb_cont_analise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lb_cont_analise)

        self.lb_titulo_analise = QLabel(self.frame_7)
        self.lb_titulo_analise.setObjectName(u"lb_titulo_analise")
        self.lb_titulo_analise.setFont(font2)
        self.lb_titulo_analise.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lb_titulo_analise)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_11 = QFrame(self.fr_contador)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 100))
        self.frame_11.setStyleSheet(u"color: rgb(255, 85, 0)")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lb_cont_email = QLabel(self.frame_11)
        self.lb_cont_email.setObjectName(u"lb_cont_email")
        self.lb_cont_email.setFont(font1)
        self.lb_cont_email.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lb_cont_email)

        self.lb_titulo_email = QLabel(self.frame_11)
        self.lb_titulo_email.setObjectName(u"lb_titulo_email")
        self.lb_titulo_email.setFont(font2)
        self.lb_titulo_email.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lb_titulo_email)


        self.horizontalLayout_2.addWidget(self.frame_11)

        self.frame_8 = QFrame(self.fr_contador)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setStyleSheet(u"color: rgb(195, 176, 0)")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lb_cont_metas = QLabel(self.frame_8)
        self.lb_cont_metas.setObjectName(u"lb_cont_metas")
        self.lb_cont_metas.setFont(font1)
        self.lb_cont_metas.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lb_cont_metas)

        self.lb_titulo_metas = QLabel(self.frame_8)
        self.lb_titulo_metas.setObjectName(u"lb_titulo_metas")
        self.lb_titulo_metas.setFont(font2)
        self.lb_titulo_metas.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lb_titulo_metas)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.fr_contador)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setStyleSheet(u"color:rgb(71, 185, 44)")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_cont_inseridos = QLabel(self.frame_6)
        self.lb_cont_inseridos.setObjectName(u"lb_cont_inseridos")
        self.lb_cont_inseridos.setFont(font1)
        self.lb_cont_inseridos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lb_cont_inseridos)

        self.lb_titulo_inserido = QLabel(self.frame_6)
        self.lb_titulo_inserido.setObjectName(u"lb_titulo_inserido")
        self.lb_titulo_inserido.setFont(font2)
        self.lb_titulo_inserido.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lb_titulo_inserido)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.fr_contador)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMaximumSize(QSize(200, 16777215))
        self.frame_5.setStyleSheet(u"QPushButton {\n"
"	background-color: white;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(109, 49, 162)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font-size: 18px;\n"
"	border-bottom: 2px solid rgb(109, 49, 162)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: white;\n"
"	border: none;\n"
"	border-bottom: 2px solid rgb(109, 49, 162)\n"
"}\n"
"\n"
"QFrame {\n"
"	border-right: 1px solid rgb(232, 232, 232);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 20, 0, 0)
        self.btn_todos = QPushButton(self.frame_5)
        self.btn_todos.setObjectName(u"btn_todos")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_todos.sizePolicy().hasHeightForWidth())
        self.btn_todos.setSizePolicy(sizePolicy2)
        self.btn_todos.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(13)
        self.btn_todos.setFont(font3)
        self.btn_todos.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_todos)

        self.btn_analise = QPushButton(self.frame_5)
        self.btn_analise.setObjectName(u"btn_analise")
        sizePolicy2.setHeightForWidth(self.btn_analise.sizePolicy().hasHeightForWidth())
        self.btn_analise.setSizePolicy(sizePolicy2)
        self.btn_analise.setMaximumSize(QSize(16777215, 40))
        self.btn_analise.setFont(font3)
        self.btn_analise.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_analise)

        self.btn_email = QPushButton(self.frame_5)
        self.btn_email.setObjectName(u"btn_email")
        sizePolicy2.setHeightForWidth(self.btn_email.sizePolicy().hasHeightForWidth())
        self.btn_email.setSizePolicy(sizePolicy2)
        self.btn_email.setMaximumSize(QSize(16777215, 40))
        self.btn_email.setFont(font3)
        self.btn_email.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_email)

        self.btn_metas = QPushButton(self.frame_5)
        self.btn_metas.setObjectName(u"btn_metas")
        sizePolicy2.setHeightForWidth(self.btn_metas.sizePolicy().hasHeightForWidth())
        self.btn_metas.setSizePolicy(sizePolicy2)
        self.btn_metas.setMaximumSize(QSize(16777215, 40))
        self.btn_metas.setFont(font3)
        self.btn_metas.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_metas)

        self.btn_inserido = QPushButton(self.frame_5)
        self.btn_inserido.setObjectName(u"btn_inserido")
        sizePolicy2.setHeightForWidth(self.btn_inserido.sizePolicy().hasHeightForWidth())
        self.btn_inserido.setSizePolicy(sizePolicy2)
        self.btn_inserido.setMaximumSize(QSize(16777215, 40))
        self.btn_inserido.setFont(font3)
        self.btn_inserido.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_inserido)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_relatorio_excel = QPushButton(self.frame_5)
        self.btn_relatorio_excel.setObjectName(u"btn_relatorio_excel")
        sizePolicy2.setHeightForWidth(self.btn_relatorio_excel.sizePolicy().hasHeightForWidth())
        self.btn_relatorio_excel.setSizePolicy(sizePolicy2)
        self.btn_relatorio_excel.setMaximumSize(QSize(16777215, 40))
        self.btn_relatorio_excel.setFont(font3)
        self.btn_relatorio_excel.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_relatorio_excel)

        self.btn_relatorio = QPushButton(self.frame_5)
        self.btn_relatorio.setObjectName(u"btn_relatorio")
        sizePolicy2.setHeightForWidth(self.btn_relatorio.sizePolicy().hasHeightForWidth())
        self.btn_relatorio.setSizePolicy(sizePolicy2)
        self.btn_relatorio.setMaximumSize(QSize(16777215, 40))
        self.btn_relatorio.setFont(font3)
        self.btn_relatorio.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_relatorio)

        self.btn_planilha = QPushButton(self.frame_5)
        self.btn_planilha.setObjectName(u"btn_planilha")
        sizePolicy2.setHeightForWidth(self.btn_planilha.sizePolicy().hasHeightForWidth())
        self.btn_planilha.setSizePolicy(sizePolicy2)
        self.btn_planilha.setMaximumSize(QSize(16777215, 40))
        self.btn_planilha.setFont(font3)
        self.btn_planilha.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_planilha)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, -1, 100, -1)
        self.lb_busca = QLabel(self.frame_10)
        self.lb_busca.setObjectName(u"lb_busca")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(12)
        self.lb_busca.setFont(font4)

        self.horizontalLayout_4.addWidget(self.lb_busca)

        self.input_busca = QLineEdit(self.frame_10)
        self.input_busca.setObjectName(u"input_busca")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.input_busca.sizePolicy().hasHeightForWidth())
        self.input_busca.setSizePolicy(sizePolicy3)
        self.input_busca.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.horizontalLayout_4.addWidget(self.input_busca)

        self.btn_busca = QPushButton(self.frame_10)
        self.btn_busca.setObjectName(u"btn_busca")
        self.btn_busca.setMaximumSize(QSize(40, 40))
        self.btn_busca.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	image: url(:/icons/icon_busca.png);\n"
"	padding: 6px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 4px\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	padding: 5px\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_busca)

        self.lb_busca_2 = QLabel(self.frame_10)
        self.lb_busca_2.setObjectName(u"lb_busca_2")
        self.lb_busca_2.setMaximumSize(QSize(90, 16777215))
        self.lb_busca_2.setFont(font4)

        self.horizontalLayout_4.addWidget(self.lb_busca_2)

        self.comboBox = QComboBox(self.frame_10)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(75, 0))
        self.comboBox.setMaximumSize(QSize(75, 16777215))
        self.comboBox.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.comboBox)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_scroll = QFrame(self.frame_9)
        self.frame_scroll.setObjectName(u"frame_scroll")
        sizePolicy.setHeightForWidth(self.frame_scroll.sizePolicy().hasHeightForWidth())
        self.frame_scroll.setSizePolicy(sizePolicy)
        self.frame_scroll.setFrameShape(QFrame.StyledPanel)
        self.frame_scroll.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_scroll)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_scroll)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(21, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(150, 0))
        self.checkBox.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_5.addWidget(self.checkBox)

        self.lb_filtro = QLabel(self.frame_2)
        self.lb_filtro.setObjectName(u"lb_filtro")
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(13)
        font5.setBold(False)
        font5.setWeight(50)
        self.lb_filtro.setFont(font5)
        self.lb_filtro.setStyleSheet(u"margin-left: 15px")
        self.lb_filtro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_filtro)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.scrollArea = QScrollArea(self.frame_scroll)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setStyleSheet(u"border:none")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 920, 443))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.frame_12 = QFrame(self.frame_scroll)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, 0, 17, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frame_paginacao = QFrame(self.frame_12)
        self.frame_paginacao.setObjectName(u"frame_paginacao")
        self.frame_paginacao.setMinimumSize(QSize(0, 0))
        self.frame_paginacao.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: white;\n"
"	font-weight: 700;\n"
"	\n"
"	background-color: rgb(169, 144, 190)\n"
"}")
        self.frame_paginacao.setFrameShape(QFrame.StyledPanel)
        self.frame_paginacao.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_paginacao)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.pag_inicio = QPushButton(self.frame_paginacao)
        self.pag_inicio.setObjectName(u"pag_inicio")
        self.pag_inicio.setMinimumSize(QSize(30, 30))
        self.pag_inicio.setMaximumSize(QSize(30, 30))
        font6 = QFont()
        font6.setPointSize(11)
        self.pag_inicio.setFont(font6)
        self.pag_inicio.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pag_inicio)

        self.pag_anterior = QPushButton(self.frame_paginacao)
        self.pag_anterior.setObjectName(u"pag_anterior")
        self.pag_anterior.setMinimumSize(QSize(30, 30))
        self.pag_anterior.setMaximumSize(QSize(30, 30))
        self.pag_anterior.setFont(font6)
        self.pag_anterior.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pag_anterior)

        self.frame_pagMeio = QFrame(self.frame_paginacao)
        self.frame_pagMeio.setObjectName(u"frame_pagMeio")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_pagMeio.sizePolicy().hasHeightForWidth())
        self.frame_pagMeio.setSizePolicy(sizePolicy4)
        self.frame_pagMeio.setFrameShape(QFrame.StyledPanel)
        self.frame_pagMeio.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_pagMeio)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pag_1 = QPushButton(self.frame_pagMeio)
        self.pag_1.setObjectName(u"pag_1")
        self.pag_1.setMinimumSize(QSize(30, 30))
        self.pag_1.setMaximumSize(QSize(30, 30))
        self.pag_1.setFont(font6)
        self.pag_1.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: rgb(76, 34, 112);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pag_1)

        self.pag_2 = QPushButton(self.frame_pagMeio)
        self.pag_2.setObjectName(u"pag_2")
        self.pag_2.setMinimumSize(QSize(30, 30))
        self.pag_2.setMaximumSize(QSize(30, 30))
        self.pag_2.setFont(font6)
        self.pag_2.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pag_2)

        self.pag_3 = QPushButton(self.frame_pagMeio)
        self.pag_3.setObjectName(u"pag_3")
        self.pag_3.setMinimumSize(QSize(30, 30))
        self.pag_3.setMaximumSize(QSize(30, 30))
        self.pag_3.setFont(font6)
        self.pag_3.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pag_3)

        self.pag_4 = QPushButton(self.frame_pagMeio)
        self.pag_4.setObjectName(u"pag_4")
        self.pag_4.setMinimumSize(QSize(30, 30))
        self.pag_4.setMaximumSize(QSize(30, 30))
        self.pag_4.setFont(font6)
        self.pag_4.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pag_4)

        self.pag_5 = QPushButton(self.frame_pagMeio)
        self.pag_5.setObjectName(u"pag_5")
        self.pag_5.setMinimumSize(QSize(30, 30))
        self.pag_5.setMaximumSize(QSize(30, 30))
        self.pag_5.setFont(font6)
        self.pag_5.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pag_5)


        self.horizontalLayout_7.addWidget(self.frame_pagMeio)

        self.pag_proximo = QPushButton(self.frame_paginacao)
        self.pag_proximo.setObjectName(u"pag_proximo")
        self.pag_proximo.setMinimumSize(QSize(30, 30))
        self.pag_proximo.setMaximumSize(QSize(30, 30))
        self.pag_proximo.setFont(font6)
        self.pag_proximo.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pag_proximo)

        self.pag_fim = QPushButton(self.frame_paginacao)
        self.pag_fim.setObjectName(u"pag_fim")
        self.pag_fim.setMinimumSize(QSize(30, 30))
        self.pag_fim.setMaximumSize(QSize(30, 30))
        self.pag_fim.setFont(font6)
        self.pag_fim.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pag_fim)


        self.horizontalLayout_6.addWidget(self.frame_paginacao)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addWidget(self.frame_12)


        self.verticalLayout_5.addWidget(self.frame_scroll)


        self.horizontalLayout_3.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_tituloPrincipal.setText(QCoreApplication.translate("MainWindow", u"Monitoramento", None))
        self.lb_cont_todos.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_titulo_todos.setText(QCoreApplication.translate("MainWindow", u"Todos", None))
        self.lb_cont_analise.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_titulo_analise.setText(QCoreApplication.translate("MainWindow", u"Em An\u00e1lise", None))
        self.lb_cont_email.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_titulo_email.setText(QCoreApplication.translate("MainWindow", u"Email Enviado", None))
        self.lb_cont_metas.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_titulo_metas.setText(QCoreApplication.translate("MainWindow", u"Metas Inseridas", None))
        self.lb_cont_inseridos.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_titulo_inserido.setText(QCoreApplication.translate("MainWindow", u"Inserido no Sistema", None))
        self.btn_todos.setText(QCoreApplication.translate("MainWindow", u"Todos", None))
        self.btn_analise.setText(QCoreApplication.translate("MainWindow", u"Em An\u00e1lise", None))
        self.btn_email.setText(QCoreApplication.translate("MainWindow", u"E-mail Enviado", None))
        self.btn_metas.setText(QCoreApplication.translate("MainWindow", u"Metas Inseridas", None))
        self.btn_inserido.setText(QCoreApplication.translate("MainWindow", u"Inserido no Sistema", None))
        self.btn_relatorio_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_relatorio.setText(QCoreApplication.translate("MainWindow", u"Gerar PDF", None))
        self.btn_planilha.setText(QCoreApplication.translate("MainWindow", u"Selecionar Planilha", None))
        self.lb_busca.setText(QCoreApplication.translate("MainWindow", u"Busca", None))
        self.btn_busca.setText("")
        self.lb_busca_2.setText(QCoreApplication.translate("MainWindow", u"Exibir:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"100", None))

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Selecionar Todos", None))
        self.lb_filtro.setText("")
        self.pag_inicio.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.pag_anterior.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pag_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pag_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pag_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pag_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pag_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pag_proximo.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pag_fim.setText(QCoreApplication.translate("MainWindow", u">>", None))
    # retranslateUi

