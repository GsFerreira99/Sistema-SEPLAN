from telas.edicao.edicaoView import EdicaoView
from telas.edicao.emailView import EmailView

from telas.edicao.espelhamentoController import EspelhamentoController

from PyQt5.QtWidgets import QMessageBox
from funcoes.poupUp import Erro


import pandas as pd


class EdicaoController:

    def __init__(self, ui) -> None:
        """ Responsável por controlar tudo que acontece na tela de Edição """
        self.ui = ui
        self.view = EdicaoView(self.ui)
        self.emailView = EmailView(self.ui)

        self.view.btn_email.clicked.connect(lambda: self.exibirEmail())

        self.view.btn_salvar.clicked.connect(lambda: self.salvar())

        self.view.btn_voltar.clicked.connect(lambda: self.voltar())
        self.view.input_metaOrigemAtual_2.editingFinished.connect(lambda: self.ativar_email())
        self.view.input_metaOrigemAtual.editingFinished.connect(lambda: self.ativar_email())

        self.view.btn_salvar_espelhado.clicked.connect(lambda: self.exibir_espelhamento())
     
    def inserir_dados(self):
        self.view.preencher_campos(self.ui.dados)
        self.ativar_email()
        self.espelhamentoController = EspelhamentoController(self.ui, self.ui.db)

    def exibir_espelhamento(self):
        self.espelhamentoController.show()
        self.espelhamentoController.definir_dados(self.dados_salvos())

    def dados_salvos(self):
        d = {
            "metaOrigemAtual": [],
            "metaDestinoAtual": [],
            "metaOrigemSuplementado": [],
            "metaDestinoSuplementado": [],
            "dataEmail": [],
            "emailDestino": [],
            "emailOrigem": [],
            "status": [],
            "id": [],
            "permaneceMetaOrigem": [],
            "permaneceMetaDestino": [],
            "geraEmailOrigem": [],
            "geraEmailDestino": [],
        }

        d['metaOrigemAtual'].append(self.view.input_metaOrigemAtual.text())
        d['metaDestinoAtual'].append(self.view.input_metaOrigemAtual_2.text())

        d['dataEmail'].append(
            pd.to_datetime(self.view.inputDate_emailInicial.date().toString('yyyy/MM/dd'), dayfirst=True))
        d['dataEmail'].append(self.view.input_origem_contato1_2.text())

        if self.view.input_origem_contato1.text() != '':
            d['emailOrigem'].append(self.view.input_origem_contato1_2.text())
        else:
            d['emailOrigem'].append(None)

        d['emailOrigem'].append(self.view.input_origem_contato1.text())
        d['emailOrigem'].append(self.view.input_origem_status1.text())

        if self.view.input_origem_contato2.text() != '':
            d['emailOrigem'].append(pd.to_datetime(self.view.inputDate_origem2.date().toString('yyyy/MM/dd'),
                                                   dayfirst=True))
        else:
            d['emailOrigem'].append(None)
        d['emailOrigem'].append(self.view.input_origem_contato2.text())
        d['emailOrigem'].append(self.view.input_origem_status2.text())

        if self.view.input_origem_contato3.text() != '':
            d['emailOrigem'].append(pd.to_datetime(self.view.inputDate_origem3.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            d['emailOrigem'].append(None)
        d['emailOrigem'].append(self.view.input_origem_contato3.text())
        d['emailOrigem'].append(self.view.input_origem_status3.text())

        # DESTINO
        if self.view.input_destino_contato1.text() != '':
            d['emailDestino'].append(pd.to_datetime(self.view.inputDate_destino1.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            d['emailDestino'].append(None)
        d['emailDestino'].append(self.view.input_destino_contato1.text())
        d['emailDestino'].append(self.view.input_destino_status1.text())

        if self.view.input_destino_contato2.text() != '':
            d['emailDestino'].append(pd.to_datetime(self.view.inputDate_destino2.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            d['emailDestino'].append(None)
        d['emailDestino'].append(self.view.input_destino_contato2.text())
        d['emailDestino'].append(self.view.input_destino_status2.text())

        if self.view.input_destino_contato3.text() != '':
            d['emailDestino'].append(pd.to_datetime(self.view.inputDate_destino3.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            d['emailDestino'].append(None)
        d['emailDestino'].append(self.view.input_destino_contato3.text())
        d['emailDestino'].append(self.view.input_destino_status3.text())

        #META
        d['metaOrigemSuplementado'].append(self.view.input_metaAnulado.text())
        d['metaDestinoSuplementado'].append(self.view.input_metaSuplementado.text())

        #STATUS
        if self.view.inputCheck_emailEnviado.isChecked():
            d['status'].append('ok')
        else:
            d['status'].append('')
        if self.view.inputCheck_inseridoMetas.isChecked():
            d['status'].append('ok')
        else:
            d['status'].append('')
        if self.view.inputCheck_atualizadoSistema.isChecked():
            d['status'].append('ok')
        else:
            d['status'].append('')

        d['permaneceMetaOrigem'] = self.view.inputCheck_permaneceMetaOrigem.isChecked()
        d['permaneceMetaDestino'] = self.view.inputCheck_permaneceMetaDestino.isChecked()
        d['geraEmailOrigem'] = self.view.inputCheck_geraEmailOrigem.isChecked()
        d['geraEmailDestino'] = self.view.inputCheck_geraEmailDestino.isChecked()

        d['id'].append(int(self.ui.dados['id']))

        return d

    def exibirEmail(self):
        self.definir_email()
        self.emailView.show()

    def ativar_email(self):
        if (str(self.ui.dados['VALOR_FISICO_ATUAL_SUPLEMENTADO']) != 'nan' and str(self.ui.dados['VALOR_FISICO_ATUAL_ANULADO']) != 'nan' and str(self.ui.dados['EMAIL_INICIAL']) != 'nan' and str(self.ui.dados['DATA_EMAIL_INICIAL']) != 'nan') or (self.view.input_metaOrigemAtual.text() != '0' and self.view.input_metaOrigemAtual_2.text() != '0'):
            self.view.btn_email.setEnabled(True)
        else:
            self.view.btn_email.setEnabled(False)

    def definir_email(self):

        self.emailView.lineEdit.setText('')
        self.emailView.textEdit_2.setText('')

        if str(self.ui.dados['EMAIL_INICIAL']) != 'nan':
            self.emailView.lineEdit.setText(str(self.ui.dados['EMAIL_INICIAL']))
        
        self.emailView.textEdit_2.setText(
            f"""
Prezado(a) Senhor(a),

Em paralelo ao monitoramento do PPA 2022-2025, cuja rotina de alimentação no SIOP se dará a cada quadrimestre, cobraremos a atualização das metas  projetadas anuais das ações dos programas, a partir das solicitações de remanejamento orçamentário das Secretarias /Órgãos municipais.

Para tanto, solicitamos informar qual a nova meta física de origem e/ou nova meta física de destino, com referência ao seguinte remanejamento.


Obs.1 - Esclarecemos ainda, que as atualizações  no SIOP serão feitas exclusivamente pela SEPLAN. 

Órgão de Origem: {self.ui.dados['NOME_ORGAO_ANULADO']} Decreto:{self.ui.dados['N_DECRETO']} Data: {self.ui.dados['DATA_ALTERACAO_ORCAMENTARIA']}
Programa de Origem: {self.ui.dados['ID_PROGRAMA_ANULADO']} - {self.ui.dados['PROGRAMA_ANULADO']}
Ação de Origem: {self.ui.dados['ID_ACAO_ANULADO']} -  {self.ui.dados['ACAO_ANULADO']}
Meta FÍSICA de Origem  ATUAL: {self.ui.dados['VALOR_FISICO_ATUAL_ANULADO']}
Produto Origem: {self.ui.dados['NOME_PRODUTO_ANULADO']}
Valor remanejado: {self.ui.dados['VALOR_FINANCEIRO']}

Órgão DESTINO: {self.ui.dados['NOME_ORGAO_SUPLEMENTADO2']} Decreto:{self.ui.dados['N_DECRETO']} Data: {self.ui.dados['DATA_ALTERACAO_ORCAMENTARIA']}
Programa de Destino: {self.ui.dados['ID_PROGRAMA_SUPLEMENTADO']} - {self.ui.dados['PROGRAMA_SUPLEMENTADO']}
Ação de Destino: {self.ui.dados['ID_ACAO_SUPLEMENTADO']} - {self.ui.dados['ACAO_SUPLEMENTADO']}
Meta FÍSICA de destino ATUAL: {self.ui.dados['VALOR_FISICO_ATUAL_SUPLEMENTADO']}
Produto destino: {self.ui.dados['NOME_PRODUTO_SUPLEMENTADO']}
INFORMAR:

NOVA Meta FÍSICA de Origem:
NOVA Meta FÌSICA de Destino:
             """
        )

    def salvar_dados(self):
        
        dados = []

        dados.append(self.view.input_metaOrigemAtual.text())
        dados.append(self.view.input_metaOrigemAtual_2.text())


        dados.append(pd.to_datetime(self.view.inputDate_emailInicial.date().toString('yyyy/MM/dd'), dayfirst=True))

        dados.append(self.view.input_origem_contato1_2.text())

        if self.view.input_origem_contato1.text() != '':
            dados.append(pd.to_datetime(self.view.inputDate_origem1.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            dados.append(None)
        dados.append(self.view.input_origem_contato1.text())
        dados.append(self.view.input_origem_status1.text())

        if self.view.input_origem_contato2.text() != '':
            dados.append(pd.to_datetime(self.view.inputDate_origem2.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            dados.append(None)
        dados.append(self.view.input_origem_contato2.text())
        dados.append(self.view.input_origem_status2.text())

        if self.view.input_origem_contato3.text() != '':
            dados.append(pd.to_datetime(self.view.inputDate_origem3.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            dados.append(None)
        dados.append(self.view.input_origem_contato3.text())
        dados.append(self.view.input_origem_status3.text())
        
        #DESTINO
        if self.view.input_destino_contato1.text() != '':
            dados.append(pd.to_datetime(self.view.inputDate_destino1.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            dados.append(None)
        dados.append(self.view.input_destino_contato1.text())
        dados.append(self.view.input_destino_status1.text())
        
        if self.view.input_destino_contato2.text() != '':
            dados.append(pd.to_datetime(self.view.inputDate_destino2.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            dados.append(None)
        dados.append(self.view.input_destino_contato2.text())
        dados.append(self.view.input_destino_status2.text())
        
        if self.view.input_destino_contato3.text() != '':
            dados.append(pd.to_datetime(self.view.inputDate_destino3.date().toString('yyyy/MM/dd'), dayfirst=True))
        else:
            dados.append(None)
        dados.append(self.view.input_destino_contato3.text())
        dados.append(self.view.input_destino_status3.text())
        
        dados.append(self.view.input_metaAnulado.text())
        dados.append(self.view.input_metaSuplementado.text())

        if self.view.inputCheck_emailEnviado.isChecked():
            dados.append('ok')
        else:
            dados.append('')
        if self.view.inputCheck_inseridoMetas.isChecked():
            dados.append('ok')
        else:
            dados.append('')
        if self.view.inputCheck_atualizadoSistema.isChecked():
            dados.append('ok')
        else:
            dados.append('')

        dados.append(self.view.inputCheck_geraEmailOrigem.isChecked())
        dados.append(self.view.inputCheck_geraEmailDestino.isChecked())

        dados.append(self.view.inputCheck_permaneceMetaOrigem.isChecked())
        dados.append(self.view.inputCheck_permaneceMetaDestino.isChecked())

        dados.append(int(self.ui.dados['id']))



        self.ui.principalController._db.atualizar_decreto(dados)
        self.ui.dados = self.ui.principalController._db.select_decreto(int(self.ui.dados['id']))
        self.inserir_dados()

    def salvar(self):
        self.salvar_dados()
        Erro("Dados salvos com sucesso.", QMessageBox.Information)

    def voltar(self):
        self.ui.view.stackedWidget.setCurrentIndex(0)
        self.ui.principalController.atualizar_contadores()
