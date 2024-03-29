import os

from PyQt5 import QtWidgets, QtCore, uic
import sys
import xz_rc

from controllers.ControlloreMezzi import ControlloreMezzi

class VistaModificaMezzo(QtWidgets.QMainWindow):
    controller = ControlloreMezzi()

    def __init__(self, parent, mezzo):
        # Costruttore 'VistaModificaMezzo'
        # :param parent: Vista che ha richiesto l'utilizzo di questa vista, posso utilizzare i metodi di parent
        # :param cliente: Cliente che si vuole modificare
        super(VistaModificaMezzo, self).__init__(parent)  # Call the inherited classes __init__ method
        dirname = os.path.dirname(__file__)
        gui_file = os.path.join(dirname, '../gui/modifica_mezzo.ui')
        uic.loadUi(gui_file, self)  # Load the .ui file
        self.mezzo=mezzo
        self.annulla_button.clicked.connect(self.close)
        self.salva_button.clicked.connect(self.modifica)
        self.targa_field.setText(mezzo.get_targa_mezzo())
        self.modello_field.setText(mezzo.get_tipo_mezzo())
        self.allestimento_field.setText(mezzo.get_allestimento_mezzo())
        self.iscrizione_datepicker.setDateTime(QtCore.QDateTime.fromString(mezzo.get_iscrizione_mezzo(),"yyyy-mm-dd"))
        self.stato_combo.setCurrentIndex(mezzo.get_stato_mezzo())
        self.patente_combo.setCurrentText(mezzo.get_patente_mezzo())
        self.targa_field.editingFinished.connect(self.check_targa)
        self.modello_field.editingFinished.connect(self.check_tipo)
        self.allestimento_field.editingFinished.connect(self.check_allestimento)
        self.iscrizione_datepicker.setMinimumDate(QtCore.QDate.currentDate())

    def modifica(self):
        # Metodo che salva i cambiamenti effettuati
        targa_validity = self.check_targa()
        tipo_validity = self.check_tipo()
        allestimento_validity = self.check_allestimento()
        if targa_validity and tipo_validity and allestimento_validity:
            self.mezzo.set_targa_mezzo(self.targa_field.text())
            self.mezzo.set_tipo_mezzo(self.modello_field.text())
            self.mezzo.set_allestimento_mezzo(self.allestimento_field.text())
            self.mezzo.set_iscrizione_mezzo(self.iscrizione_datepicker.date().toString("yyyy-MM-dd"))
            self.mezzo.set_stato(self.stato_combo.currentIndex())
            self.mezzo.set_patente_mezzo(self.patente_combo.currentText())
            self.controller.modifica_mezzo(self.mezzo)
            self.parent().update()
            self.close()


    def check_targa(self):
        # Metodo per controllo campo 'targa'
        if len(self.targa_field.text()) == 0:
            self.targa_error.setText("Inserire targa del mezzo")
            return False
        else:
            self.targa_error.setText("")
            return True

    def check_tipo(self):
        # Metodo per controllo campo 'tipo'
        if len(self.modello_field.text()) == 0:
            self.modello_error.setText("Inserire modello del mezzo")
            return False
        else:
            self.modello_error.setText("")
            return True

    def check_allestimento(self):
        # Metodo per controllo campo 'allestimento'
        if len(self.allestimento_field.text()) == 0:
            self.allestimento_error.setText("Inserire l'allestimento del mezzo")
            return False
        else:
            self.allestimento_error.setText("")
            return True
