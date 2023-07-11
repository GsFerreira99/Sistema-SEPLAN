# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Espelhamento_SelectEWqqjv.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)
import media.resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(724, 748)
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
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(True)
        self.lb_tituloPrincipal.setFont(font)
        self.lb_tituloPrincipal.setStyleSheet(u"color: white;")
        self.lb_tituloPrincipal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_tituloPrincipal)


        self.verticalLayout.addWidget(self.Titulo)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radio_todos = QRadioButton(self.frame)
        self.radio_todos.setObjectName(u"radio_todos")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.radio_todos.setFont(font1)
        self.radio_todos.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.radio_todos)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radio_contatosDestino = QRadioButton(self.frame_2)
        self.radio_contatosDestino.setObjectName(u"radio_contatosDestino")
        self.radio_contatosDestino.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_contatosDestino, 6, 0, 1, 1)

        self.radio_metaOrigemAtual = QRadioButton(self.frame_2)
        self.radio_metaOrigemAtual.setObjectName(u"radio_metaOrigemAtual")
        self.radio_metaOrigemAtual.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_metaOrigemAtual, 1, 0, 1, 1)

        self.radio_permaneceMeta = QRadioButton(self.frame_2)
        self.radio_permaneceMeta.setObjectName(u"radio_permaneceMeta")
        self.radio_permaneceMeta.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_permaneceMeta, 2, 0, 1, 1)

        self.check_naoGeraEmail = QCheckBox(self.frame_2)
        self.check_naoGeraEmail.setObjectName(u"check_naoGeraEmail")
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(13)
        self.check_naoGeraEmail.setFont(font2)

        self.gridLayout.addWidget(self.check_naoGeraEmail, 4, 2, 1, 1)

        self.radio_statusEnviado = QRadioButton(self.frame_2)
        self.radio_statusEnviado.setObjectName(u"radio_statusEnviado")
        self.radio_statusEnviado.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_statusEnviado, 8, 0, 1, 1)

        self.radio_metaDestinoAtual = QRadioButton(self.frame_2)
        self.radio_metaDestinoAtual.setObjectName(u"radio_metaDestinoAtual")
        self.radio_metaDestinoAtual.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_metaDestinoAtual, 1, 4, 1, 1)

        self.frame_19 = QFrame(self.frame_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setEnabled(False)
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
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.lb_metaAnulado_titulo.setFont(font3)

        self.verticalLayout_16.addWidget(self.lb_metaAnulado_titulo)

        self.input_metaAnulado = QLineEdit(self.frame_19)
        self.input_metaAnulado.setObjectName(u"input_metaAnulado")
        self.input_metaAnulado.setEnabled(False)
        self.input_metaAnulado.setMinimumSize(QSize(0, 25))
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(10)
        self.input_metaAnulado.setFont(font4)
        self.input_metaAnulado.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.verticalLayout_16.addWidget(self.input_metaAnulado)


        self.gridLayout.addWidget(self.frame_19, 3, 2, 1, 1)

        self.radio_metaSuplementadoDestino = QRadioButton(self.frame_2)
        self.radio_metaSuplementadoDestino.setObjectName(u"radio_metaSuplementadoDestino")
        self.radio_metaSuplementadoDestino.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_metaSuplementadoDestino, 3, 4, 1, 1)

        self.radio_contatosOrigem = QRadioButton(self.frame_2)
        self.radio_contatosOrigem.setObjectName(u"radio_contatosOrigem")
        self.radio_contatosOrigem.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_contatosOrigem, 7, 0, 1, 1)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setEnabled(False)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMaximumSize(QSize(16777215, 250))
        font5 = QFont()
        font5.setPointSize(8)
        self.frame_17.setFont(font5)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_17)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setContentsMargins(30, 0, 0, 0)
        self.label_23 = QLabel(self.frame_17)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setFamilies([u"Calibri"])
        font6.setPointSize(13)
        font6.setBold(False)
        self.label_23.setFont(font6)

        self.gridLayout_2.addWidget(self.label_23, 0, 0, 1, 1)

        self.input_origem_status1 = QLineEdit(self.frame_17)
        self.input_origem_status1.setObjectName(u"input_origem_status1")
        self.input_origem_status1.setMinimumSize(QSize(0, 25))
        self.input_origem_status1.setFont(font4)
        self.input_origem_status1.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_status1, 1, 2, 1, 1)

        self.input_origem_contato1 = QLineEdit(self.frame_17)
        self.input_origem_contato1.setObjectName(u"input_origem_contato1")
        self.input_origem_contato1.setMinimumSize(QSize(0, 25))
        self.input_origem_contato1.setFont(font4)
        self.input_origem_contato1.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_contato1, 1, 1, 1, 1)

        self.input_origem_contato2 = QLineEdit(self.frame_17)
        self.input_origem_contato2.setObjectName(u"input_origem_contato2")
        self.input_origem_contato2.setMinimumSize(QSize(0, 25))
        self.input_origem_contato2.setFont(font4)
        self.input_origem_contato2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_contato2, 2, 1, 1, 1)

        self.input_origem_contato3 = QLineEdit(self.frame_17)
        self.input_origem_contato3.setObjectName(u"input_origem_contato3")
        self.input_origem_contato3.setMinimumSize(QSize(0, 25))
        self.input_origem_contato3.setFont(font4)
        self.input_origem_contato3.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_contato3, 3, 1, 1, 1)

        self.input_origem_status2 = QLineEdit(self.frame_17)
        self.input_origem_status2.setObjectName(u"input_origem_status2")
        self.input_origem_status2.setMinimumSize(QSize(0, 25))
        self.input_origem_status2.setFont(font4)
        self.input_origem_status2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_2.addWidget(self.input_origem_status2, 2, 2, 1, 1)

        self.input_origem_status3 = QLineEdit(self.frame_17)
        self.input_origem_status3.setObjectName(u"input_origem_status3")
        self.input_origem_status3.setMinimumSize(QSize(0, 25))
        self.input_origem_status3.setFont(font4)
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
        self.inputDate_origem1.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(6, 0, 0)))
        self.inputDate_origem1.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.inputDate_origem1, 1, 0, 1, 1)

        self.inputDate_origem2 = QDateEdit(self.frame_17)
        self.inputDate_origem2.setObjectName(u"inputDate_origem2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputDate_origem2.sizePolicy().hasHeightForWidth())
        self.inputDate_origem2.setSizePolicy(sizePolicy1)
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
        self.inputDate_origem2.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(6, 0, 0)))
        self.inputDate_origem2.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.inputDate_origem2, 2, 0, 1, 1)

        self.inputDate_origem3 = QDateEdit(self.frame_17)
        self.inputDate_origem3.setObjectName(u"inputDate_origem3")
        sizePolicy1.setHeightForWidth(self.inputDate_origem3.sizePolicy().hasHeightForWidth())
        self.inputDate_origem3.setSizePolicy(sizePolicy1)
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
        self.inputDate_origem3.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(6, 0, 0)))
        self.inputDate_origem3.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.inputDate_origem3, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_17, 7, 2, 1, 4)

        self.radio_dataEmail = QRadioButton(self.frame_2)
        self.radio_dataEmail.setObjectName(u"radio_dataEmail")
        self.radio_dataEmail.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_dataEmail, 5, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setEnabled(False)
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
        self.lb_metaOrigemAtual_titulo.setFont(font3)

        self.verticalLayout_13.addWidget(self.lb_metaOrigemAtual_titulo)

        self.input_metaOrigemAtual = QLineEdit(self.frame_14)
        self.input_metaOrigemAtual.setObjectName(u"input_metaOrigemAtual")
        self.input_metaOrigemAtual.setEnabled(False)
        self.input_metaOrigemAtual.setMinimumSize(QSize(0, 25))
        self.input_metaOrigemAtual.setFont(font4)
        self.input_metaOrigemAtual.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.verticalLayout_13.addWidget(self.input_metaOrigemAtual)


        self.gridLayout.addWidget(self.frame_14, 1, 2, 1, 1)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setEnabled(False)
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
        self.lb_metaDestinoAtual_titulo.setFont(font3)

        self.verticalLayout_14.addWidget(self.lb_metaDestinoAtual_titulo)

        self.input_metaOrigemAtual_2 = QLineEdit(self.frame_15)
        self.input_metaOrigemAtual_2.setObjectName(u"input_metaOrigemAtual_2")
        self.input_metaOrigemAtual_2.setEnabled(False)
        self.input_metaOrigemAtual_2.setMinimumSize(QSize(0, 25))
        self.input_metaOrigemAtual_2.setFont(font4)
        self.input_metaOrigemAtual_2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.verticalLayout_14.addWidget(self.input_metaOrigemAtual_2)


        self.gridLayout.addWidget(self.frame_15, 1, 5, 1, 1)

        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setEnabled(False)
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
        font7 = QFont()
        font7.setFamilies([u"Calibri"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.lb_dataInicial_titulo.setFont(font7)

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
        self.inputDate_emailInicial.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(6, 0, 0)))
        self.inputDate_emailInicial.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.inputDate_emailInicial, 2, 0, 1, 1)

        self.input_origem_contato1_2 = QLineEdit(self.frame_16)
        self.input_origem_contato1_2.setObjectName(u"input_origem_contato1_2")
        self.input_origem_contato1_2.setMinimumSize(QSize(0, 25))
        self.input_origem_contato1_2.setFont(font4)
        self.input_origem_contato1_2.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.gridLayout_4.addWidget(self.input_origem_contato1_2, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_16, 5, 2, 1, 1)

        self.radio_metaSuplementadoOrigem = QRadioButton(self.frame_2)
        self.radio_metaSuplementadoOrigem.setObjectName(u"radio_metaSuplementadoOrigem")
        self.radio_metaSuplementadoOrigem.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_metaSuplementadoOrigem, 3, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setEnabled(False)
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
        self.lb_metaSuplementado_titulo.setFont(font3)

        self.verticalLayout_17.addWidget(self.lb_metaSuplementado_titulo)

        self.input_metaSuplementado = QLineEdit(self.frame_20)
        self.input_metaSuplementado.setObjectName(u"input_metaSuplementado")
        self.input_metaSuplementado.setEnabled(False)
        self.input_metaSuplementado.setMinimumSize(QSize(0, 25))
        self.input_metaSuplementado.setFont(font4)
        self.input_metaSuplementado.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(161, 150, 170)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(161, 150, 170)\n"
