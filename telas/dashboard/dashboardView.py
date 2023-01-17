from cmath import e
from media.ui_dashboard import Ui_Form
from telas.dashboard.itemTabelaView import ItemTabelaView
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QFileDialog, QPushButton
from PyQt5.QtCore import Qt, QSize

import pandas as pd



class DashboardView(Ui_Form, QWidget):

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self._items = []
        self.vbox = QVBoxLayout()
        self.botoes: {int: QPushButton} = {}
        self.botoes_pag: [QPushButton] = [self.pag_1, self.pag_2, self.pag_3, self.pag_4, self.pag_5]

        self.pag_anterior.clicked.connect(lambda: self.proximo_anterior(False))
        self.pag_proximo.clicked.connect(lambda: self.proximo_anterior(True))

        self.pag_inicio.clicked.connect(lambda: self.pagi_inicio_fim(True))
        self.pag_fim.clicked.connect(lambda: self.pagi_inicio_fim(False))

        self.paginacao_ativa = 1
        self.dados_pag = []

        self.ui = ui
    
    def preencher_lb_todos(self, value):
        self.lb_cont_todos.setText(str(value))
    
    def preencher_lb_analise(self, value):
        self.lb_cont_analise.setText(str(value))
    
    def preencher_lb_metas(self, value):
        self.lb_cont_metas.setText(str(value))
    
    def preencher_lb_email(self, value):
        self.lb_cont_email.setText(str(value))
    
    def preencher_lb_inserido(self, value):
        self.lb_cont_inseridos.setText(str(value))

    def selecionar_plan(self):
        arquivo = QFileDialog.getOpenFileName()[0]
        if arquivo != '':
            with open('caminho.txt', 'w') as a:
                a.write(arquivo)
                a.close()
        self.ui.principalController.atualizar_contadores()

    def limpar(self):
            for i in self._items:
                i.deleteLater()
                i = None
            self._items = []

    def dados_paginacao(self, dados):
        pages = {1:[]}
        pagNum = int(self.comboBox.currentText())
        count = 1
        for num in dados.index:
            pages[len(pages)].append(dados.iloc[num])
            if count == pagNum:
                count =1
                pages[len(pages)] = []
            else:
                count+=1
        return pages

    def pagi_inicio_fim(self, tipo: bool):
        if tipo is True and self.pagi>5:
            self.paginacao_ativa = 1
            self.atualizar_texto_botoes([
                self.paginacao_ativa,
                self.paginacao_ativa+1,
                self.paginacao_ativa + 2,
                self.paginacao_ativa + 3,
                self.paginacao_ativa+4])
            self.click_botoes_pag(1)
        elif tipo is False and self.pagi>5 :
            self.paginacao_ativa = self.pagi
            self.atualizar_texto_botoes([
                self.paginacao_ativa - 4,
                self.paginacao_ativa - 3,
                self.paginacao_ativa - 2,
                self.paginacao_ativa - 1,
                self.paginacao_ativa])
            self.click_botoes_pag(5)
        self.preencher_scroll(self.dados_pag, self.paginacao_ativa)



    def proximo_anterior(self, tipo: bool):
        if tipo is True and self.paginacao_ativa<5and self.paginacao_ativa<self.pagi:
            self.paginacao_ativa+=1
            self.click_botoes_pag(self.paginacao_ativa)
        elif tipo is True and self.paginacao_ativa>=5and self.paginacao_ativa<=self.pagi:
            self.paginacao_ativa += 1
            self.atualizar_texto_botoes([
                self.paginacao_ativa-4,
                self.paginacao_ativa-3,
                self.paginacao_ativa-2,
                self.paginacao_ativa-1,
                self.paginacao_ativa])
        elif tipo is False and self.paginacao_ativa>=6and self.paginacao_ativa<=self.pagi:
            self.paginacao_ativa -= 1
            self.atualizar_texto_botoes([
                self.paginacao_ativa-4,
                self.paginacao_ativa-3,
                self.paginacao_ativa-2,
                self.paginacao_ativa-1,
                self.paginacao_ativa])
        elif tipo is False and self.paginacao_ativa!=1:
            self.paginacao_ativa -= 1
            self.click_botoes_pag(self.paginacao_ativa)
        self.preencher_scroll(self.dados_pag, self.paginacao_ativa)

    def atualizar_texto_botoes(self, dados:[str]):
        self.pag_1.setText(str(dados[0]))
        self.pag_2.setText(str(dados[1]))
        self.pag_3.setText(str(dados[2]))
        self.pag_4.setText(str(dados[3]))
        self.pag_5.setText(str(dados[4]))

    def click_botoes_pag(self, id: int):
        try:
            for i in self.botoes_pag:
                i.setStyleSheet(u"QPushButton {\n"
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
            self.botoes_pag[id-1].setStyleSheet(u"QPushButton{\n"
    "	color: white;\n"
    "	background-color: rgb(76, 34, 112);\n"
    "}")
        except:
            pass

    def paginacao(self, dados):
        self.pagi = (round(len(dados) / int(self.comboBox.currentText()))) +1
        self.definir_botoes()
        self.dados_paginacao(dados)
        return self.pagi

    def definir_botoes(self):
        for i in self.botoes_pag:
            i.setText("")
            i.setEnabled(False)
        try:
            if self.pagi == 0:
                self.botoes_pag[0].setText(str(self.pagi  + 1))
                self.botoes_pag[0].setEnabled(True)
            for i in range(self.pagi):
                self.botoes_pag[i].setText(str(i + 1))
                self.botoes_pag[i].setEnabled(True)
        except:
            pass

    def preencher_scroll(self, dados, id:int):
        self.limpar()
        self.widget = QWidget()
        self.vbox.deleteLater()
        self.vbox = QVBoxLayout()
        items = pd.DataFrame(columns={'ID', 'OBJETO'})

        dados = dados[id-1]

        for j, i in enumerate(dados.index):
            try:
                object = ItemTabelaView(self.ui, dados.iloc[j])
                self._items.append(object)
                d = pd.DataFrame(data={"ID": j+1, 'OBJETO': [object]}, index=[j+1])
                items = pd.concat([items, d])
                self.vbox.addWidget(object)
            except IndexError:
                pass

        self.verticalSpacer = QSpacerItem(2000, 40, QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.vbox.addSpacerItem(self.verticalSpacer)
        self.widget.setLayout(self.vbox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignTop)
        self.scrollArea.setWidget(self.widget)

        return items

    def filtro_scroll(self, dados):
        self.widget = QWidget()                 
        self.vbox = QVBoxLayout()               

        for i in range(dados.index.size):
            object = ItemTabelaView(self.ui, dados.iloc[i])
            self.vbox.addWidget(object)

        self.verticalSpacer = QSpacerItem(2000, 40, QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.vbox.addSpacerItem(self.verticalSpacer)
        self.widget.setLayout(self.vbox)

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignTop)
        self.scrollArea.setWidget(self.widget)

