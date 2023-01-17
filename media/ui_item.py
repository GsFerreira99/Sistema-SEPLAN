# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ItemTabelaGTcTtC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import media.resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(905, 269)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 0))
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"	border:none\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"border: 1px solid rgb(238, 238, 238)	;\n"
"border-left: 3px solid rgb(109, 49, 162);\n"
"	\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 0, 0)
        self.frame_conteudo = QFrame(self.frame_4)
        self.frame_conteudo.setObjectName(u"frame_conteudo")
        self.frame_conteudo.setMaximumSize(QSize(16777215, 60))
        self.frame_conteudo.setStyleSheet(u"border:none")
        self.frame_conteudo.setFrameShape(QFrame.StyledPanel)
        self.frame_conteudo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_conteudo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_3 = QFrame(self.frame_conteudo)
        self.content_3.setObjectName(u"content_3")
        sizePolicy1.setHeightForWidth(self.content_3.sizePolicy().hasHeightForWidth())
        self.content_3.setSizePolicy(sizePolicy1)
        self.content_3.setMaximumSize(QSize(16777215, 30))
        self.content_3.setFrameShape(QFrame.StyledPanel)
        self.content_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.content_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 9, -1, 0)
        self.check_relatorio = QCheckBox(self.content_3)
        self.check_relatorio.setObjectName(u"check_relatorio")
        self.check_relatorio.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_6.addWidget(self.check_relatorio)

        self.lb_status = QLabel(self.content_3)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMaximumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lb_status.setFont(font)
        self.lb_status.setStyleSheet(u"image: url(:/icons/alerta.png);\n"
"border-radius: 100px;\n"
"")

        self.horizontalLayout_6.addWidget(self.lb_status)

        self.lb_data_3 = QLabel(self.content_3)
        self.lb_data_3.setObjectName(u"lb_data_3")
        self.lb_data_3.setFont(font)
        self.lb_data_3.setStyleSheet(u"border: none")

        self.horizontalLayout_6.addWidget(self.lb_data_3)

        self.lb_decreto_3 = QLabel(self.content_3)
        self.lb_decreto_3.setObjectName(u"lb_decreto_3")
        self.lb_decreto_3.setFont(font)
        self.lb_decreto_3.setStyleSheet(u"border: none")

        self.horizontalLayout_6.addWidget(self.lb_decreto_3)


        self.verticalLayout_2.addWidget(self.content_3)

        self.content = QFrame(self.frame_conteudo)
        self.content.setObjectName(u"content")
        sizePolicy1.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy1)
        self.content.setMaximumSize(QSize(16777215, 30))
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, -1, -1, -1)
        self.lb_decreto = QLabel(self.content)
        self.lb_decreto.setObjectName(u"lb_decreto")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.lb_decreto.setFont(font1)
        self.lb_decreto.setStyleSheet(u"border: none")

        self.horizontalLayout_3.addWidget(self.lb_decreto)

        self.lb_data = QLabel(self.content)
        self.lb_data.setObjectName(u"lb_data")
        self.lb_data.setFont(font1)
        self.lb_data.setStyleSheet(u"border: none")

        self.horizontalLayout_3.addWidget(self.lb_data)


        self.verticalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.frame_conteudo)

        self.frame_detalhes = QFrame(self.frame_4)
        self.frame_detalhes.setObjectName(u"frame_detalhes")
        self.frame_detalhes.setMaximumSize(QSize(16777215, 200))
        self.frame_detalhes.setStyleSheet(u"border:none")
        self.frame_detalhes.setFrameShape(QFrame.StyledPanel)
        self.frame_detalhes.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_detalhes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setContentsMargins(25, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_detalhes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: none")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_orgao_destino_3 = QLabel(self.frame_3)
        self.lb_orgao_destino_3.setObjectName(u"lb_orgao_destino_3")
        self.lb_orgao_destino_3.setMaximumSize(QSize(200, 20))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(12)
        self.lb_orgao_destino_3.setFont(font2)
        self.lb_orgao_destino_3.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_orgao_destino_3, 3, 0, 1, 1)

        self.lb_programa_origem = QLabel(self.frame_3)
        self.lb_programa_origem.setObjectName(u"lb_programa_origem")
        self.lb_programa_origem.setMaximumSize(QSize(230, 16777215))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(9)
        self.lb_programa_origem.setFont(font3)
        self.lb_programa_origem.setStyleSheet(u"margin-left: 20px")
        self.lb_programa_origem.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_programa_origem, 2, 1, 1, 1)

        self.lb_orgao_origem_3 = QLabel(self.frame_3)
        self.lb_orgao_origem_3.setObjectName(u"lb_orgao_origem_3")
        sizePolicy1.setHeightForWidth(self.lb_orgao_origem_3.sizePolicy().hasHeightForWidth())
        self.lb_orgao_origem_3.setSizePolicy(sizePolicy1)
        self.lb_orgao_origem_3.setMaximumSize(QSize(200, 20))
        self.lb_orgao_origem_3.setFont(font2)
        self.lb_orgao_origem_3.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_orgao_origem_3, 0, 0, 1, 1)

        self.lb_programa_destino = QLabel(self.frame_3)
        self.lb_programa_destino.setObjectName(u"lb_programa_destino")
        self.lb_programa_destino.setMaximumSize(QSize(230, 16777215))
        self.lb_programa_destino.setFont(font3)
        self.lb_programa_destino.setStyleSheet(u"margin-left: 20px")
        self.lb_programa_destino.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_programa_destino, 5, 1, 1, 1)

        self.lb_orgao_origem_4 = QLabel(self.frame_3)
        self.lb_orgao_origem_4.setObjectName(u"lb_orgao_origem_4")
        self.lb_orgao_origem_4.setMaximumSize(QSize(200, 20))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(10)
        self.lb_orgao_origem_4.setFont(font4)
        self.lb_orgao_origem_4.setStyleSheet(u"margin-left: 10px")
        self.lb_orgao_origem_4.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_orgao_origem_4, 1, 0, 1, 1)

        self.lb_orgao_destino = QLabel(self.frame_3)
        self.lb_orgao_destino.setObjectName(u"lb_orgao_destino")
        self.lb_orgao_destino.setMaximumSize(QSize(200, 50))
        self.lb_orgao_destino.setFont(font3)
        self.lb_orgao_destino.setStyleSheet(u"margin-left: 20px")
        self.lb_orgao_destino.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_orgao_destino, 5, 0, 1, 1)

        self.lb_orgao_origem = QLabel(self.frame_3)
        self.lb_orgao_origem.setObjectName(u"lb_orgao_origem")
        self.lb_orgao_origem.setMaximumSize(QSize(200, 50))
        self.lb_orgao_origem.setFont(font3)
        self.lb_orgao_origem.setStyleSheet(u"margin-left: 20px")
        self.lb_orgao_origem.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_orgao_origem, 2, 0, 1, 1)

        self.lb_orgao_destino_4 = QLabel(self.frame_3)
        self.lb_orgao_destino_4.setObjectName(u"lb_orgao_destino_4")
        self.lb_orgao_destino_4.setMaximumSize(QSize(200, 20))
        self.lb_orgao_destino_4.setFont(font3)
        self.lb_orgao_destino_4.setStyleSheet(u"margin-left: 10px")
        self.lb_orgao_destino_4.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_orgao_destino_4, 4, 0, 1, 1)

        self.lb_programa_destino_3 = QLabel(self.frame_3)
        self.lb_programa_destino_3.setObjectName(u"lb_programa_destino_3")
        self.lb_programa_destino_3.setMaximumSize(QSize(230, 16777215))
        self.lb_programa_destino_3.setFont(font3)
        self.lb_programa_destino_3.setStyleSheet(u"border:none")
        self.lb_programa_destino_3.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_programa_destino_3, 4, 1, 1, 1)

        self.lb_programa_origem_3 = QLabel(self.frame_3)
        self.lb_programa_origem_3.setObjectName(u"lb_programa_origem_3")
        self.lb_programa_origem_3.setMaximumSize(QSize(230, 16777215))
        self.lb_programa_origem_3.setFont(font3)
        self.lb_programa_origem_3.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lb_programa_origem_3, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 3, 1)

        self.btn_detalhes = QPushButton(self.frame_detalhes)
        self.btn_detalhes.setObjectName(u"btn_detalhes")
        sizePolicy.setHeightForWidth(self.btn_detalhes.sizePolicy().hasHeightForWidth())
        self.btn_detalhes.setSizePolicy(sizePolicy)
        self.btn_detalhes.setMaximumSize(QSize(50, 16777215))
        self.btn_detalhes.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	image: url(:/icons/drop-down.png);\n"
