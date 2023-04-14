from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Color, PatternFill
from openpyxl.utils import get_column_letter


class Relatorio_xls:

    def __init__(self, caminho:str, dados):
        self.__caminho = caminho
        self.__dados = dados
        self.__workbook = Workbook()

        self.plan_ativa = self.__workbook.active

        self.preencherPlanilha()

    def setTitulo(self, titulo:str="Relatório") -> None:
        self.plan_ativa.title = titulo

    def salvar(self) -> None:
        self.__workbook.save(self.__caminho)

    def cabecalho(self) -> None:
        tabela = {
            "A2": ["ÓRGÃO", Color(rgb='a4c2f4')],
            "B2": ["DECRETO", Color(rgb='a4c2f4')],
            "C2": ["DATA EMAIL", Color(rgb='a4c2f4')],
            "D2": ["ENDERECO EMAIL", Color(rgb='a4c2f4')],
            "E2": ["PENDENCIA", Color(rgb='00FF0000')],
        }

        for cel, value in tabela.items():
            self.plan_ativa[cel].font = Font(bold=True)
            self.plan_ativa[cel] = value[0]
            self.plan_ativa[cel].fill = my_fill = PatternFill(patternType='solid', fgColor=value[1])

    def preencherDados(self):
        for j, i in enumerate(self.__dados['id'].values):
            dados = self.__dados[self.__dados['id'] == i]
            self.inserirDecreto(dados, j+3)

    def inserirDecreto(self, dados, column:int) -> None:
        self.plan_ativa[f'A{column}'] = ''
        self.plan_ativa[f'B{column}'] = dados['N_DECRETO'].values[0]
        self.plan_ativa[f'C{column}'] = ''
        self.plan_ativa[f'D{column}'] = ''
        self.plan_ativa[f'E{column}'] = ''

    def preencherPlanilha(self) -> None:
        self.cabecalho()
        self.preencherDados()
        self.salvar()
