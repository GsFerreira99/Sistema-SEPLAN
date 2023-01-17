from inspect import Attribute
from posixpath import split
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import re
from funcoes.genericos import filtro_dinheiro

from funcoes.base_pdf import Pdf
    
    
class Relatorio(Pdf):

    def __init__(self, caminho, dados, filtro):
        super().__init__(caminho)

        self.filtro = filtro
        self.dados = dados
        self.y = 740
        self.gerar()

    def gerar(self):
        self.can = canvas.Canvas(self.packet)
        for j, i in enumerate(self.dados['id'].values):
            dados = self.dados[self.dados['id'] == i]
            self.preencher_filtro(self.filtro)
            self.preencher_decreto(dados)
            self.preencher_origem(dados)
            self.preencher_destino(dados)
            self.preencher_dataEmail(dados)
            self.preencher_valorRemanejado(dados)
            if j < len(self.dados):
                self.can.showPage()
        self.can.save()
        self.gerar_relatorio_mensal()

    def preencher_filtro(self, filtro):
        self.font(12)
        self.can.drawString(95, 706, f"{filtro}")
    
    def preencher_decreto(self, dados):
        self.font(12)
        self.can.drawString(95, 645, f"{dados['N_DECRETO'].values[0]}")
        try:
            self.can.drawString(410, 645, f"{dados['DATA_ALTERACAO_ORCAMENTARIA'].values[0].strftime('%d/%m/%Y')}")
        except AttributeError as error:
            print(error)

    def preencher_origem(self, dados):
        self.font(9)
        self.can.drawString(200, 597, f"{dados['ORGAO_ANULADO'].values[0]} - {dados['NOME_ORGAO_ANULADO'].values[0]}")
        self.can.drawString(200, 574, f"{dados['ID_PROGRAMA_ANULADO'].values[0]} - {dados['PROGRAMA_ANULADO'].values[0]}")
        self.can.drawString(200, 550, f"{dados['ID_ACAO_ANULADO'].values[0]} - {dados['ACAO_ANULADO'].values[0]}")
        self.can.drawString(200, 528, f"{dados['NOME_PRODUTO_ANULADO'].values[0]}")
        self.can.drawString(200, 505, f"{dados['NOVA_META_FISICA_ANULADO'].values[0]}")

    def preencher_destino(self, dados):
        self.font(9)
        self.can.drawString(200, 450, f"{dados['NOME_ORGAO_SUPLEMENTADO'].values[0]} - {dados['NOME_ORGAO_SUPLEMENTADO2'].values[0]}")
        self.can.drawString(200, 425, f"{dados['ID_PROGRAMA_SUPLEMENTADO'].values[0]} - {dados['PROGRAMA_SUPLEMENTADO'].values[0]}")
        self.can.drawString(200, 403, f"{dados['ID_ACAO_SUPLEMENTADO'].values[0]} - {dados['ACAO_SUPLEMENTADO'].values[0]}")
        self.can.drawString(200, 380, f"{dados['NOME_PRODUTO_SUPLEMENTADO'].values[0]}")
        self.can.drawString(200, 359, f"{dados['NOVA_META_FISICA_SUPLEMENTADO'].values[0]}")

    def preencher_dataEmail(self, dados):
        self.font(12)
        if dados['DATA_EMAIL_INICIAL'].values[0] != None:
            try:
                self.can.drawString(95, 310, f"{dados['DATA_EMAIL_INICIAL'].values[0].strftime('%d/%m/%Y')}")
                e = str(dados['EMAIL_INICIAL'].values[0])
                if e == '':
                    self.can.drawString(250, 310, f"{e}")
                    return
                try:
                    emails = re.split("[,\;|-]",e)
                except:
                    emails = [e]
                y = 310
                print(emails)
                for email in emails: 
                    self.can.drawString(250, y, f"{email}")
                    y-=15
            except AttributeError as error:
                print(error)
    
    def preencher_valorRemanejado(self, dados):
        self.font(12)
        self.can.drawString(95, 250, f"{filtro_dinheiro(dados['VALOR_FINANCEIRO'].values[0])}")

    def preencher_emailOrigem(self, dados):
        self.font(10)
        self.can.drawString(95, 230, f"{dados['DATA_CONTATO_1_ORIGEM'].values[0]}")
        self.can.drawString(275, 230, f"{dados['CONTATO_1_ORIGEM'].values[0]}")
        self.can.drawString(450, 230, f"{dados['STATUS_1_ORIGEM'].values[0]}")


        self.can.drawString(95, 215, f"{dados['DATA_CONTATO_2_ORIGEM'].values[0]}")
        self.can.drawString(275, 215, f"{dados['CONTATO_2_ORIGEM'].values[0]}")
        self.can.drawString(450, 215, f"{dados['STATUS_2_ORIGEM'].values[0]}")

        self.can.drawString(95, 200, f"{dados['DATA_CONTATO_3_ORIGEM'].values[0]}")
        self.can.drawString(275, 200, f"{dados['CONTATO_2_ORIGEM'].values[0]}")
        self.can.drawString(450, 200, f"{dados['STATUS_2_ORIGEM'].values[0]}")


    def preencher_emailDestino(self, dados):
        self.font(10)
        self.can.drawString(95, 115, f"{dados['DATA_CONTATO_1_DESTINO'].values[0]}")
        self.can.drawString(275, 115, f"{dados['CONTATO_1_DESTINO'].values[0]}")
        self.can.drawString(450, 115, f"{dados['STATUS_1_DESTINO'].values[0]}")


        self.can.drawString(95, 100, f"{dados['DATA_CONTATO_2_DESTINO'].values[0]}")
        self.can.drawString(275, 100, f"{dados['CONTATO_2_DESTINO'].values[0]}")
        self.can.drawString(450, 100, f"{dados['STATUS_2_DESTINO'].values[0]}")

        self.can.drawString(95, 85, f"{dados['DATA_CONTATO_3_DESTINO'].values[0]}")
        self.can.drawString(275, 85, f"{dados['CONTATO_3_DESTINO'].values[0]}")
        self.can.drawString(450, 85, f"{dados['STATUS_3_DESTINO'].values[0]}")
        