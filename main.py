# Importación de clases

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Restaurante Amazónico")

# Crear productos
producto1 = Producto("Encebollado", 4.50, "Plato Principal")
producto2 = Producto("Jugo Natural", 2.00, "Bebida")
producto3 = Producto("Tigrillo", 5.00, "Desayuno")

# Crear clientes
cliente1 = Cliente("Juan Pérez", "1234567890")
cliente2 = Cliente("María Gómez", "0987654321")

# Registrar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Registrar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print("===== SISTEMA DE GESTIÓN DE RESTAURANTE =====")
print(f"Nombre del restaurante: {restaurante.nombre}")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()
