"""Database Interface"""

from abc import ABC
from producto import Producto

class Database(ABC):
    '''Interface para las bases de datos'''
    def insertar(self, producto : Producto) -> None:
        '''Método para insertar en la base de datos'''

    def actualizar(self, id : str, producto : Producto) -> None:
        '''Método para actualizar en la base de datos'''

    def eliminar(self, id : str) -> None:
        '''Método para eliminar en la base de datos'''
