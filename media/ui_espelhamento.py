# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EspelhamentoCLToZS.ui'
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
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(724, 684)
        Form.setMinimumSize(QSize(724, 300))
        Form.setMaximumSize(QSize(724, 16777215))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 17)
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

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_busca = QLabel(self.frame_3)
        self.lb_busca.setObjectName(u"lb_busca")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.lb_busca.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lb_busca)

        self.input_busca = QLineEdit(self.frame_3)
        self.input_busca.setObjectName(u"input_busca")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_busca.sizePolicy().hasHeightForWidth())
        self.input_busca.setSizePolicy(sizePolicy1)
        self.input_busca.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.horizontalLayout_3.addWidget(self.input_busca)

        self.btn_busca = QPushButton(self.frame_3)
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

        self.horizontalLayout_3.addWidget(self.btn_busca)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(150, 0))
        self.checkBox.setMaximumSize(QSize(110, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.checkBox.setFont(font2)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.lb_totalDecretos = QLabel(self.frame_2)
        self.lb_totalDecretos.setObjectName(u"lb_totalDecretos")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.lb_totalDecretos.setFont(font3)
        self.lb_totalDecretos.setStyleSheet(u"")
        self.lb_totalDecretos.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lb_totalDecretos)


        self.verticalLayout.addWidget(self.frame_2)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.tabWidget.setFont(font4)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid lightgray;\n"
"  top:-1px; \n"
"  background: rgb(245, 245, 245);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(230, 230, 230); \n"
"  border: 1px solid lightgray; \n"
"  padding: 15px 46px;\n"
"} \n"
"\n"
"QTabBar::tab:hover { \n"
"  background:rgb(136, 50, 101); \n"
"	color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected { \n"
"  background:rgb(136, 50, 101); \n"
"color: white;\n"
"  margin-bottom: -1px; \n"
"}")
        self.tab_analise = QWidget()
        self.tab_analise.setObjectName(u"tab_analise")
        self.verticalLayout_4 = QVBoxLayout(self.tab_analise)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_analise = QScrollArea(self.tab_analise)
        self.scrollArea_analise.setObjectName(u"scrollArea_analise")
        self.scrollArea_analise.setEnabled(True)
        self.scrollArea_analise.setStyleSheet(u"border:none")
        self.scrollArea_analise.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_analise.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_analise.setWidgetResizable(True)
        self.scrollArea_analise.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 687, 369))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea_analise.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_analise)

        self.tabWidget.addTab(self.tab_analise, "")
        self.tab_enviado = QWidget()
        self.tab_enviado.setObjectName(u"tab_enviado")
        self.verticalLayout_5 = QVBoxLayout(self.tab_enviado)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_enviado = QScrollArea(self.tab_enviado)
        self.scrollArea_enviado.setObjectName(u"scrollArea_enviado")
        self.scrollArea_enviado.setEnabled(True)
        self.scrollArea_enviado.setMinimumSize(QSize(700, 300))
        self.scrollArea_enviado.setStyleSheet(u"border:none")
        self.scrollArea_enviado.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_enviado.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_enviado.setWidgetResizable(True)
        self.scrollArea_enviado.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 687, 369))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea_enviado.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_5.addWidget(self.scrollArea_enviado)

        self.tabWidget.addTab(self.tab_enviado, "")
        self.tab_metas = QWidget()
        self.tab_metas.setObjectName(u"tab_metas")
        self.verticalLayout_6 = QVBoxLayout(self.tab_metas)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_metas = QScrollArea(self.tab_metas)
        self.scrollArea_metas.setObjectName(u"scrollArea_metas")
        self.scrollArea_metas.setEnabled(True)
        self.scrollArea_metas.setStyleSheet(u"border:none")
        self.scrollArea_metas.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_metas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_metas.setWidgetResizable(True)
        self.scrollArea_metas.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 687, 369))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_metas.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_6.addWidget(self.scrollArea_metas)

        self.tabWidget.addTab(self.tab_metas, "")
        self.tab_sistema = QWidget()
        self.tab_sistema.setObjectName(u"tab_sistema")
        self.verticalLayout_7 = QVBoxLayout(self.tab_sistema)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_sistema = QScrollArea(self.tab_sistema)
        self.scrollArea_sistema.setObjectName(u"scrollArea_sistema")
        self.scrollArea_sistema.setEnabled(True)
        self.scrollArea_sistema.setStyleSheet(u"border:none")
        self.scrollArea_sistema.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_sistema.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_sistema.setWidgetResizable(True)
        self.scrollArea_sistema.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 687, 369))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_sistema.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_7.addWidget(self.scrollArea_sistema)

        self.tabWidget.addTab(self.tab_sistema, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_salvar_espelhado = QPushButton(self.frame)
        self.btn_salvar_espelhado.setObjectName(u"btn_salvar_espelhado")
        self.btn_salvar_espelhado.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.btn_salvar_espelhado.setFont(font5)
        self.btn_salvar_espelhado.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"background-color: rgb(136, 50, 101);\n"
"color: white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(156, 58, 117)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:rgb(143, 53, 107)\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_salvar_espelhado)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_tituloPrincipal.setText(QCoreApplication.translate("Form", u"Selecione os Decretos", None))
        self.lb_busca.setText(QCoreApplication.translate("Form", u"Busca", None))
        self.btn_busca.setText("")
        self.checkBox.setText(QCoreApplication.translate("Form", u"Selecionar Todos", None))
        self.lb_totalDecretos.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_analise), QCoreApplication.translate("Form", u"Em An\u00e1lise", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_enviado), QCoreApplication.translate("Form", u"E-mail Enviado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_metas), QCoreApplication.translate("Form", u"Metas Inseridas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sistema), QCoreApplication.translate("Form", u"Inserido no Sistema", None))
        self.btn_salvar_espelhado.setText(QCoreApplication.translate("Form", u"Salvar", None))
    # retranslateUi

