from media.ui_selectEspelhamento import Ui_Form
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QSpacerItem, QSizePolicy
from telas.dashboard.itemTabelaView import ItemTabelaView
from PyQt5.QtCore import Qt


class SelectEspelhamentoView(Ui_Form, QDialog):

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.ui = ui

        self.setModal(True)
        self.radio_todos.clicked.connect(lambda: self.marcar_todos())

    def marcar_todos(self):
        if self.radio_todos.isChecked():
            self.radio_status.setChecked(True)
            self.radio_metaNova.setChecked(True)
            self.radio_dataEmail.setChecked(True)
            self.radio_metaAtual.setChecked(True)
            self.radio_contatosDestino.setChecked(True)
            self.radio_contatosOrigem.setChecked(True)
        else:
            self.radio_status.setChecked(False)
            self.radio_metaNova.setChecked(False)
            self.radio_dataEmail.setChecked(False)
            self.radio_metaAtual.setChecked(False)
            self.radio_contatosDestino.setChecked(False)
            self.radio_contatosOrigem.setChecked(False)