"}")

        self.verticalLayout_17.addWidget(self.input_metaSuplementado)


        self.gridLayout.addWidget(self.frame_20, 3, 5, 1, 1)

        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setEnabled(False)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMaximumSize(QSize(16777215, 250))
        self.frame_18.setFont(font5)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_18)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(30)
        self.gridLayout_3.setContentsMargins(30, 0, 0, 0)
        self.inputDate_destino1 = QDateEdit(self.frame_18)
        self.inputDate_destino1.setObjectName(u"inputDate_destino1")
        sizePolicy1.setHeightForWidth(self.inputDate_destino1.sizePolicy().hasHeightForWidth())
        self.inputDate_destino1.setSizePolicy(sizePolicy1)
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
        self.inputDate_destino1.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(6, 0, 0)))
        self.inputDate_destino1.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.inputDate_destino1, 1, 0, 1, 1)

        self.input_destino_contato1 = QLineEdit(self.frame_18)
        self.input_destino_contato1.setObjectName(u"input_destino_contato1")
        self.input_destino_contato1.setMinimumSize(QSize(0, 25))
        self.input_destino_contato1.setFont(font4)
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
        self.input_destino_status3.setFont(font4)
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
        self.input_destino_status1.setFont(font4)
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
        self.input_destino_contato2.setFont(font4)
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
        self.input_destino_status2.setFont(font4)
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
        sizePolicy1.setHeightForWidth(self.inputDate_destino2.sizePolicy().hasHeightForWidth())
        self.inputDate_destino2.setSizePolicy(sizePolicy1)
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
        self.inputDate_destino2.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(6, 0, 0)))
        self.inputDate_destino2.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.inputDate_destino2, 3, 0, 1, 1)

        self.input_destino_contato3 = QLineEdit(self.frame_18)
        self.input_destino_contato3.setObjectName(u"input_destino_contato3")
        self.input_destino_contato3.setMinimumSize(QSize(0, 25))
        self.input_destino_contato3.setFont(font4)
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
        self.label_24.setEnabled(False)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMaximumSize(QSize(16777215, 20))
        self.label_24.setFont(font6)

        self.gridLayout_3.addWidget(self.label_24, 0, 0, 1, 1)

        self.inputDate_destino3 = QDateEdit(self.frame_18)
        self.inputDate_destino3.setObjectName(u"inputDate_destino3")
        sizePolicy1.setHeightForWidth(self.inputDate_destino3.sizePolicy().hasHeightForWidth())
        self.inputDate_destino3.setSizePolicy(sizePolicy1)
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
        self.inputDate_destino3.setDateTime(QDateTime(QDate(2022, 6, 7), QTime(6, 0, 0)))
        self.inputDate_destino3.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.inputDate_destino3, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_18, 6, 2, 1, 4)

        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 50))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.inputCheck_emailEnviado = QCheckBox(self.frame_13)
        self.inputCheck_emailEnviado.setObjectName(u"inputCheck_emailEnviado")
        self.inputCheck_emailEnviado.setEnabled(False)
        self.inputCheck_emailEnviado.setFont(font2)

        self.horizontalLayout_3.addWidget(self.inputCheck_emailEnviado)

        self.radio_statusMetas = QRadioButton(self.frame_13)
        self.radio_statusMetas.setObjectName(u"radio_statusMetas")
        self.radio_statusMetas.setMaximumSize(QSize(20, 16777215))
        self.radio_statusMetas.setAutoExclusive(False)

        self.horizontalLayout_3.addWidget(self.radio_statusMetas)

        self.inputCheck_inseridoMetas = QCheckBox(self.frame_13)
        self.inputCheck_inseridoMetas.setObjectName(u"inputCheck_inseridoMetas")
        self.inputCheck_inseridoMetas.setEnabled(False)
        self.inputCheck_inseridoMetas.setFont(font2)

        self.horizontalLayout_3.addWidget(self.inputCheck_inseridoMetas)

        self.radio_statusSistema = QRadioButton(self.frame_13)
        self.radio_statusSistema.setObjectName(u"radio_statusSistema")
        self.radio_statusSistema.setMaximumSize(QSize(20, 16777215))
        self.radio_statusSistema.setAutoExclusive(False)

        self.horizontalLayout_3.addWidget(self.radio_statusSistema)

        self.inputCheck_atualizadoSistema = QCheckBox(self.frame_13)
        self.inputCheck_atualizadoSistema.setObjectName(u"inputCheck_atualizadoSistema")
        self.inputCheck_atualizadoSistema.setEnabled(False)
        self.inputCheck_atualizadoSistema.setFont(font2)

        self.horizontalLayout_3.addWidget(self.inputCheck_atualizadoSistema)


        self.gridLayout.addWidget(self.frame_13, 8, 2, 1, 4)

        self.check_permaneceMeta = QCheckBox(self.frame_2)
        self.check_permaneceMeta.setObjectName(u"check_permaneceMeta")
        self.check_permaneceMeta.setFont(font2)

        self.gridLayout.addWidget(self.check_permaneceMeta, 2, 2, 1, 1)

        self.radio_naoGeraEmail = QRadioButton(self.frame_2)
        self.radio_naoGeraEmail.setObjectName(u"radio_naoGeraEmail")
        self.radio_naoGeraEmail.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radio_naoGeraEmail, 4, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.btn_proximo = QPushButton(self.frame)
        self.btn_proximo.setObjectName(u"btn_proximo")
        self.btn_proximo.setMinimumSize(QSize(0, 40))
        font8 = QFont()
        font8.setFamilies([u"Calibri"])
        font8.setPointSize(15)
        font8.setBold(True)
        self.btn_proximo.setFont(font8)
        self.btn_proximo.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.btn_proximo)


        self.verticalLayout.addWidget(self.frame)

