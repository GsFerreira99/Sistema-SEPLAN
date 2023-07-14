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
            self.radio_statusMetas.setChecked(True)
            self.radio_statusEnviado.setChecked(True)
            self.radio_statusSistema.setChecked(True)
            self.radio_metaOrigemAtual.setChecked(True)
            self.radio_metaSuplementadoOrigem.setChecked(True)
            self.radio_metaDestinoAtual.setChecked(True)
            self.radio_metaSuplementadoDestino.setChecked(True)
            self.radio_dataEmail.setChecked(True)
            self.radio_contatosDestino.setChecked(True)
            self.radio_contatosOrigem.setChecked(True)

            self.radio_permaneceMetaOrigem.setChecked(True)
            self.radio_permaneceMetaDestino.setChecked(True)
            self.radio_geraEmailDestino.setChecked(True)
            self.radio_geraEmailOrigem.setChecked(True)
        else:
            self.radio_statusMetas.setChecked(False)
            self.radio_statusSistema.setChecked(False)
            self.radio_statusEnviado.setChecked(False)
            self.radio_metaOrigemAtual.setChecked(False)
            self.radio_metaSuplementadoOrigem.setChecked(False)
            self.radio_metaDestinoAtual.setChecked(False)
            self.radio_metaSuplementadoDestino.setChecked(False)
            self.radio_dataEmail.setChecked(False)
            self.radio_contatosDestino.setChecked(False)
            self.radio_contatosOrigem.setChecked(False)
            self.radio_permaneceMetaOrigem.setChecked(False)
            self.radio_permaneceMetaDestino.setChecked(False)
            self.radio_geraEmailDestino.setChecked(False)
            self.radio_geraEmailOrigem.setChecked(False)
