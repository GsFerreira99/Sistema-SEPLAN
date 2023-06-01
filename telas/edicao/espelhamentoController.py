from telas.edicao.espelhamentoView import EspelhamentoView
from telas.edicao.selectEspelhamentoView import SelectEspelhamentoView
from datetime import datetime
from calendar import calendar
from PyQt5.QtCore import QDate
from funcoes.genericos import filtro_dinheiro

from PyQt5.QtWidgets import QMessageBox
from funcoes.poupUp import Erro


import pandas as pd


class EspelhamentoController:

    def __init__(self, ui, db) -> None:
        """ Responsável por controlar tudo que acontece na tela de Edição """
        self.ui = ui
        self.view = EspelhamentoView(self.ui)
        self.viewSelect = SelectEspelhamentoView(self.ui)
        self._items = {
            "TODOS": [],
            "ANÁLISE": [],
            "EMAIL ENVIADO": [],
            "METAS INSERIDAS": [],
            "INSERIDO SISTEMA": []
        }

        self.db = db

        self.ativo = False
        self.dados_salvos = {}
        self.dados_escolhidos = {}

        self.view.checkBox.clicked.connect(lambda: self.select_todos())

        self.view.btn_busca.clicked.connect(lambda: self.busca())
        self.view.btn_salvar_espelhado.clicked.connect(lambda: self.salvar())

        self.view.btn_todos.clicked.connect(lambda: self.inserir_dados_scroll('TODOS'))
        self.view.btn_email.clicked.connect(lambda: self.inserir_dados_scroll('EMAIL ENVIADO'))
        self.view.btn_inserido.clicked.connect(lambda: self.inserir_dados_scroll('INSERIDO SISTEMA'))
        self.view.btn_metas.clicked.connect(lambda: self.inserir_dados_scroll('METAS INSERIDAS'))
        self.view.btn_analise.clicked.connect(lambda: self.inserir_dados_scroll('ANÁLISE'))

        self.viewSelect.btn_proximo.clicked.connect(lambda: self.proximo())

        self.inserir_dados_scroll('TODOS')

    def inserir_dados_scroll(self, filtro):
        if filtro == 'INSERIDO SISTEMA':
            self.definir_dados_scroll(self.db.select_inserido)
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
            self.filtro_atual = 'INSERIDO SISTEMA'
        if filtro == 'ANÁLISE':
            self.definir_dados_scroll(self.db.select_analise)
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
            self.filtro_atual = 'ANÁLISE'
        if filtro == 'METAS INSERIDAS':
            self.definir_dados_scroll(self.db.select_metas)
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
            self.filtro_atual = 'METAS INSERIDAS'
        if filtro == 'EMAIL ENVIADO':
            self.definir_dados_scroll(self.db.select_email)
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
            self.filtro_atual = 'EMAIL ENVIADO'
        if filtro == 'TODOS':
            self.definir_dados_scroll(self.db.select_todos)
            self._items = self.view.preencher_scroll(self.view.dados_pag, 1)
            self.filtro_atual = 'TODOS'
        self.contagem_decretos()
        self.view.verificar_tela(self.filtro_atual)

    def contagem_decretos(self):
        self.view.lb_totalDecretos.setText(
            f"Decretos Encontratos: {len(self.view.dados_total)}")

    def definir_dados_scroll(self, dados):
        pag = self.view.paginacao(dados)
        pag = round(pag)

        self.view.dados_total = dados
        self.view.dados_pag = []

        inicio = 0

        for i in range(pag):
            fim = inicio + 10
            self.view.dados_pag.append(dados.iloc[inicio:fim])
            inicio += 10


    def definir_dados(self, dados):
        self.dados_salvos = dados
        self.preencher_campos_select(dados)

    def preencher_campos_select(self, dados):
        self.viewSelect.input_metaOrigemAtual.setText(dados['metaOrigem'][0])
        self.viewSelect.input_metaOrigemAtual_2.setText(dados['metaOrigem'][1])

        self.viewSelect.inputDate_emailInicial.setDate(self.montar_data(dados['dataEmail'][0]))
        self.viewSelect.input_origem_contato1_2.setText(dados['dataEmail'][1])

        self.viewSelect.input_metaAnulado.setText(dados['metaNova'][0])
        self.viewSelect.input_metaSuplementado.setText(dados['metaNova'][1])


        #DATAS EMAIL
        if dados['emailOrigem'][1] != '':
            self.viewSelect.inputDate_origem1.setDate(self.montar_data(dados['emailOrigem'][0]))
        self.viewSelect.input_origem_contato1.setText(str(dados['emailOrigem'][1]))
        self.viewSelect.input_origem_status1.setText(str(dados['emailOrigem'][2]))

        if dados['emailOrigem'][4] != '':
            self.viewSelect.inputDate_origem2.setDate(self.montar_data(dados['emailOrigem'][3]))
        self.viewSelect.input_origem_contato2.setText(str(dados['emailOrigem'][4]))
        self.viewSelect.input_origem_status2.setText(str(dados['emailOrigem'][5]))

        if dados['emailOrigem'][7] != '':
            self.viewSelect.inputDate_origem3.setDate(self.montar_data(dados['emailOrigem'][6]))
        self.viewSelect.input_origem_contato3.setText(str(dados['emailOrigem'][7]))
        self.viewSelect.input_origem_status3.setText(str(dados['emailOrigem'][8]))

        if dados['emailDestino'][1] != '':
            self.viewSelect.inputDate_destino1.setDate(self.montar_data(dados['emailDestino'][0]))
        self.viewSelect.input_destino_contato1.setText(str(dados['emailDestino'][1]))
        self.viewSelect.input_destino_status1.setText(str(dados['emailDestino'][2]))

        if dados['emailDestino'][4] != '':
            self.viewSelect.inputDate_destino2.setDate(self.montar_data(dados['emailDestino'][3]))
        self.viewSelect.input_destino_contato2.setText(str(dados['emailDestino'][4]))
        self.viewSelect.input_destino_status2.setText(str(dados['emailDestino'][5]))

        if dados['emailDestino'][7] != '':
            self.viewSelect.inputDate_destino3.setDate(self.montar_data(dados['emailDestino'][6]))
        self.viewSelect.input_destino_contato3.setText(str(dados['emailDestino'][7]))
        self.viewSelect.input_destino_status3.setText(str(dados['emailDestino'][8]))

        self.viewSelect.input_metaAnulado.setText(str(dados['metaNova'][0]))
        self.viewSelect.input_metaSuplementado.setText(str(dados['metaNova'][1]))

        self.limpar_checkBox()

        if dados['status'][0] == 'ok':
            self.viewSelect.inputCheck_emailEnviado.setChecked(True)
        if dados['status'][1] == 'ok':
            self.viewSelect.inputCheck_inseridoMetas.setChecked(True)
        if dados['status'][2] == 'ok':
            self.viewSelect.inputCheck_atualizadoSistema.setChecked(True)


    def limpar_select(self):
        self.viewSelect.lb_decreto_info.setText("")
        self.viewSelect.lb_dataDecreto_info.setText("")
        self.viewSelect.input_origem_contato1_2.setText("")
        self.viewSelect.lb_origem_orgao_info.setText("")
        self.viewSelect.lb_origem_programa_info.setText("")
        self.viewSelect.lb_origem_acao_info.setText("")
        self.viewSelect.lb_origem_acao_info_13.setText("")
        self.viewSelect.lb_destino_orgao_info.setText("")
        self.viewSelect.lb_destino_acao_info.setText("")
        self.viewSelect.lb_destino_programa_info.setText("")
        self.viewSelect.lb_origem_acao_info_15.setText("")
        self.viewSelect.lb_valor_info.setText("")
        self.viewSelect.input_metaOrigemAtual.setText("")
        self.viewSelect.lb_origem_acao_info_3.setText("")
        self.viewSelect.input_metaOrigemAtual_2.setText("")
        self.viewSelect.lb_origem_acao_info_11.setText("")

        self.viewSelect.input_origem_contato1_2.setText('')

        self.viewSelect.input_origem_contato1.setText('')
        self.viewSelect.input_origem_contato2.setText('')
        self.viewSelect.input_origem_contato3.setText('')
        self.viewSelect.input_origem_status1.setText('')
        self.viewSelect.input_origem_status2.setText('')
        self.viewSelect.input_origem_status3.setText('')

        self.viewSelect.input_destino_contato1.setText('')
        self.viewSelect.input_destino_contato2.setText('')
        self.viewSelect.input_destino_contato3.setText('')
        self.viewSelect.input_destino_status1.setText('')
        self.viewSelect.input_destino_status2.setText('')
        self.viewSelect.input_destino_status3.setText('')

        self.viewSelect.input_metaAnulado.setText('')
        self.viewSelect.input_metaSuplementado.setText('')

        dateNow = datetime.now()
        data = QDate(dateNow.year, dateNow.month, dateNow.day)

        self.viewSelect.inputDate_emailInicial.setDate(data)

        self.viewSelect.inputDate_origem1.setDate(data)
        self.viewSelect.inputDate_origem2.setDate(data)
        self.viewSelect.inputDate_origem3.setDate(data)

        self.viewSelect.inputDate_destino1.setDate(data)
        self.viewSelect.inputDate_destino2.setDate(data)
        self.viewSelect.inputDate_destino3.setDate(data)

    def busca(self, value=None):
        campo = self.view.input_busca.text()
        filt = campo

        if campo == '':
            self.filtrar('TODOS')
            return

        campo = self.verificar_campo_data(campo)

        # self.filtro_busca()

        self.definir_dados_scroll(self.db.select_busca(campo, self.filtro_atual))
        self._items = self.view.preencher_scroll(self.view.dados_pag, 1)

        self.view.lb_totalDecretos.setText(f"Filtro: {filt}            Decretos Encontratos: {len(self.view.dados_total)}")

    def verificar_campo_data(self, campo):
        data = campo
        try:
            if len(campo) == 4 and int(campo) <= datetime.now().year:
                datetime(int(campo), 1, 1)
            elif len(campo) == 7:
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

    def campo_total(self):
        text = 'Decretos encontrados: '
        if self.view.tabWidget.currentIndex() == 0:
            self.view.lb_totalDecretos.setText(text+str(len(self._items['ANÁLISE'][1])))
        elif self.view.tabWidget.currentIndex() == 1:
            self.view.lb_totalDecretos.setText(text+str(len(self._items['EMAIL ENVIADO'][1])))
        elif self.view.tabWidget.currentIndex() == 2:
            self.view.lb_totalDecretos.setText(text+str(len(self._items['METAS INSERIDAS'][1])))
        elif self.view.tabWidget.currentIndex() == 3:
            self.view.lb_totalDecretos.setText(text+str(len(self._items['INSERIDO SISTEMA'][1])))

    def inserir_dadosgf(self):
        self.view.limpar(self._items)
        for filtro, item in self._items.items():
            dec = self.db.select_busca([self.ui.dados['N_DECRETO']], filtro)
            if not dec.empty:
                fil = dec['id'] != self.ui.dados['id']
                dec = dec[fil]
            i = self.view.preencher_scroll(
                dec,
                item[0]
            )

            if i != None:
                self._items[filtro][1] = i
                self.ativo = True
            else:
                self._items[filtro][1] = []

        self.view.tabWidget.setCurrentIndex(0)
        self.campo_total()

    def select_todos(self):
        if self.view.checkBox.isChecked():
            status = True
        else:
            status = False

        for obj in self._items:
            try:
                    obj.check_relatorio.setChecked(status)
            except IndexError:
                pass
            except TypeError:
                pass
            except RuntimeError:
                pass

    def show(self):
        self.viewSelect.show()

    def proximo(self):
        self.dados_escolhidos = {
            "todos": self.viewSelect.radio_todos.isChecked(),
            "metaAtual": self.viewSelect.radio_metaAtual.isChecked(),
            "metaNova": self.viewSelect.radio_metaNova.isChecked(),
            "dataEmail": self.viewSelect.radio_dataEmail.isChecked(),
            "contatosDestino": self.viewSelect.radio_contatosDestino.isChecked(),
            "contatosOrigem": self.viewSelect.radio_contatosOrigem.isChecked(),
            "status": self.viewSelect.radio_status.isChecked(),
        }

        for i in self.dados_escolhidos.values():
            if i is True:
                self.view.show()
                self.viewSelect.close()
                return


        Erro("Selecione 1 dos campos para serem espelhados!", QMessageBox.Information)

    def lista_dados(self):
        dados = {}

        if self.dados_escolhidos['todos'] is True:
            return self.dados_salvos
        else:
            if self.dados_escolhidos['metaAtual'] is True:
                dados['metaOrigem'] = self.dados_salvos['metaOrigem']
            if self.dados_escolhidos['metaNova'] is True:
                dados['metaNova'] = self.dados_salvos['metaNova']
            if self.dados_escolhidos['dataEmail'] is True:
                dados['dataEmail'] = self.dados_salvos['dataEmail']
            if self.dados_escolhidos['contatosDestino'] is True:
                dados['emailDestino'] = self.dados_salvos['emailDestino']
            if self.dados_escolhidos['contatosOrigem'] is True:
                dados['emailOrigem'] = self.dados_salvos['emailOrigem']
            if self.dados_escolhidos['status'] is True:
                dados['status'] = self.dados_salvos['status']
            dados['id'] = self.dados_salvos['id']
            return dados

    def salvar(self):

        dados = self.lista_dados()

        self.ui.edicaoController.salvar_dados()
        for item in self._items:
            if item.check_relatorio.isChecked():
                dados['id'] = [int(item.get_id())]
                self.ui.principalController._db.atualizar_decreto_espelhado(dados)


        Erro("Dados salvos com sucesso.", QMessageBox.Information)
        self.view.close()

    def show_select_espelhamento(self):
        pass

    def limpar_checkBox(self):
        self.viewSelect.inputCheck_emailEnviado.setChecked(False)
        self.viewSelect.inputCheck_inseridoMetas.setChecked(False)
        self.viewSelect.inputCheck_atualizadoSistema.setChecked(False)

    def montar_data(self, data):
        try:
            date = QDate(int(data[6:]), int(data[3:5]), int(data[:2]))
            return date
        except:
            if data == 0:
                return QDate(1, 1, 2000)
            elif type(data) == str:
                return QDate(1, 1, 2000)
            elif pd.isnull(data) == True:
                return QDate(1, 1, 2000)
            try:
                date = QDate(data.year, data.month, data.day)
                return date
            except:
                date = QDate(int(data[6:]), int(data[3:5]), int(data[:2]))
                return date