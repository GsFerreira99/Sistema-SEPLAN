from telas.metricas.metricasView import MetricasView


class MetricasController:

    def __init__(self, ui):
        """ Responsável por controlar tudo que acontece na tela Principal """
        self.ui = ui
        self.view = MetricasView(self.ui)

        self.view.btn_voltar.clicked.connect(self.mudar_tela)
        self.view.comboBox.currentIndexChanged.connect(lambda: self.dados())

    def dados(self):
        filtro = self.view.comboBox.currentText()
        if filtro == '':
            self.view.lb_filtro.setText("Filtro Atual: Todos")
            self.view.score_1.setText(str(round(self.ui.principalController._db.select_score_1, 2)))
            self.view.score_2.setText(str(round(self.ui.principalController._db.select_score_2, 2)))
        else:
            self.view.lb_filtro.setText(f"Filtro Atual: {filtro}")
            self.view.score_1.setText(str(round(self.ui.principalController._db.select_filtro_score_1(filtro), 2)))
            self.view.score_2.setText(str(round(self.ui.principalController._db.select_filtro_score_2(filtro), 2)))
    def mudar_tela(self):
        self.ui.view.stackedWidget.setCurrentIndex(0)

    def preencher_filtro(self):
        dados = self.ui.principalController._db.select_secretarias
        self.view.comboBox.clear()
        self.view.comboBox.addItem('')
        for i, j in enumerate(dados.index):
            self.view.comboBox.addItem(dados.iloc[j]['NOME_ORGAO_SUPLEMENTADO2'])
            #self.view.comboBox.addItem(dados.iloc[j]['NOME_ORGAO_ANULADO'])
        self.dados()
