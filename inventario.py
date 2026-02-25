import json
from producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.json"):
        # Diccionario: clave = ID, valor = Producto
        self.productos = {}
        self.archivo = archivo
        self.cargar()

    # ===============================
    # Agregar producto
    # ===============================
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ El ID ya existe.")
            return

        self.productos[producto.get_id()] = producto
        self.guardar()
        print("✅ Producto agregado.")

    # ===============================
    # Eliminar producto
    # ===============================
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar()
            print("🗑 Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    # ===============================
    # Actualizar producto
    # ===============================
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar()
            print("✏ Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    # ===============================
    # Buscar por nombre
    # ===============================
    def buscar_producto(self, nombre):
        resultados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        if resultados:
            for p in resultados:
                print(p)
        else:
            print("❌ No se encontraron coincidencias.")

    # ===============================
    # Mostrar todos
    # ===============================
    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        for p in self.productos.values():
            print(p)

    # ===============================
    # Guardar en archivo JSON
    # ===============================
    def guardar(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump(
                    {id_p: p.to_dict() for id_p, p in self.productos.items()},
                    f,
                    indent=4
                )
        except Exception as e:
            print(f"Error al guardar archivo: {e}")

    # ===============================
    # Cargar desde archivo JSON
    # ===============================
    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                for id_p, data in datos.items():
                    self.productos[id_p] = Producto.from_dict(data)
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo.")
            self.guardar()
        except Exception as e:
            print(f"Error al cargar archivo: {e}")
