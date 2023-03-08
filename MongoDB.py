"""Connection to MongoDB"""

from pymongo import MongoClient

from database import Database
from producto import Producto


class MongoDB(Database):
    """Connection to MongoDB"""

    def insetar(self, producto:Producto) -> None:
        """Insert in mongoDB"""
        self.collection.insert_one(
            {
                "id": producto.id,
                "name": producto.nombre,
                "precio": producto.precio,
                "cantidad": producto.cantidad
            }
        )

    def actulizar(self, id:int, producto: Producto) -> None:
        """Actualizar en mongo DB"""
        self.collection.update_one({"id":id}, {
                "id": producto.id,
                "name": producto.nombre,
                "precio": producto.precio,
                "cantidad": producto.cantidad
            })

    def eliminar(self, id: int) -> None:
        """Eliminar en mongoDB"""
        self.collection.delete_one({"id" : id})

    def abrir(self) -> None:
        self.client = MongoClient(
            "mongodb+srv://admin:root@cluster0.muthfez.mongodb.net/?retryWrites=true&w=majority"
        )
        self.db = self.client["Solid"]
        self.collection = self.db["Productos"]

    def cerrar(self) -> None:
        self.client.close()
