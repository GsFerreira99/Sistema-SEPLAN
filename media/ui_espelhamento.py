# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EspelhamentosiQABl.ui'
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
        Form.resize(724, 805)
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

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.btn_todos = QPushButton(self.frame_4)
        self.btn_todos.setObjectName(u"btn_todos")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_todos.sizePolicy().hasHeightForWidth())
        self.btn_todos.setSizePolicy(sizePolicy2)
        self.btn_todos.setMinimumSize(QSize(0, 45))
        self.btn_todos.setMaximumSize(QSize(16777215, 45))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_todos.setFont(font4)
        self.btn_todos.setStyleSheet(u"QPushButton {\n"
"	background: rgb(230, 230, 230); \n"
" 	 border: 1px solid lightgray; \n"
"	  padding: 15px 46px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	 background:rgb(136, 50, 101); \n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:selected {\n"
" background:rgb(136, 50, 101); \n"
"color: white;\n"
"  margin-bottom: -1px; \n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_todos)

        self.btn_analise = QPushButton(self.frame_4)
        self.btn_analise.setObjectName(u"btn_analise")
        sizePolicy2.setHeightForWidth(self.btn_analise.sizePolicy().hasHeightForWidth())
        self.btn_analise.setSizePolicy(sizePolicy2)
        self.btn_analise.setMinimumSize(QSize(0, 45))
        self.btn_analise.setMaximumSize(QSize(16777215, 45))
        self.btn_analise.setFont(font4)
        self.btn_analise.setStyleSheet(u"QPushButton {\n"
"	background: rgb(230, 230, 230); \n"
" 	 border: 1px solid lightgray; \n"
"	  padding: 15px 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	 background:rgb(136, 50, 101); \n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:selected {\n"
" background:rgb(136, 50, 101); \n"
"color: white;\n"
"  margin-bottom: -1px; \n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_analise)

        self.btn_email = QPushButton(self.frame_4)
        self.btn_email.setObjectName(u"btn_email")
        sizePolicy2.setHeightForWidth(self.btn_email.sizePolicy().hasHeightForWidth())
        self.btn_email.setSizePolicy(sizePolicy2)
        self.btn_email.setMinimumSize(QSize(0, 45))
        self.btn_email.setMaximumSize(QSize(16777215, 45))
        self.btn_email.setFont(font4)
        self.btn_email.setStyleSheet(u"QPushButton {\n"
"	background: rgb(230, 230, 230); \n"
" 	 border: 1px solid lightgray; \n"
"	  padding: 15px 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	 background:rgb(136, 50, 101); \n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:selected {\n"
" background:rgb(136, 50, 101); \n"
"color: white;\n"
"  margin-bottom: -1px; \n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_email)

        self.btn_metas = QPushButton(self.frame_4)
        self.btn_metas.setObjectName(u"btn_metas")
        sizePolicy2.setHeightForWidth(self.btn_metas.sizePolicy().hasHeightForWidth())
        self.btn_metas.setSizePolicy(sizePolicy2)
        self.btn_metas.setMinimumSize(QSize(0, 45))
        self.btn_metas.setMaximumSize(QSize(16777215, 45))
        self.btn_metas.setFont(font4)
        self.btn_metas.setStyleSheet(u"QPushButton {\n"
"	background: rgb(230, 230, 230); \n"
" 	 border: 1px solid lightgray; \n"
"	  padding: 15px 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	 background:rgb(136, 50, 101); \n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:selected {\n"
" background:rgb(136, 50, 101); \n"
"color: white;\n"
"  margin-bottom: -1px; \n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_metas)

        self.btn_inserido = QPushButton(self.frame_4)
        self.btn_inserido.setObjectName(u"btn_inserido")
        sizePolicy2.setHeightForWidth(self.btn_inserido.sizePolicy().hasHeightForWidth())
        self.btn_inserido.setSizePolicy(sizePolicy2)
        self.btn_inserido.setMinimumSize(QSize(0, 45))
        self.btn_inserido.setMaximumSize(QSize(16777215, 45))
        self.btn_inserido.setFont(font4)
        self.btn_inserido.setStyleSheet(u"QPushButton {\n"
"	background: rgb(230, 230, 230); \n"
" 	 border: 1px solid lightgray; \n"
"	  padding: 15px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	 background:rgb(136, 50, 101); \n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:selected {\n"
" background:rgb(136, 50, 101); \n"
"color: white;\n"
"  margin-bottom: -1px; \n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_inserido)


        self.verticalLayout.addWidget(self.frame_4)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setStyleSheet(u"border:none")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 707, 432))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_12 = QFrame(self.frame)
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
        font5 = QFont()
        font5.setPointSize(11)
        self.pag_inicio.setFont(font5)
        self.pag_inicio.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pag_inicio)

        self.pag_anterior = QPushButton(self.frame_paginacao)
        self.pag_anterior.setObjectName(u"pag_anterior")
        self.pag_anterior.setMinimumSize(QSize(30, 30))
        self.pag_anterior.setMaximumSize(QSize(30, 30))
        self.pag_anterior.setFont(font5)
        self.pag_anterior.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pag_anterior)

        self.frame_pagMeio = QFrame(self.frame_paginacao)
        self.frame_pagMeio.setObjectName(u"frame_pagMeio")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_pagMeio.sizePolicy().hasHeightForWidth())
        self.frame_pagMeio.setSizePolicy(sizePolicy3)
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
        self.pag_1.setFont(font5)
        self.pag_1.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: rgb(76, 34, 112);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pag_1)

        self.pag_2 = QPushButton(self.frame_pagMeio)
        self.pag_2.setObjectName(u"pag_2")
        self.pag_2.setMinimumSize(QSize(30, 30))
        self.pag_2.setMaximumSize(QSize(30, 30))
        self.pag_2.setFont(font5)
        self.pag_2.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pag_2)

        self.pag_3 = QPushButton(self.frame_pagMeio)
        self.pag_3.setObjectName(u"pag_3")
        self.pag_3.setMinimumSize(QSize(30, 30))
        self.pag_3.setMaximumSize(QSize(30, 30))
        self.pag_3.setFont(font5)
        self.pag_3.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pag_3)

        self.pag_4 = QPushButton(self.frame_pagMeio)
        self.pag_4.setObjectName(u"pag_4")
        self.pag_4.setMinimumSize(QSize(30, 30))
        self.pag_4.setMaximumSize(QSize(30, 30))
        self.pag_4.setFont(font5)
        self.pag_4.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pag_4)

        self.pag_5 = QPushButton(self.frame_pagMeio)
        self.pag_5.setObjectName(u"pag_5")
        self.pag_5.setMinimumSize(QSize(30, 30))
        self.pag_5.setMaximumSize(QSize(30, 30))
        self.pag_5.setFont(font5)
        self.pag_5.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.pag_5)


        self.horizontalLayout_7.addWidget(self.frame_pagMeio)

        self.pag_proximo = QPushButton(self.frame_paginacao)
        self.pag_proximo.setObjectName(u"pag_proximo")
        self.pag_proximo.setMinimumSize(QSize(30, 30))
        self.pag_proximo.setMaximumSize(QSize(30, 30))
        self.pag_proximo.setFont(font5)
        self.pag_proximo.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pag_proximo)

        self.pag_fim = QPushButton(self.frame_paginacao)
        self.pag_fim.setObjectName(u"pag_fim")
        self.pag_fim.setMinimumSize(QSize(30, 30))
        self.pag_fim.setMaximumSize(QSize(30, 30))
        self.pag_fim.setFont(font5)
        self.pag_fim.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pag_fim)


        self.horizontalLayout_6.addWidget(self.frame_paginacao)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.btn_salvar_espelhado = QPushButton(self.frame)
        self.btn_salvar_espelhado.setObjectName(u"btn_salvar_espelhado")
        self.btn_salvar_espelhado.setMinimumSize(QSize(0, 40))
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(15)
        font6.setBold(True)
        font6.setWeight(75)
        self.btn_salvar_espelhado.setFont(font6)
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

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_tituloPrincipal.setText(QCoreApplication.translate("Form", u"Selecione os Decretos", None))
        self.lb_busca.setText(QCoreApplication.translate("Form", u"Busca", None))
        self.btn_busca.setText("")
        self.checkBox.setText(QCoreApplication.translate("Form", u"Selecionar Todos", None))
        self.lb_totalDecretos.setText("")
        self.btn_todos.setText(QCoreApplication.translate("Form", u"Todos", None))
        self.btn_analise.setText(QCoreApplication.translate("Form", u"Em An\u00e1lise", None))
        self.btn_email.setText(QCoreApplication.translate("Form", u"E-mail Enviado", None))
        self.btn_metas.setText(QCoreApplication.translate("Form", u"Metas Inseridas", None))
        self.btn_inserido.setText(QCoreApplication.translate("Form", u"Inserido no Sistema", None))
        self.pag_inicio.setText(QCoreApplication.translate("Form", u"<<", None))
        self.pag_anterior.setText(QCoreApplication.translate("Form", u"<", None))
        self.pag_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pag_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pag_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pag_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pag_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pag_proximo.setText(QCoreApplication.translate("Form", u">", None))
        self.pag_fim.setText(QCoreApplication.translate("Form", u">>", None))
        self.btn_salvar_espelhado.setText(QCoreApplication.translate("Form", u"Salvar", None))
    # retranslateUi

