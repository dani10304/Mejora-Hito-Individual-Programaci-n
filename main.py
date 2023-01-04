import re
#creamos una clase llamada cliente
class Cliente:
    #definimos el método init con todos los datos del cliente
    def __init__(self, nombre, apellido, pais, telefono, correo, password):
        self.nombre = nombre
        self.apellido = apellido
        self.pais = pais
        self.telefono = telefono
        self.correo = correo
        self.password = password
    #definimos la función para que nos muestre por consola que el usuario se ha registrado
    def RegistroCliente(self):
      print(f'El cliente {self.nombre}, ha sido registrado con sus datos')

def es_direccion_correo_valida(direccion):
  # Utiliza una expresión regular para verificar si la dirección de correo electrónico cumple con el formato válido
  coincidencia = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', direccion)
  if coincidencia == None:
    return False
  return True

# Prueba la función con algunas direcciones de correo electrónico
direcciones = ['juanperez@gmail.com', 'mi@correo', 'anagolez@gmail.com']
for direccion in direcciones:
  resultado = es_direccion_correo_valida(direccion)
  print(f'{direccion}: {resultado}')

#Aquí llamamos a los dos clientes a registrar
cliente1 = Cliente("Juan", "Pérez", "España", "654879210", "juanperez@gmail.com", "juaitopz")
cliente2 = Cliente("Ana", "González", "España", "694852015", "anagolez@gmail.com", "anitagon")
#y por último llamamos al método registroCliete con los dos clientes anteriores
cliente1.RegistroCliente()
cliente2.RegistroCliente()

#Creamos un diccionario en el cual introducimos los productos con su nombre, precio y cantidad
productos = [
  { "nombre": "Zapatillas de deporte", "precio": 100, "cantidad": 5 },
  { "nombre": "Camisa de algodón", "precio": 50, "cantidad": 3 },
  { "nombre": "Pantalón de mezclilla", "precio": 75, "cantidad": 4 }
]

# Creamos el diccionario de la compra
compra = {
  "cliente": input('dime que cliente ha efectuado la compra: '),
  "pais": "España",
  "productos": [],
  "total": 0
}

# Solicitamos al usuario que seleccione los productos a comprar
print("Selecciona los productos a comprar:")
for i, producto in enumerate(productos):
  print(f"{i+1}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad disponible: {producto['cantidad']}")
print("Escribe el número de los productos separados por comas (ej: 1,3,4) o escribe 'finalizar' para terminar la compra")
seleccion = input("> ")

# Mientras el usuario no escriba "finalizar", seguimos pidiendo productos
while seleccion != "finalizar":
  try:
    # Convertimos la selección a una lista de números
    seleccion = [int(x) for x in seleccion.split(",")]
    # Agregamos cada producto seleccionado al diccionario de la compra
    for i in seleccion:
      # Decrementamos la cantidad disponible del producto
      productos[i-1]["cantidad"] -= 1
      # Agregamos el producto a la compra
      compra["productos"].append(productos[i-1])
      # Incrementamos el total de la compra
      compra["total"] += productos[i-1]["precio"]
    # Volvemos a solicitar productos al usuario
    print("Selecciona otros productos o escribe 'finalizar' para terminar la compra")
    seleccion = input("> ")
  except ValueError:
    print("Por favor, ingresa una lista de números separados por comas o escribe 'finalizar' para terminar la compra")
    seleccion = input("> ")

# Mostramos la información de la compra
print(f"Compra realizada por {compra['cliente']} al pais {compra['pais']}:")
for producto in compra["productos"]:
  print(f"- {producto['nombre']} por un precio de {producto['precio']}")

#imprimimos por consola el precio total de la compra
print(f"Total: {compra['total']} euros")

#queremos hacerle un descuento del 10% por su compra navideña
precio_original = int(input('dime el precio total de su pedido: '))
porcentaje_descuento = 10

#introducimos las formulas del descuento y el precio final
descuento = precio_original * porcentaje_descuento / 100
precio_con_descuento = precio_original - descuento

#imprimimos por consola el precio con descuento
print(f"Precio con descuento: ${precio_con_descuento:.2f}")

# Define las opciones de pago disponibles
payment_options = ['tarjeta de crédito', 'Pay Pal']

# Pregunte al usuario por su opción de pago
print("Seleccione una opción de pago:")

# Muestra una lista de opciones de pago al usuario
for i, option in enumerate(payment_options):
    print(f"{i+1}. {option}")

# Pida al usuario que ingrese su opción de pago
selected_option = input("Ingrese el número de la opción deseada: ")

# Convierte la opción seleccionada por el usuario a un número entero
selected_option = int(selected_option)

# Obtiene la opción de pago seleccionada por el usuario
selected_payment_option = payment_options[selected_option - 1]

# Muestra la opción de pago seleccionada por el usuario
print(f"Ha seleccionado la opción de pago: {selected_payment_option}")

#enviamos la factura al cliente
print(f"la factura total de ${precio_con_descuento:.2f} euros ha sido enviada al correo mediante un documento PDF")

#introduce los datos de su compra
idcompra=int(input('introduce el id de compra enviado en tu factura: '))
fecha=input('introduce la fecha de compra en dd/mm/yyyy: ')
telefono=int(input('introduce tu número de telefono: '))

#imprime el mensaje  de que puede seguir la compra a través del SMS
print('Puedes seguir la compra mediante el SMS de tu telefono móvil')


