from Modelo.ventana_principal_modelo import Ventana_principal_Modelo
from Vista.ventana_principal_vista import Ventana_Principal_Vista

class Ventana_Principal_Controlador():
    def __init__(self):
        self.model = Ventana_principal_Modelo

        # 3> create view instance
        self.view = Ventana_Principal_Vista()

        self.view.opciones.add_command(label="Insertar", command = self.saludar)
        self.view.opciones.add_command(label="Visualizar",  command = self.saludar)
        self.view.opciones.add_command(label="Acerca de",  command = self.saludar)
        self.view.menuppal.add_cascade(label="Opciones", menu=self.view.opciones)
        self.view.root.config(menu=self.view.menuppal)

    def saludar(self):
        print("HOLA")