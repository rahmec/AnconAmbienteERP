import os

from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from models.Mezzo import Mezzo
from views.VistaModificaMezzo import VistaModificaMezzo

class VistaMezzo(QtWidgets.QMainWindow):
    def __init__(self, parent, mezzo):
        # Costruttore 'VistaMezzo'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        # :param mezzo: mezzo dal quale visualizzare le informazioni
        super(VistaMezzo, self).__init__()  # Call the inherited classes __init__ method
        dirname = os.path.dirname(__file__)
        gui_file = os.path.join(dirname, '../gui/visualizza_mezzo.ui')
        uic.loadUi(gui_file, self)  # Load the .ui file
        self.mezzo = mezzo
        self.parent = parent
        self.id_label.setText(str(mezzo.get_id_mezzo()))
        self.targa_label.setText(mezzo.get_targa_mezzo())
        self.modello_label.setText(mezzo.get_tipo_mezzo())
        self.allestimento_label.setText(mezzo.get_allestimento_mezzo())
        self.iscrizione_label.setText(mezzo.get_iscrizione_mezzo())
        self.patente_label.setText(mezzo.get_patente_mezzo())
        stato=mezzo.get_stato_mezzo()
        if stato == 0:
            stato = "Disponibile"
        else:
            stato = "Non Disponibile"
        self.stato_label.setText(stato)
        self.indietro_button.clicked.connect(self.close)
        self.modifica_button.clicked.connect(self.go_modifica)

    def go_modifica(self):
        # Metodo per passare alla vista di modifica
        self.vista_modificamezzo = VistaModificaMezzo(self, self.mezzo)
        self.vista_modificamezzo.show()   
        self.close()   