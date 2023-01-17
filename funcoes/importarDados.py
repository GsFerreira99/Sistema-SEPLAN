import pandas as pd


class ImportarDados:

    def __init__(self, caminho) -> None:
        self._caminho = caminho
        self._pd = pd.read_excel(self._caminho, sheet_name="Planilha1")

    @property
    def retornar_lista_dados(self):
        lista = []
        self._pd = self._pd.fillna('')
        for index, row in self._pd.iterrows():
            lista.append((
                row['N_DECRETO'],
                row['DOTACAO_SUPLEMENTADA'],
                row['DOTACAO_ANULADO'],
                row['VALOR_FINANCEIRO'],
                row['VALOR_FISICO_ATUAL_SUPLEMENTADO'],
                row['VALOR_FISICO_ATUAL_ANULADO'],
                self.converter_data(row['DATA_ALTERACAO_ORCAMENTARIA']),
                self.converter(row['NOME_ORGAO_SUPLEMENTADO']),
                self.converter(row['UNIDADE_SUPLEMENTADO']),
                row['NOME_ORGAO_SUPLEMENTADO2'],
                row['FUCAO_SUPLEMENTADO'],
                row['SUBFUNCAO_SUPLEMENTADO'],
                self.converter(row['ID_PROGRAMA_SUPLEMENTADO']),
                row['PROGRAMA_SUPLEMENTADO'],
                self.converter(row['ID_ACAO_SUPLEMENTADO']),
                row['ACAO_SUPLEMENTADO'],
                row['NATUREZA_DA_DESPESA_SUPLEMENTADO'],
                str(row['FONTE_DE_RECURSO_SUPLEMENTADO']),
                row['NOME_PRODUTO_SUPLEMENTADO'],
                self.converter(row['ORGAO_ANULADO']),
                self.converter(row['UNIDADE_ANULADO']),
                row['NOME_ORGAO_ANULADO'],
                row['FUNCAO_ANULADO'],
                row['SUBFUNCAO_ANULADO'],
                self.converter(row['ID_PROGRAMA_ANULADO']),
                row['PROGRAMA_ANULADO'],
                self.converter(row['ID_ACAO_ANULADO']),
                row['ACAO_ANULADO'],
                str(row['NATUREZA_DA_DESPEZA_ANULADA']),
                self.converter(row['FONTE_DE_RECURSO_ANULADA']),
                row['NOME_PRODUTO_ANULADO'],
                row['OCORRIDO'],
                row['COL_ALERTA'],
                self.converter_data(row['DATA_EMAIL_INICIAL']),
                row['EMAIL_INICIAL'],
                row['EMAIL_ENVIADO'],
                row['NOVA_META_FISICA_ANULADO'],
                row['NOVA_META_FISICA_SUPLEMENTADO'],
                row['INSERIDO_METAS'],
                row['ATUALIZADO_NO_SISTEMA'],
                self.converter_data(row['DATA_CONTATO_1_ORIGEM']),
                row['CONTATO_1_ORIGEM'],
                row['STATUS_1_ORIGEM'],
                self.converter_data(row['DATA_CONTATO_2_ORIGEM']),
                row['CONTATO_2_ORIGEM'],
                row['STATUS_2_ORIGEM'],
                self.converter_data(row['DATA_CONTATO_3_ORIGEM']),
                row['CONTATO_3_ORIGEM'],
                row['STATUS_3_ORIGEM'],
                self.converter_data(row['DATA_CONTATO_1_DESTINO']),
                row['CONTATO_1_DESTINO'],
                row['STATUS_1_DESTINO'],
                self.converter_data(row['DATA_CONTATO_2_DESTINO']),
                row['CONTATO_2_DESTINO'],
                row['STATUS_2_DESTINO'],
                self.converter_data(row['DATA_CONTATO_3_DESTINO']),
                row['CONTATO_3_DESTINO'],
                row['STATUS_3_DESTINO'],
            ))
        return lista

    def converter(self, campo):
        if type(campo) != str and campo != None:
            return int(campo)
        else:
            return campo

    def converter_data(self, data):
        try:
            if type(data) != str:
                return data
            elif len(data) == 10:
                return f"{data[6:]}-{data[3:5]}-{data[:2]}"
            else:
                return None
        except:
            return None