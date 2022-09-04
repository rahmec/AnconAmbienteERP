from models.MapperMezzi import MapperMezzi

class ControlloreMezzo:
    def __init__(self):
        self.mapper = MapperMezzi()

    def get_mezzo(self, id):
        return self.mapper.get_mezzo(id)
    
    def get_mezzi(self):
        return self.mapper.get_mezzi()
    
    def get_mezzi_disponibili(self, data_inizio, data_fine):
        return self.mapper.get_mezzi_disponibili(data_inizio, data_fine)

    def insert_mezzo(self, targa, tipo, allestimento, iscrizione_albo, patente, stato):
        return self.mapper.insert_operatore(targa, tipo, allestimento, iscrizione_albo, patente, stato)

    def ricerca_mezzi(self, text):
        return self.mapper.ricerca_mezzi(text)

    def elimina_mezzi(self, mezzi):
        return self.mapper.elimina_mezzi(mezzi)    

    def modifica_mezzo(self, mezzo):
        return self.mapper.update_mezzo(mezzo.get_id_mezzo(), mezzo)
