from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot #Identificar cuando se ejecute el evento del boton
from ui_mainwindow import Ui_MainWindow #Importar libreria de la interfaz del designer en .py
from Actividad09_Particulas.particula import Particula
from Actividad09_Particulas.adminparticula import AdminParticula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.particulas = AdminParticula() #instancia en la clase MainWindow
        
        self.ui = Ui_MainWindow() #crear un objeto de una vista del designer
        self.ui.setupUi(self) #Las configuraciones que se hacen se incrustan en el objeto
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio) #Decirle que cuando le de click se conecte a la función
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar) #Conectar el evento del boton a la función
      
    def limpiar(self):
        self.ui.id_spinBox.setValue(0)
        self.ui.origenx_spinBox.setValue(0)
        self.ui.origeny_spinBox.setValue(0)
        self.ui.destinox_spinBox.setValue(0)
        self.ui.destinoy_spinBox.setValue(0)
        self.ui.velocidad_spinBox.setValue(0)
        self.ui.red_spinBox.setValue(0)
        self.ui.green_spinBox.setValue(0)
        self.ui.blue_spinBox.setValue(0)  
        
    def entrada_datos(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        
        return particula

    @Slot() #Decirle que la siguiente función detectara eventos click
    def click_agregar_inicio(self):
        self.particulas.agregar_inicio(self.entrada_datos())
        self.limpiar()
        
    @Slot()
    def click_agregar_final(self):
        self.particulas.agregar_final(self.entrada_datos())
        self.limpiar()
    
    @Slot()
    def mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))