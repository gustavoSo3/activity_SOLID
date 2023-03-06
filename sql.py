import psycopg2

from activity_SOLID.producto import Producto


class SQL():

    def __init__(self) -> None:
        self.abrirSQL = psycopg2.connect(
            host='ec2-52-204-195-2.compute-1.amazonaws.com', database='products', user='', password='')
        self.cursor = self.abrirSQL.cursor()

    # Consultas

    # insertar()
    def insertar(self, producto: Producto) -> None:
        print('Insertar nuevo registro')    
        producto.nombre: str = input('Ingresa el nombre del producto:')
        producto.precio: float = input('Ingresa el precio del producto:')
        producto.cantidad: int = input('Ingresa el precio del producto:')

        self.cursor.execute('INSERT INTO PRODUCTOS (nombre, precio, cantidad) VALUES (' +
                            producto.nombre+', '+producto.precio+', '+producto.cantidad+')')
        print('Insert correcto')

    # actualizar()

    def actualizar(self, producto: Producto) -> None:
        print('Actualizar registro')
        print('Qué desea cambiar?')
        print('[1] - Nombre')
        print('[2] - Precio')
        print('[3] - Cantidad')
        opc: str = input()

        producto.nombre: str = input(
            'Ingresa el nombre del producto a actualizar: ')

        match opc:
            case '1':
                nuevoNombre: str = input('Ingresa el nuevo nombre: ')
                self.cursor.execute(
                    'UPDATE PRODUCTOS SET nombre = '+nuevoNombre+' WHERE ')

            case '2':
                nuevoPrecio: float = input('Ingresa el nuevo precio: ')

            case '3':
                nuevaCant: int = input('Ingresa la nueva cantidad: ')

    # eliminar()
