from pymongo import MongoClient
from unittest import result

from activity_SOLID.producto import Producto


class MongoDB:
    def __init__(self) -> None:
        self.client = MongoClient("mongodb+srv://admin:root@cluster0.muthfez.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["Solid"]
        self.collection = self.db["Productos"]

    def insetar(self, producto:Producto) -> None:
        self.collection.insert_one({"id": producto.id, "name": producto.nombre, "precio": producto.precio, "cantidad": producto.cantidad})

    def actulizar(self, producto:Producto) -> None:
        result = self.collection.find(producto.id)
        self.collection.update_one(result)

    def delete(self, producto:Producto) -> None:
        result = self.collection.find(producto.id)
        self.collection.delete_one(result)

