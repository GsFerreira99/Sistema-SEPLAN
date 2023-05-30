from calendar import calendar
from datetime import datetime
from telas.dashboard.dashboardView import DashboardView
from funcoes.relatorio import Relatorio
from funcoes.relatorio_excel import Relatorio_xls
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from funcoes.importarDados import ImportarDados
from funcoes.dataBase import DataBase
from funcoes.poupUp import Erro
from funcoes.credenciais import carregar_credenciais

import calendar


class DashBoardController:

    def __init__(self, ui) -> object:
        """ Responsável por controlar tudo que acontece na tela Principal """
        self.ui = ui
        self.view = DashboardView(self.ui)

        self.credenciais_servidor()
        self._db.conectar()

        #self._dados = self._db.select_todos

        self.filtro_atual = 'TODOS'

        self.relatorio = []

        self.inserir_dados()

        self.view.btn_inserido.clicked.connect(lambda: self.filtrar('INSERIDO SISTEMA'))
        self.view.btn_analise.clicked.connect(lambda: self.filtrar('ANÁLISE'))
        self.view.btn_metas.clicked.connect(lambda: self.filtrar('METAS INSERIDAS'))
        self.view.btn_email.clicked.connect(lambda: self.filtrar('EMAIL ENVIADO'))
        self.view.btn_todos.clicked.connect(lambda: self.filtrar('TODOS'))

        self.view.checkBox.clicked.connect(lambda: self.marcar_todos())
        self.view.comboBox.currentIndexChanged.connect(lambda: self.filtrar(self.filtro_atual))


        self.view.btn_relatorio.clicked.connect(lambda: self.caminho_relatorio())
        self.view.btn_relatorio_excel.clicked.connect(lambda: self.caminho_relatorio_excel())
        self.view.btn_planilha.clicked.connect(lambda: self.selecionar_plan())

        self.view.btn_busca.clicked.connect(lambda: self.busca())
    
    def credenciais_servidor(self):
        dados = carregar_credenciais("credenciais.json")
        self._db = DataBase(dados['host'], dados['user'], dados['password'], dados['porta'])
        self.ui.db = self._db

    def selecionar_plan(self):
        arquivo = QFileDialog.getOpenFileName()[0]
        try:
            dados = ImportarDados(arquivo).retornar_lista_dados
            self._db.inserir_decreto(dados)
            self.inserir_dados()
            Erro("Planilha Importada com sucesso.", QMessageBox.Information)
        except FileNotFoundError:
            Erro("Planilha não encontrada", QMessageBox.Warning)

    def caminho_relatorio(self):
        if len(self.relatorio) > 0:
            try:
                arquivo = QFileDialog.getSaveFileName(caption="Exportar relatório em PDF", directory="", filter="PDF files (*.pdf)")[0]
            except FileNotFoundError:
                return
            try:
                if arquivo == "":
                     return
                if self.view.checkBox.isChecked() is True:
                    dados = self._db.select_todos
                    dados = dados[dados.id.isin(self.relatorio)]
                else:
                    dados = self._db.select_todos
                    dados = dados[dados.id.isin(self.relatorio)]
                Relatorio(arquivo, dados, self.filtro_atual)
                Erro("Relatório gerado com sucesso.", QMessageBox.Information)
            except ValueError:
                return
        else:
            Erro("Nenhum decreto selecionado.", QMessageBox.Information)

    def caminho_relatorio_excel(self):
        if len(self.relatorio) > 0:
            try:
                arquivo = QFileDialog.getSaveFileName(caption="Exportar relatório Excel", directory="", filter="Planilha (*.xls)")[0]
            except FileNotFoundError:
                return
            try:
                if arquivo == "":
                     return
                if self.view.checkBox.isChecked() is True:
                    dados = self.view.dados_total
                else:
                    dados = self._db.select_todos
                    dados = dados[dados.id.isin(self.relatorio)]
                Relatorio_xls(arquivo, dados)
                Erro("Relatório gerado com sucesso.", QMessageBox.Information)
            except ValueError:
                return
        else:
            Erro("Nenhum decreto selecionado.", QMessageBox.Information)

    def inserir_dados(self):
        self.definir_dados(self._db.select_todos)
        self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
        self.atualizar_contadores()

    def inserir_metas(self):
        self.definir_dados(self._db.select_metas)
        self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
        self.atualizar_contadores()

    def verificar_tela(self):
        self.reset_css_button()
        if self.filtro_atual == 'INSERIDO SISTEMA':
            self.view.btn_inserido.setStyleSheet("QPushButton {font-size: 18px;border-bottom: 2px solid rgb(109, 49, 162)}")
        elif self.filtro_atual == 'ANÁLISE':
            self.view.btn_analise.setStyleSheet("QPushButton {font-size: 18px;border-bottom: 2px solid rgb(109, 49, 162)}")
        elif self.filtro_atual == 'METAS INSERIDAS':
            self.view.btn_metas.setStyleSheet("QPushButton {font-size: 18px;border-bottom: 2px solid rgb(109, 49, 162)}")
        elif self.filtro_atual == 'EMAIL ENVIADO':
            self.view.btn_email.setStyleSheet("QPushButton {font-size: 18px;border-bottom: 2px solid rgb(109, 49, 162)}")
        elif self.filtro_atual == 'TODOS':
            self.view.btn_todos.setStyleSheet("QPushButton {font-size: 18px;border-bottom: 2px solid rgb(109, 49, 162)}")
        self.view.lb_filtro.setText(f"Filtro: {self.filtro_atual.title()}")

    def reset_css_button(self):
        self.view.btn_inserido.setStyleSheet("QPushButton {	background-color: white;	border: none;	border-bottom: 1px solid rgb(109, 49, 162)} QPushButton:hover {	background-color: white;	border: none;	font-size: 18px;	border-bottom: 2px solid rgb(109, 49, 162)}")
        self.view.btn_analise.setStyleSheet("QPushButton {	background-color: white;	border: none;	border-bottom: 1px solid rgb(109, 49, 162)} QPushButton:hover {	background-color: white;	border: none;	font-size: 18px;	border-bottom: 2px solid rgb(109, 49, 162)}")
        self.view.btn_metas.setStyleSheet("QPushButton {	background-color: white;	border: none;	border-bottom: 1px solid rgb(109, 49, 162)} QPushButton:hover {	background-color: white;	border: none;	font-size: 18px;	border-bottom: 2px solid rgb(109, 49, 162)}")
        self.view.btn_email.setStyleSheet("QPushButton {	background-color: white;	border: none;	border-bottom: 1px solid rgb(109, 49, 162)} QPushButton:hover {	background-color: white;	border: none;	font-size: 18px;	border-bottom: 2px solid rgb(109, 49, 162)}")
        self.view.btn_todos.setStyleSheet("QPushButton {	background-color: white;	border: none;	border-bottom: 1px solid rgb(109, 49, 162)} QPushButton:hover {	background-color: white;	border: none;	font-size: 18px;	border-bottom: 2px solid rgb(109, 49, 162)}")


    def filtro_new(self, filtro):
        self.atualizar_contadores()
        if filtro == 'INSERIDO SISTEMA':
            self.modificar_dados(
                self._db.select_todos.sort_values(by=['DATA_ALTERACAO_ORCAMENTARIA'], ascending=True),
                self._db.select_inserido)
            self.filtro_atual = 'INSERIDO SISTEMA'
        elif filtro == 'ANÁLISE':
            self.modificar_dados(
                self._db.select_todos.sort_values(by=['DATA_ALTERACAO_ORCAMENTARIA'], ascending=True),
                self._db.select_analise)
            self.filtro_atual = 'ANÁLISE'
        elif filtro == 'METAS INSERIDAS':
            self.modificar_dados(
                self._db.select_todos.sort_values(by=['DATA_ALTERACAO_ORCAMENTARIA'], ascending=False), self._db.select_metas)
            self.filtro_atual = 'METAS INSERIDAS'
        elif filtro == 'EMAIL ENVIADO':
            self.modificar_dados(
                self._db.select_todos.sort_values(by=['DATA_ALTERACAO_ORCAMENTARIA'], ascending=True), self._db.select_email)
            self.filtro_atual = 'EMAIL ENVIADO'
        elif filtro == 'TODOS':
            self.modificar_dados(
                self._db.select_todos.sort_values(by=['DATA_ALTERACAO_ORCAMENTARIA']), self._db.select_todos)
            self.filtro_atual = 'TODOS'
        self.verificar_tela()
        return


    def filtrar(self, filtro):
        self.atualizar_contadores()
        if filtro == 'INSERIDO SISTEMA':
            self.definir_dados(self._db.select_inserido)
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
            self.filtro_atual = 'INSERIDO SISTEMA'
        elif filtro == 'ANÁLISE':
            self.definir_dados(self._db.select_analise)
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
            self.filtro_atual = 'ANÁLISE'
        elif filtro == 'METAS INSERIDAS':
            self.definir_dados(self._db.select_metas)
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
            self.filtro_atual = 'METAS INSERIDAS'
        elif filtro == 'EMAIL ENVIADO':
            self.definir_dados(self._db.select_email)
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
            self.filtro_atual = 'EMAIL ENVIADO'
        elif filtro == 'TODOS':
            self.definir_dados(self._db.select_todos)
            self.filtro_atual = 'TODOS'
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
        self.verificar_tela()
        return

    def definir_dados(self, dados):
        pag = self.view.paginacao(dados)
        pag = round(pag)

        self.view.dados_total = dados
        self.view.dados_pag = []

        inicio = 0

        for i in range(pag):
            fim = inicio + int(self.view.comboBox.currentText())
            self.view.dados_pag.append(dados.iloc[inicio:fim])
            inicio+=int(self.view.comboBox.currentText())

    def filtro_busca(self, dados):

        #self._items = self.view.preencher_scroll(self.view.dados_total, 1)
        #self.filtro_atual = 'INSERIDO SISTEMA'
        #self._items = self.view.preencher_scroll(dados)
        if self.filtro_atual == 'EMAIL ENVIADO':
            self._items = self.view.preencher_scroll(
                dados.sort_values(by=['DATA_ALTERACAO_ORCAMENTARIA'], ascending=True), 1, False)

        else:
            self._items = self.view.preencher_scroll(
                dados.sort_values(by=['DATA_ALTERACAO_ORCAMENTARIA'], ascending=True), 1, False)
        self.verificar_tela()

    def ocultar_items(self):
        for i in self._items.index:
            obj = self._items['OBJETO'][i]
            obj.setHidden(True)

    def busca(self, value=None):
        campo = self.view.input_busca.text()
        filt = campo
        self.reset_css_button()

        if campo == '':
            self.filtrar('TODOS')
            return

        campo = self.verificar_campo_data(campo)

        #self.filtro_busca()

        self.definir_dados(self._db.select_busca(campo, self.filtro_atual))
        self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
        
        self.view.lb_filtro.setText(f"Filtro: {filt}            Decretos Encontratos: {len(self.view.dados_total)}")

    def verificar_campo_data(self, campo):
        data = campo
        try:
            if len(campo) == 4 and int(campo) <= datetime.now().year:
                datetime(int(campo), 1, 1)
            elif  len(campo) == 7:
                datetime(int(campo[3:]), int(campo[:2]), 1)
            elif len(campo) == 10:
                datetime(int(campo[6:]), int(campo[3:5]), int(campo[:2]))
            else:
                return [campo]
        except:
            return [campo]

        try:
            if len(data) == 4:
                dataIni = f"{data}-01-01"
                dataFim = f"{data}-12-31"
            elif len(data) == 7:
                dataIni = f"{data[3:]}-{data[:2]}-01"
                dataFim = f"{data[3:]}-{data[:2]}-31"
            elif len(data) == 10:
                dataT = f"{data[6:]}-{data[3:5]}-{data[:2]}"
                dataIni = datetime(int(dataT[:4]), int(dataT[5:7]), int(dataT[8:]))
                dataFim = datetime(int(dataT[:4]), int(dataT[5:7]), int(dataT[8:]))
                return [dataIni.strftime("%Y-%m-%d"), dataFim.strftime("%Y-%m-%d")]
            else:
                return [campo]
            dataIni = datetime(int(dataIni[:4]), int(dataIni[5:7]), int(dataIni[8:]))
            dataFim = datetime(int(dataFim[:4]), int(dataFim[5:7]), calendar.monthrange(dataIni.year, dataIni.month)[1])
            
            return [dataIni.strftime("%Y-%m-%d"), dataFim.strftime("%Y-%m-%d")]
        except ValueError as a:
            print(a)
            return [campo]

    def marcar_todos(self):
        if self.view.checkBox.isChecked():
            status = True
        else:
            status = False
        for obj in self.view._items:
                obj.check_relatorio.setChecked(status)
                obj.marcar()

    def modificar_dados(self, dados, values, status='FILTRO'):
        v = values['id']
        for i, j in zip(self._items['OBJETO'].values, dados['id'].values):
            obj = i
            obje = dados[dados['id']==j]
            obj.atualizar_dados(obje.loc[obje.index[0]])
            item = obje.loc[obje.index[0]]
            if item['id'] in v.values:
                obj.setHidden(False)
        self.marcar_todos()
        self.relatorio = []
        self.view.scrollArea.verticalScrollBar().setSliderPosition(0)
        return

    def atualizar_contadores(self):
        self.view.preencher_lb_todos(len(self._db.select_todos))
        self.view.preencher_lb_analise(len(self._db.select_analise))
        self.view.preencher_lb_email(len(self._db.select_email))
        self.view.preencher_lb_metas(len(self._db.select_metas))
        self.view.preencher_lb_inserido(len(self._db.select_inserido))