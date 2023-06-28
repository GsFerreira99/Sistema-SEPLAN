# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MetricasTDQYfx.ui'
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
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import media.resource_rc
import media.resource

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(942, 690)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none")
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
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

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, 50, 50, 50)
        self.frame = QFrame(self.Content)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(75, 60, 75, 60)
        self.lb_score1 = QLabel(self.frame_2)
        self.lb_score1.setObjectName(u"lb_score1")
        self.lb_score1.setMinimumSize(QSize(0, 65))
        self.lb_score1.setMaximumSize(QSize(16777215, 65))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.lb_score1.setFont(font1)
        self.lb_score1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_score1)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.score_1 = QLabel(self.frame_5)
        self.score_1.setObjectName(u"score_1")
        self.score_1.setMinimumSize(QSize(250, 250))
        self.score_1.setMaximumSize(QSize(250, 250))
        font2 = QFont()
        font2.setPointSize(76)
        self.score_1.setFont(font2)
        self.score_1.setStyleSheet(u"QLabel {\n"
"border: 8px solid rgb(109, 49, 162);\n"
"border-radius: 120px;\n"
"\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: rgb(135, 111, 162);\n"
"}")
        self.score_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.score_1)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_busca = QLabel(self.frame_4)
        self.lb_busca.setObjectName(u"lb_busca")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.lb_busca.setFont(font3)

        self.horizontalLayout_3.addWidget(self.lb_busca)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(250, 35))
        self.comboBox.setStyleSheet(u"\n"
"QComboBox:focus {\n"
"	border: 1px solid rgb(10, 38, 71);\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{   \n"
"	image: url(:/icons/icons/cil-arrow-bottom.png);\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    border-top-right-radius: 9px;\n"
"	border-bottom-right-radius: 9px;\n"
"	background-color: rgb(109, 49, 162);\n"
"	width: 25px\n"
"}\n"
"\n"
"QComboBox::drop-down:hover \n"
"{\n"
"	background-color: rgb(89, 40, 134);\n"
"}\n"
"\n"
"QComboBox::drop-down:pressed \n"
"{\n"
"	background-color: rgb(149, 68, 225)\n"
"}")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.lb_filtro = QLabel(self.frame_4)
        self.lb_filtro.setObjectName(u"lb_filtro")
        self.lb_filtro.setMinimumSize(QSize(300, 0))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.lb_filtro.setFont(font4)
        self.lb_filtro.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_filtro)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(75, 60, 75, 60)
        self.lb_score2 = QLabel(self.frame_3)
        self.lb_score2.setObjectName(u"lb_score2")
        self.lb_score2.setMinimumSize(QSize(0, 65))
        self.lb_score2.setMaximumSize(QSize(16777215, 65))
        self.lb_score2.setFont(font1)
        self.lb_score2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_score2)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.score_2 = QLabel(self.frame_6)
        self.score_2.setObjectName(u"score_2")
        self.score_2.setMinimumSize(QSize(250, 250))
        self.score_2.setMaximumSize(QSize(250, 250))
        self.score_2.setFont(font2)
        self.score_2.setStyleSheet(u"QLabel {\n"
"border: 8px solid rgb(109, 49, 162);\n"
"border-radius: 120px;\n"
"\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: rgb(135, 111, 162);\n"
"}")
        self.score_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.score_2)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.Content)

        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MainWindow", None))
        self.btn_voltar.setText("")
        self.lb_tituloPrincipal.setText(QCoreApplication.translate("Form", u"M\u00e9tricas", None))
        self.lb_score1.setText(QCoreApplication.translate("Form", u"Score 1", None))
        self.score_1.setText(QCoreApplication.translate("Form", u"5.2", None))
        self.lb_busca.setText(QCoreApplication.translate("Form", u"Filtro: ", None))
        self.lb_filtro.setText(QCoreApplication.translate("Form", u"Filtro Atual: Todos", None))
        self.lb_score2.setText(QCoreApplication.translate("Form", u"Score 2", None))
        self.score_2.setText(QCoreApplication.translate("Form", u"5.2", None))
    # retranslateUi

