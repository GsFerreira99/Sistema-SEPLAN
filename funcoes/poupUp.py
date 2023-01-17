from PyQt5.QtWidgets import QMessageBox

def Erro(mensagem, tipo, titulo="Confirmação",):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setIcon(tipo)
        msg.setText(mensagem)
        msg.addButton(QMessageBox.Ok)

        msg.exec_()