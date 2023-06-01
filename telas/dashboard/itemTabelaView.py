from media.ui_item import Ui_Form
from PyQt5.QtWidgets import QWidget
from datetime import datetime
from PyQt5.QtCore import QDate


class ItemTabelaView(Ui_Form, QWidget):

    def __init__(self, ui, dados, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.ui = ui
        self._dados = dados


        self.preencher_campos()
        self.alerta_meta()
        self.btn_detalhes.clicked.connect(lambda: self.exibirDetalhes())

        self.check_relatorio.clicked.connect(lambda: self.marcar())
        
        if self._dados['EMAIL_ENVIADO'] == 'ok' and self._dados['INSERIDO_METAS'] != 'ok' and self._dados['ATUALIZADO_NO_SISTEMA'] != 'ok':
            self.envio_email()


    def alerta_meta(self):
        if (str(self._dados['NOVA_META_FISICA_ANULADO']) == '' and str(self._dados['NOVA_META_FISICA_SUPLEMENTADO']) != '') or (str(self._dados['NOVA_META_FISICA_ANULADO']) != '' and str(self._dados['NOVA_META_FISICA_SUPLEMENTADO']) == '') and (str(self._dados['INSERIDO_METAS']) != 'ok' and str(self._dados['INSERIDO_METAS']) != 'ATUALIZADO_NO_SISTEMA'):
            self.lb_status.setMaximumWidth(50)
        else:
            self.lb_status.setMaximumWidth(0)

    def atualizar_dados(self, dados):
        self._dados = dados
        self.preencher_campos()
        self.alerta_meta()
        if self._dados['EMAIL_ENVIADO'] == 'ok' and self._dados['INSERIDO_METAS'] != 'ok' and self._dados['ATUALIZADO_NO_SISTEMA'] != 'ok':
            self.envio_email()
        else:
            self.frame_4.setStyleSheet("""QFrame{ border: 1px solid rgb(238, 238, 238)	;border-left: 3px solid rgb(109, 49, 162);}""")

    def preencher_campos(self):
        self.limpar_campos()
        self.lb_decreto.setText(str(self._dados['N_DECRETO']))
        if self._dados['DATA_ALTERACAO_ORCAMENTARIA'] != None and self._dados['DATA_ALTERACAO_ORCAMENTARIA'] != '':
            self.lb_data.setText(str(self._dados['DATA_ALTERACAO_ORCAMENTARIA'].strftime('%d/%m/%Y')))

        self.lb_orgao_destino.setText(f"{self._dados['NOME_ORGAO_SUPLEMENTADO']} - {self._dados['NOME_ORGAO_SUPLEMENTADO2']}")
        self.lb_programa_destino.setText(f"{self._dados['ID_PROGRAMA_SUPLEMENTADO']} - {self._dados['PROGRAMA_SUPLEMENTADO']}")
        self.lb_acao_acao.setText(f"{self._dados['ID_ACAO_SUPLEMENTADO']} - {self._dados['ACAO_SUPLEMENTADO']}")
        
        self.lb_orgao_origem.setText(f"{self._dados['ORGAO_ANULADO']} - {self._dados['NOME_ORGAO_ANULADO']}")
        self.lb_programa_origem.setText(f"{self._dados['ID_PROGRAMA_ANULADO']} - {self._dados['PROGRAMA_ANULADO']}")
        self.lb_acao_origem_2.setText(f"{self._dados['ID_ACAO_ANULADO']} - {self._dados['ACAO_ANULADO']}")

    def limpar_campos(self):
        self.lb_decreto.setText(" ")
        self.lb_data.setText("")
        self.lb_orgao_destino.setText("")
        self.lb_programa_destino.setText("")
        self.lb_acao_acao.setText("")
        
        self.lb_orgao_origem.setText("")
        self.lb_programa_origem.setText("")
        self.lb_acao_origem_2.setText("")

    def envio_email(self):
        inicio = self.ui.edicaoController.view.montar_data(self._dados['DATA_EMAIL_INICIAL'])
        data = datetime.now()
        hoje = QDate(data.year, data.month, data.day)

        self.verificar_dias(inicio, hoje)
        if (str(self._dados['DATA_CONTATO_1_ORIGEM']) != 'nan' and str(self._dados['DATA_CONTATO_1_ORIGEM']) != 'NaT') and (str(self._dados['CONTATO_1_ORIGEM']) != 'nan' and str(self._dados['CONTATO_1_ORIGEM']) != ''):
            self.verificar_dias(self.ui.edicaoController.view.montar_data(self._dados['DATA_CONTATO_1_ORIGEM']), hoje)
        if (str(self._dados['DATA_CONTATO_1_DESTINO']) != 'nan' and str(self._dados['DATA_CONTATO_1_DESTINO']) != 'NaT') and (str(self._dados['CONTATO_1_DESTINO']) != 'nan' and str(self._dados['CONTATO_1_DESTINO']) != ''):
            self.verificar_dias(self.ui.edicaoController.view.montar_data(self._dados['DATA_CONTATO_1_DESTINO']), hoje)
        if (str(self._dados['DATA_CONTATO_2_ORIGEM']) != 'nan' and str(self._dados['DATA_CONTATO_2_ORIGEM']) != 'NaT') and (str(self._dados['CONTATO_2_ORIGEM']) != 'nan' and str(self._dados['CONTATO_2_ORIGEM']) != ''):
            self.verificar_dias(self.ui.edicaoController.view.montar_data(self._dados['DATA_CONTATO_2_ORIGEM']), hoje)
        if (str(self._dados['DATA_CONTATO_2_DESTINO']) != 'nan' and str(self._dados['DATA_CONTATO_2_DESTINO']) != 'NaT') and (str(self._dados['CONTATO_2_DESTINO']) != 'nan' and str(self._dados['CONTATO_2_DESTINO']) != ''):
            self.verificar_dias(self.ui.edicaoController.view.montar_data(self._dados['DATA_CONTATO_2_DESTINO']), hoje)
        if (str(self._dados['DATA_CONTATO_3_ORIGEM']) != 'nan' and str(self._dados['DATA_CONTATO_3_ORIGEM']) != 'NaT') and (str(self._dados['CONTATO_3_ORIGEM']) != 'nan' and str(self._dados['CONTATO_3_ORIGEM']) != ''):
            self.verificar_dias(self.ui.edicaoController.view.montar_data(self._dados['DATA_CONTATO_3_ORIGEM']), hoje)
        if (str(self._dados['DATA_CONTATO_3_DESTINO']) != 'nan' and str(self._dados['DATA_CONTATO_3_DESTINO']) != 'NaT') and (str(self._dados['CONTATO_3_DESTINO']) != 'nan' and str(self._dados['CONTATO_3_DESTINO']) != ''):
            self.verificar_dias(self.ui.edicaoController.view.montar_data(self._dados['DATA_CONTATO_3_DESTINO']), hoje)
            return

    def verificar_dias(self, inicio, fim):
        if inicio.daysTo(fim) < 4:
            self.frame_4.setStyleSheet("""QFrame{ border: 1px solid rgb(238, 238, 238)	;border-left: 3px solid rgb(50,205,50);}""")
        elif inicio.daysTo(fim) >= 5 and inicio.daysTo(fim) < 10:
            self.frame_4.setStyleSheet("""QFrame{ border: 1px solid rgb(238, 238, 238)	;border-left: 3px solid rgb(255,255,0);}""")
        elif inicio.daysTo(fim) >= 10:
            self.frame_4.setStyleSheet("""QFrame{ border: 1px solid rgb(238, 238, 238)	;border-left: 3px solid rgb(255,0,0);}""")

    def exibirDetalhes(self):
        self.ui.view.stackedWidget.setCurrentIndex(1)
        self._dados = self.ui.db.select_decreto(int(self._dados['id']))
        self.ui.dados = self._dados
        self.ui.edicaoController.inserir_dados()
        self.ui.edicaoController.ativar_email()

    def marcar(self):
        try:
            if self.check_relatorio.isChecked() and not((self._dados['id']) in self.ui.principalController.relatorio):
                self.ui.principalController.relatorio.append((self._dados['id']))
            elif not self.check_relatorio.isChecked() and ((self._dados['id']) in self.ui.principalController.relatorio):
                self.ui.principalController.relatorio.remove((self._dados['id']))
        except ValueError:
            return

    def get_id(self):
        return self._dados['id']

    def get_dados(self):
        return self._dados

    def ocultar_seta(self):
        self.btn_detalhes.setVisible(False)

