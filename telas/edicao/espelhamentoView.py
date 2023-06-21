from media.ui_espelhamento import Ui_Form
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton
from telas.dashboard.itemTabelaView import ItemTabelaView
from PyQt5.QtCore import Qt


class EspelhamentoView(Ui_Form, QDialog):

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.ui = ui

        self.setModal(True)

        self.botoes: {int: QPushButton} = {}
        self.botoes_pag: [QPushButton] = [self.pag_1, self.pag_2, self.pag_3, self.pag_4, self.pag_5]

        self.pag_anterior.clicked.connect(lambda: self.proximo_anterior(False))
        self.pag_proximo.clicked.connect(lambda: self.proximo_anterior(True))

        self.pag_inicio.clicked.connect(lambda: self.pagi_inicio_fim(True))
        self.pag_fim.clicked.connect(lambda: self.pagi_inicio_fim(False))

        self.paginacao_ativa = 1
        self.dados_pag = []
        self._items = []

    def preencher_scroll(self, dados, id: int, tipo: bool = True, esp:bool=True):
        self.limpar()
        self.widget = QWidget()
        try:
            self.vbox.deleteLater()
        except Exception as exeption:
            pass
        self.vbox = QVBoxLayout()
        items = []
        self._items = []

        if tipo is True:
            dados = dados[id - 1]

        for j, i in enumerate(dados.index):
            try:
                object = ItemTabelaView(self.ui, dados.iloc[j])
                if self.checkBox.isChecked():
                    object.check_relatorio.setChecked(True)
                items.append(object)
                self.vbox.addWidget(object)
                if esp is True:
                    object.ocultar_seta()

            except IndexError:
                pass
            except TypeError:
                pass
            except RuntimeError:
                pass

        self.verticalSpacer = QSpacerItem(2000, 40, QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.vbox.addSpacerItem(self.verticalSpacer)
        self.widget.setLayout(self.vbox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignTop)
        self.scrollArea.setWidget(self.widget)

        self._items = items
        return items

    def verificar_tela(self, filtro):
        self.reset_css_button()
        if filtro == 'INSERIDO SISTEMA':
            self.btn_inserido.setStyleSheet("QPushButton {	 background:rgb(136, 50, 101); 	color: white; border: 1px solid lightgray; 	  padding: 15px 30px;}")
        elif filtro == 'ANÁLISE':
            self.btn_analise.setStyleSheet("QPushButton {	 background:rgb(136, 50, 101); 	color: white; border: 1px solid lightgray; 	  padding: 15px 30px;}")
        elif filtro == 'METAS INSERIDAS':
            self.btn_metas.setStyleSheet("QPushButton {	 background:rgb(136, 50, 101); 	color: white; border: 1px solid lightgray; 	  padding: 15px 30px;}")
        elif filtro == 'EMAIL ENVIADO':
            self.btn_email.setStyleSheet("QPushButton {	 background:rgb(136, 50, 101); 	color: white; border: 1px solid lightgray; 	  padding: 15px 30px;}")
        elif filtro == 'TODOS':
            self.btn_todos.setStyleSheet("QPushButton {	 background:rgb(136, 50, 101); 	color: white; border: 1px solid lightgray; 	  padding: 15px 30px;}")

    def reset_css_button(self):
        items = [self.btn_todos, self.btn_analise, self.btn_metas, self.btn_inserido, self.btn_email]
        for btn in items:
            btn.setStyleSheet("QPushButton {	background: rgb(230, 230, 230);  	 border: 1px solid lightgray; 	  padding: 15px 30px;}QPushButton:hover {	 background:rgb(136, 50, 101); 	color: white}")

    def preencher_todos(self, widgets):
        if len(widgets) == 0:
            return
        widget = QWidget()
        vbox = QVBoxLayout()

        for i in widgets[0]:
            try:
                vbox.addWidget(i)
            except IndexError:
                pass

        verticalSpacer = QSpacerItem(2000, 40, QSizePolicy.Maximum, QSizePolicy.Expanding)
        vbox.addSpacerItem(verticalSpacer)
        widget.setLayout(vbox)
        self.scrollArea_todos.setWidgetResizable(True)
        self.scrollArea_todos.setAlignment(Qt.AlignTop)
        self.scrollArea_todos.setWidget(widget)

    def limpar(self):
        for i in self._items:
            i.deleteLater()
            i = None
        self._items = []

    def paginacao(self, dados):
        self.pagi = (round(len(dados) / 10)) + 1
        self.definir_botoes()
        self.dados_paginacao(dados)
        return self.pagi

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
        self.ui._items = self.preencher_scroll(self.dados_pag, self.paginacao_ativa)

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
                self.botoes_pag[id - 1].setStyleSheet(u"QPushButton{\n"
                                                      "	color: white;\n"
                                                      "	background-color: rgb(76, 34, 112);\n"
                                                      "}")
            except:
                pass

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
        self.ui._items = self.preencher_scroll(self.dados_pag, self.paginacao_ativa)

    def verificar_check(self):
        if self.checkBox.isChecked() is True:
            self.checkBox.setChecked(False)


    def atualizar_texto_botoes(self, dados:[str]):
        self.pag_1.setText(str(dados[0]))
        self.pag_2.setText(str(dados[1]))
        self.pag_3.setText(str(dados[2]))
        self.pag_4.setText(str(dados[3]))
        self.pag_5.setText(str(dados[4]))

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

    def dados_paginacao(self, dados):
        pages = {1:[]}
        pagNum = 10
        count = 1
        for num in dados.index:
            pages[len(pages)].append(dados.iloc[num])
            if count == pagNum:
                count =1
                pages[len(pages)] = []
            else:
                count+=1
        return pages


