from media.ui_email import Ui_Form
from PyQt5.QtWidgets import QWidget, QDialog




class EmailView(Ui_Form, QDialog):

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.ui = ui

        self.setModal(True)
