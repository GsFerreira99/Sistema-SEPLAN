from media.ui_main import Ui_Form
from PyQt5.QtWidgets import QWidget




class MainView(Ui_Form, QWidget):

    def __init__(self, parent=None):
        """Cria a janela principal do sistema onde são inseridas todas as outras telas"""
        super().__init__(parent)
        super().setupUi(self)