#if QT_CONFIG(shortcut)
        self.lb_metaAnulado_titulo.setBuddy(self.input_metaOrigemAtual)
        self.label_23.setBuddy(self.input_metaOrigemAtual)
        self.lb_metaOrigemAtual_titulo.setBuddy(self.input_metaOrigemAtual)
        self.lb_metaDestinoAtual_titulo.setBuddy(self.input_metaOrigemAtual_2)
        self.lb_dataInicial_titulo.setBuddy(self.input_metaOrigemAtual)
        self.lb_metaSuplementado_titulo.setBuddy(self.input_metaOrigemAtual)
        self.label_24.setBuddy(self.input_metaOrigemAtual)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lb_tituloPrincipal.setText(QCoreApplication.translate("Form", u"Selecione os Campos a Serem Espelhados", None))
        self.radio_todos.setText(QCoreApplication.translate("Form", u"Marcar Todos", None))
        self.radio_contatosDestino.setText("")
        self.radio_metaOrigemAtual.setText("")
        self.radio_permaneceMeta.setText("")
        self.check_naoGeraEmail.setText(QCoreApplication.translate("Form", u"N\u00e3o gera email", None))
        self.radio_statusEnviado.setText("")
        self.radio_metaDestinoAtual.setText("")
        self.lb_metaAnulado_titulo.setText(QCoreApplication.translate("Form", u"Nova Meta F\u00edsica Anulado (Origem)", None))
        self.radio_metaSuplementadoDestino.setText("")
        self.radio_contatosOrigem.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"Origem", None))
        self.input_origem_status1.setPlaceholderText(QCoreApplication.translate("Form", u"Status 1", None))
        self.input_origem_contato1.setText("")
        self.input_origem_contato1.setPlaceholderText(QCoreApplication.translate("Form", u"Contato 1", None))
        self.input_origem_contato2.setText("")
        self.input_origem_contato2.setPlaceholderText(QCoreApplication.translate("Form", u"Contato 2", None))
        self.input_origem_contato3.setText("")
        self.input_origem_contato3.setPlaceholderText(QCoreApplication.translate("Form", u"Contato 3", None))
        self.input_origem_status2.setPlaceholderText(QCoreApplication.translate("Form", u"Status 2", None))
        self.input_origem_status3.setPlaceholderText(QCoreApplication.translate("Form", u"Status 3", None))
        self.radio_dataEmail.setText("")
        self.lb_metaOrigemAtual_titulo.setText(QCoreApplication.translate("Form", u"Meta F\u00cdSICA de Origem ATUAL", None))
        self.lb_metaDestinoAtual_titulo.setText(QCoreApplication.translate("Form", u"Meta F\u00cdSICA de Destino ATUAL", None))
        self.lb_dataInicial_titulo.setText(QCoreApplication.translate("Form", u"Data Email Inicial", None))
        self.input_origem_contato1_2.setText("")
        self.input_origem_contato1_2.setPlaceholderText(QCoreApplication.translate("Form", u"Destinat\u00e1rios", None))
        self.radio_metaSuplementadoOrigem.setText("")
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
        self.inputCheck_emailEnviado.setText(QCoreApplication.translate("Form", u"E-mail Enviado", None))
        self.radio_statusMetas.setText("")
        self.inputCheck_inseridoMetas.setText(QCoreApplication.translate("Form", u"Inserido Metas", None))
        self.radio_statusSistema.setText("")
        self.inputCheck_atualizadoSistema.setText(QCoreApplication.translate("Form", u"Atualizado Sistema", None))
        self.check_permaneceMeta.setText(QCoreApplication.translate("Form", u"Permanece a mesma meta", None))
        self.radio_naoGeraEmail.setText("")
        self.btn_proximo.setText(QCoreApplication.translate("Form", u"Pr\u00f3ximo", None))
    # retranslateUi

