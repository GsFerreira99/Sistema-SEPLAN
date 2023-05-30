from media.ui_espelhamento import Ui_Form
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QSpacerItem, QSizePolicy
from telas.dashboard.itemTabelaView import ItemTabelaView
from PyQt5.QtCore import Qt


class EspelhamentoView(Ui_Form, QDialog):

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.ui = ui

        self.setModal(True)

    def preencher_scroll(self, dados, scroll):
        if len(dados) == 0:
            return
        widget = QWidget()

        vbox = QVBoxLayout()
        items = []

        for j, i in enumerate(dados.index):
            try:
                object = ItemTabelaView(self.ui, dados.iloc[j])
                object.btn_detalhes.setVisible(False)
                items.append(object)
                vbox.addWidget(object)
            except IndexError:
                pass

        verticalSpacer = QSpacerItem(2000, 40, QSizePolicy.Maximum, QSizePolicy.Expanding)
        vbox.addSpacerItem(verticalSpacer)
        widget.setLayout(vbox)
        scroll.setWidgetResizable(True)
        scroll.setAlignment(Qt.AlignTop)
        scroll.setWidget(widget)

        return items


    def preencher_todos(self, widgets):
        if len(widgets) == 0:
            return
        widget = QWidget()
        vbox = QVBoxLayout()

        for i in widgets[0]:
            try:
                vbox.addWidget(i)
            except IndexError:
                pass

        verticalSpacer = QSpacerItem(2000, 40, QSizePolicy.Maximum, QSizePolicy.Expanding)
        vbox.addSpacerItem(verticalSpacer)
        widget.setLayout(vbox)
        self.scrollArea_todos.setWidgetResizable(True)
        self.scrollArea_todos.setAlignment(Qt.AlignTop)
        self.scrollArea_todos.setWidget(widget)


    def limpar(self, dados):
        for widgets in dados.values():
            for i in widgets[1]:
                i.deleteLater()
                i = None