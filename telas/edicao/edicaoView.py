from media.ui_edicao import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate
from datetime import datetime
import pandas as pd

from funcoes.genericos import filtro_dinheiro




class EdicaoView(Ui_Form, QWidget):

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.ui = ui
        self.atualizar_data()

        self.btn_salvar_espelhado.setEnabled(True)

        self.inputCheck_permaneceMetaOrigem.clicked.connect(self.permanece_decreto)
        self.inputCheck_permaneceMetaDestino.clicked.connect(self.permanece_decreto)

    def atualizar_data(self):
        dateNow = datetime.now()
        data = QDate(dateNow.year, dateNow.month, dateNow.day)
        
        self.inputDate_emailInicial.setDate(data)

        self.inputDate_origem1.setDate(data)
        self.inputDate_origem2.setDate(data)
        self.inputDate_origem3.setDate(data)

        self.inputDate_destino1.setDate(data)
        self.inputDate_destino2.setDate(data)
        self.inputDate_destino3.setDate(data)

    def preencher_campos(self, dados):
        self.atualizar_data()
        self.limpar()

        self.lb_decreto_info.setText(str(dados['N_DECRETO']))
        if dados['DATA_ALTERACAO_ORCAMENTARIA'] != None and type(dados['DATA_ALTERACAO_ORCAMENTARIA']) != str:
            self.lb_dataDecreto_info.setText(str(dados['DATA_ALTERACAO_ORCAMENTARIA'].strftime('%d/%m/%Y')))

        if str(dados['EMAIL_INICIAL']) != 'nan':
            self.input_origem_contato1_2.setText(str(dados['EMAIL_INICIAL']))
        
        self.lb_origem_orgao_info.setText(f"{dados['ORGAO_ANULADO']} - {dados['NOME_ORGAO_ANULADO']}")
        self.lb_origem_programa_info.setText(f"{dados['ID_PROGRAMA_ANULADO']} - {dados['PROGRAMA_ANULADO']}")
        self.lb_origem_acao_info.setText(f"{dados['ID_ACAO_ANULADO']} - {dados['ACAO_ANULADO']}")
        self.lb_origem_acao_info_13.setText(f"{dados['NOME_PRODUTO_ANULADO']}")

        self.lb_destino_orgao_info.setText(f"{dados['NOME_ORGAO_SUPLEMENTADO']} - {dados['NOME_ORGAO_SUPLEMENTADO2']}")
        self.lb_destino_acao_info.setText(f"{dados['ID_ACAO_SUPLEMENTADO']} - {dados['ACAO_SUPLEMENTADO']}")
        self.lb_destino_programa_info.setText(f"{dados['ID_PROGRAMA_SUPLEMENTADO']} - {dados['PROGRAMA_SUPLEMENTADO']}")
        self.lb_origem_acao_info_15.setText(f"{dados['NOME_PRODUTO_SUPLEMENTADO']}")

        self.lb_valor_info.setText(f"{filtro_dinheiro(dados['VALOR_FINANCEIRO'])}")

        if str(dados['VALOR_FISICO_ATUAL_ANULADO']) != 'nan':
            self.input_metaOrigemAtual.setText(str(dados['VALOR_FISICO_ATUAL_ANULADO']))
            self.lb_origem_acao_info_3.setText(f"{dados['VALOR_FISICO_ATUAL_ANULADO']}")
        if str(dados['VALOR_FISICO_ATUAL_SUPLEMENTADO']) != 'nan':
            self.input_metaOrigemAtual_2.setText(str(dados['VALOR_FISICO_ATUAL_SUPLEMENTADO']))
            self.lb_origem_acao_info_11.setText(f"{dados['VALOR_FISICO_ATUAL_SUPLEMENTADO']}")

        #DATAS
        if str(dados['DATA_EMAIL_INICIAL']) != 'nan' and str(dados['DATA_EMAIL_INICIAL']) != 'NaT':
            self.inputDate_emailInicial.setDate(self.montar_data(dados['DATA_EMAIL_INICIAL']))
        
        if str(dados['DATA_CONTATO_1_ORIGEM']) != 'nan' and str(dados['DATA_CONTATO_1_ORIGEM']) != 'NaT':
            self.inputDate_origem1.setDate(self.montar_data(dados['DATA_CONTATO_1_ORIGEM']))
        if str(dados['DATA_CONTATO_2_ORIGEM']) != 'nan' and str(dados['DATA_CONTATO_2_ORIGEM']) != 'NaT':
            self.inputDate_origem2.setDate(self.montar_data(dados['DATA_CONTATO_2_ORIGEM']))
        if str(dados['DATA_CONTATO_3_ORIGEM']) != 'nan' and str(dados['DATA_CONTATO_3_ORIGEM']) != 'NaT':
            self.inputDate_origem3.setDate(self.montar_data(dados['DATA_CONTATO_3_ORIGEM']))
        if str(dados['DATA_CONTATO_1_DESTINO']) != 'nan' and str(dados['DATA_CONTATO_1_DESTINO']) != 'NaT':
            self.inputDate_destino1.setDate(self.montar_data(dados['DATA_CONTATO_1_DESTINO']))
        if str(dados['DATA_CONTATO_2_DESTINO']) != 'nan' and str(dados['DATA_CONTATO_2_DESTINO']) != 'NaT':
            self.inputDate_destino2.setDate(self.montar_data(dados['DATA_CONTATO_2_DESTINO']))
        if str(dados['DATA_CONTATO_3_DESTINO']) != 'nan' and str(dados['DATA_CONTATO_3_DESTINO']) != 'NaT':
            self.inputDate_destino3.setDate(self.montar_data(dados['DATA_CONTATO_3_DESTINO']))

        #CONTATOS ORIGEM  
        if str(dados['CONTATO_1_ORIGEM']) != 'nan':
            self.input_origem_contato1.setText(str(dados['CONTATO_1_ORIGEM']))
        if str(dados['STATUS_1_ORIGEM']) != 'nan':
            self.input_origem_status1.setText(str(dados['STATUS_1_ORIGEM']))
        
        if str(dados['CONTATO_2_ORIGEM']) != 'nan':
            self.input_origem_contato2.setText(str(dados['CONTATO_2_ORIGEM']))
        if str(dados['STATUS_2_ORIGEM']) != 'nan':
            self.input_origem_status2.setText(str(dados['STATUS_2_ORIGEM']))
        
        if str(dados['CONTATO_3_ORIGEM']) != 'nan':
            self.input_origem_contato3.setText(str(dados['CONTATO_3_ORIGEM']))
        if str(dados['STATUS_3_ORIGEM']) != 'nan':
            self.input_origem_status3.setText(str(dados['STATUS_3_ORIGEM']))

        #CONTATOS DESTINO 
        if str(dados['CONTATO_1_DESTINO']) != 'nan':
            self.input_destino_contato1.setText(str(dados['CONTATO_1_DESTINO']))
        if str(dados['STATUS_1_DESTINO']) != 'nan':
            self.input_destino_status1.setText(str(dados['STATUS_1_DESTINO']))
        
        if str(dados['CONTATO_2_DESTINO']) != 'nan':
            self.input_destino_contato2.setText(str(dados['CONTATO_2_DESTINO']))
        if str(dados['STATUS_2_DESTINO']) != 'nan':
            self.input_destino_status2.setText(str(dados['STATUS_2_DESTINO']))
        
        if str(dados['CONTATO_3_DESTINO']) != 'nan':
            self.input_destino_contato3.setText(str(dados['CONTATO_3_DESTINO']))
        if str(dados['STATUS_3_DESTINO']) != 'nan':
            self.input_destino_status3.setText(str(dados['STATUS_3_DESTINO']))

        if str(dados['NOVA_META_FISICA_ANULADO']) != 'nan':
            self.input_metaAnulado.setText(str(dados['NOVA_META_FISICA_ANULADO']))
        if str(dados['NOVA_META_FISICA_SUPLEMENTADO']) != 'nan':
            self.input_metaSuplementado.setText(str(dados['NOVA_META_FISICA_SUPLEMENTADO']))

        self.limpar_checkBox()

        if str(dados['EMAIL_ENVIADO']) == 'ok':
            self.inputCheck_emailEnviado.setChecked(True)
        if str(dados['INSERIDO_METAS']) == 'ok':
            self.inputCheck_inseridoMetas.setChecked(True)
        if str(dados['ATUALIZADO_NO_SISTEMA']) == 'ok':
            self.inputCheck_atualizadoSistema.setChecked(True)

        self.inputCheck_geraEmailOrigem.setChecked(dados['NAO_GERA_EMAIL_ORIGEM'])
        self.inputCheck_geraEmailDestino.setChecked(dados['NAO_GERA_EMAIL_DESTINO'])

        self.inputCheck_permaneceMetaOrigem.setChecked(dados['PERMANECE_DECRETO_ORIGEM'])
        self.inputCheck_permaneceMetaDestino.setChecked(dados['PERMANECE_DECRETO_DESTINO'])


        self.ativar_campos(dados)

    def permanece_decreto(self):
        text = 'permanece a mesma meta'

        if self.inputCheck_permaneceMetaOrigem.isChecked() is True:
            self.input_metaAnulado.setEnabled(False)
            self.input_metaAnulado.setText(text)
        else:
            self.input_metaAnulado.setEnabled(True)

        if self.inputCheck_permaneceMetaDestino.isChecked() is True:
            self.input_metaSuplementado.setText(text)
            self.input_metaSuplementado.setEnabled(False)
        else:
            self.input_metaSuplementado.setEnabled(True)



    def ativar_campos(self, dados):
          return  

    def limpar(self):
        self.lb_decreto_info.setText("")
        self.lb_dataDecreto_info.setText("")
        self.input_origem_contato1_2.setText("")
        self.lb_origem_orgao_info.setText("")
        self.lb_origem_programa_info.setText("")
        self.lb_origem_acao_info.setText("")
        self.lb_origem_acao_info_13.setText("")
        self.lb_destino_orgao_info.setText("")
        self.lb_destino_acao_info.setText("")
        self.lb_destino_programa_info.setText("")
        self.lb_origem_acao_info_15.setText("")
        self.lb_valor_info.setText("")
        self.input_metaOrigemAtual.setText("")
        self.lb_origem_acao_info_3.setText("")
        self.input_metaOrigemAtual_2.setText("")
        self.lb_origem_acao_info_11.setText("")

        self.input_origem_contato1_2.setText('')

        self.input_origem_contato1.setText('')
        self.input_origem_contato2.setText('')
        self.input_origem_contato3.setText('')
        self.input_origem_status1.setText('')
        self.input_origem_status2.setText('')
        self.input_origem_status3.setText('')

        self.input_destino_contato1.setText('')
        self.input_destino_contato2.setText('')
        self.input_destino_contato3.setText('')
        self.input_destino_status1.setText('')
        self.input_destino_status2.setText('')
        self.input_destino_status3.setText('')

        self.input_metaAnulado.setText('')
        self.input_metaSuplementado.setText('')

    def limpar_checkBox(self):
        self.inputCheck_emailEnviado.setChecked(False)
        self.inputCheck_inseridoMetas.setChecked(False)
        self.inputCheck_atualizadoSistema.setChecked(False)
        self.inputCheck_geraEmailOrigem.setChecked(False)
        self.inputCheck_geraEmailDestino.setChecked(False)
        self.inputCheck_permaneceMetaOrigem.setChecked(False)
        self.inputCheck_permaneceMetaDestino.setChecked(False)

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
