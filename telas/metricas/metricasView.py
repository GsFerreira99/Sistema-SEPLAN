from media.ui_metricas import Ui_Form
from PyQt5.QtWidgets import QWidget, QMainWindow


class MetricasView(Ui_Form, QMainWindow):

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.ui = ui

        self.lb_score3.setText("PRODUTIVIDADE DO SETOR")
        self.lb_score2.setText("ATUALIZAÇÃO DE PPA")
        self.lb_score1.setText("PERMANENCIA DE METAS")