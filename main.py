from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import sys 

#Controlers
from telas.dashboard.dashboardController import DashBoardController
from telas.edicao.edicaoController import EdicaoController
from telas.metricas.metricasController import MetricasController
from telas.main.mainView import MainView


class App:
    def __init__(self):
        """Responsável por Iniciar a Aplicação"""
        self.view = MainView()

        self.edicaoController = EdicaoController(self)
        self.principalController = DashBoardController(self)
        self.metricasController = MetricasController(self)

        self.view.stackedWidget.insertWidget(0, self.principalController.view)
        self.view.stackedWidget.insertWidget(1, self.edicaoController.view)
        self.view.stackedWidget.insertWidget(2, self.metricasController.view)
        self.view.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = App()
    app.setWindowIcon(QIcon('icon.ico'))
    sys.exit(app.exec_())
