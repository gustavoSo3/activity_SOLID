from databaseInterface import Database
class Reporte:
    def __init__(self, db:Database) -> None:
        self.db
    
    def abrir(self):
        '''Método que abrirá la conexión con la base de datos'''
        self.db.abrir()
    
    def cerrar(self):
        '''Método que cerrará la conexión con la base de datos'''
        self.db.cerrar()
