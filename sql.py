"""SQL Database connection"""
import psycopg2

from database import Database

from producto import Producto


class SQL(Database):
    """SQL Database Connection"""

    def insertar(self, producto: Producto) -> None:
        print("Insertar nuevo registro")
        self.cursor.execute("INSERT INTO PRODUCTOS (nombre, precio, cantidad) VALUES (" +
                            producto.nombre+", "+producto.precio+", "+producto.cantidad+")")
        print("Insert correcto")


    def actualizar(self, id : int, producto: Producto) -> None:
        print("Actualizar registro")
        self.cursor.execute(
            "UPDATE PRODUCTOS SET nombre = "+producto.nombre+
            ", cantidad ="+producto.cantidad+
            ", precio ="+producto.precio+
            " WHERE id ="+producto.id)
        print("Registro actualizado")

    def eliminar(self, id: int) -> None:
        print("Eliminar registro")
        self.cursor.execute("DELETE FROM PRODUCTOS WHERE id ="+id)
        print("Registro borrado")

    def abrir(self) -> None:
        self.abrir_sql = psycopg2.connect(
            host="ec2-52-204-195-2.compute-1.amazonaws.com",
            database="products",
            user="",
            password=""
        )
        self.cursor = self.abrir_sql.cursor()

    def cerrar(self) -> None:
        """Closes the database connection"""
        self.abrir_sql.close()
        