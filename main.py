from PySide2.QtWidgets import QPushButton, QApplication
import sys
from mainwindow import MainWindow

#Aplicación de Qt
app = QApplication()
window = MainWindow() #Instancia de la clase MainWindow
window.show() #Metodo de la clase (Mostrar)
#Qt loop (Evitar que se cierre la ventana)
sys.exit(app.exec_())