"	padding: 6px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 4px\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	padding: 5px\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_detalhes, 0, 2, 3, 1)

        self.frame = QFrame(self.frame_detalhes)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_acao_origem = QLabel(self.frame)
        self.lb_acao_origem.setObjectName(u"lb_acao_origem")
        self.lb_acao_origem.setMaximumSize(QSize(16777215, 20))
        self.lb_acao_origem.setFont(font3)
        self.lb_acao_origem.setStyleSheet(u"border: none")
        self.lb_acao_origem.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lb_acao_origem)

        self.lb_acao_origem_4 = QLabel(self.frame)
        self.lb_acao_origem_4.setObjectName(u"lb_acao_origem_4")
        self.lb_acao_origem_4.setMaximumSize(QSize(16777215, 20))
        self.lb_acao_origem_4.setFont(font3)
        self.lb_acao_origem_4.setStyleSheet(u"border: none")
        self.lb_acao_origem_4.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lb_acao_origem_4)

        self.lb_acao_origem_2 = QLabel(self.frame)
        self.lb_acao_origem_2.setObjectName(u"lb_acao_origem_2")
        self.lb_acao_origem_2.setFont(font3)
        self.lb_acao_origem_2.setStyleSheet(u"margin-left: 20px")
        self.lb_acao_origem_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lb_acao_origem_2)

        self.lb_acao_origem_3 = QLabel(self.frame)
        self.lb_acao_origem_3.setObjectName(u"lb_acao_origem_3")
        self.lb_acao_origem_3.setMaximumSize(QSize(16777215, 20))
        self.lb_acao_origem_3.setFont(font3)
        self.lb_acao_origem_3.setStyleSheet(u"border: none")
        self.lb_acao_origem_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lb_acao_origem_3)

        self.lb_acao_destino_2 = QLabel(self.frame)
        self.lb_acao_destino_2.setObjectName(u"lb_acao_destino_2")
        self.lb_acao_destino_2.setMaximumSize(QSize(16777215, 20))
        self.lb_acao_destino_2.setFont(font3)
        self.lb_acao_destino_2.setStyleSheet(u"border:none")
        self.lb_acao_destino_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lb_acao_destino_2)

        self.lb_acao_acao = QLabel(self.frame)
        self.lb_acao_acao.setObjectName(u"lb_acao_acao")
        self.lb_acao_acao.setFont(font3)
        self.lb_acao_acao.setStyleSheet(u"margin-left: 20px")
        self.lb_acao_acao.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lb_acao_acao)


        self.gridLayout.addWidget(self.frame, 0, 1, 3, 1)


        self.verticalLayout.addWidget(self.frame_detalhes)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.check_relatorio.setText("")
        self.lb_status.setText("")
        self.lb_data_3.setText(QCoreApplication.translate("Form", u"N\u00famero Decreto / Portaria", None))
        self.lb_decreto_3.setText(QCoreApplication.translate("Form", u"Data Decreto", None))
        self.lb_decreto.setText(QCoreApplication.translate("Form", u"57816", None))
        self.lb_data.setText(QCoreApplication.translate("Form", u"19/05/2022", None))
        self.lb_orgao_destino_3.setText(QCoreApplication.translate("Form", u"Destino", None))
        self.lb_programa_origem.setText(QCoreApplication.translate("Form", u"0229 - GEST\u00c3O PARTICIPATIVA E CIDADANIA", None))
        self.lb_orgao_origem_3.setText(QCoreApplication.translate("Form", u"Origem", None))
        self.lb_programa_destino.setText(QCoreApplication.translate("Form", u"201 - CULTURA PATRIM\u00d4NIO CULTURAL E TURISMO", None))
        self.lb_orgao_origem_4.setText(QCoreApplication.translate("Form", u"\u00d3rg\u00e3o:", None))
        self.lb_orgao_destino.setText(QCoreApplication.translate("Form", u"31 - SECULT", None))
        self.lb_orgao_origem.setText(QCoreApplication.translate("Form", u"11 - SEMGOV", None))
        self.lb_orgao_destino_4.setText(QCoreApplication.translate("Form", u"\u00d3rg\u00e3o", None))
        self.lb_programa_destino_3.setText(QCoreApplication.translate("Form", u"Programa", None))
        self.lb_programa_origem_3.setText(QCoreApplication.translate("Form", u"Programa:", None))
        self.btn_detalhes.setText("")
        self.lb_acao_origem.setText("")
        self.lb_acao_origem_4.setText(QCoreApplication.translate("Form", u"A\u00e7\u00e3o:", None))
        self.lb_acao_origem_2.setText(QCoreApplication.translate("Form", u"2033 - APOIO AS DEMANDAS DA SOCIEDADE CIVIL", None))
        self.lb_acao_origem_3.setText("")
        self.lb_acao_destino_2.setText(QCoreApplication.translate("Form", u"A\u00e7\u00e3o", None))
        self.lb_acao_acao.setText(QCoreApplication.translate("Form", u"2006 - PROMOVER E DESENVOLVER O AMBIENTE CULTURAL", None))
    # retranslateUi

