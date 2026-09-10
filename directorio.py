import json  # Librería nativa de Python para manejar archivos JSON

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_info(self):
        return f"Nombre: {self.nombre} - Teléfono: {self.telefono}"

# --- NUEVAS FUNCIONES DE PERSISTENCIA ---

def cargar_datos():
    # Intentamos abrir el archivo. Si no existe, devolvemos una lista vacía.
    try:
        # 'with open' asegura que el archivo se cierre automáticamente al terminar
        with open("mis_contactos.json", "r") as archivo:
            # Convertimos el texto del JSON a una lista de diccionarios de Python
            datos_cargados = json.load(archivo)
            
            # Reconstruimos los Objetos Contacto a partir de los diccionarios
            directorio_recuperado = []
            for dato in datos_cargados:
                nuevo_contacto = Contacto(dato["nombre"], dato["telefono"])
                directorio_recuperado.append(nuevo_contacto)
                
            return directorio_recuperado
            
    except FileNotFoundError:
        # Este error ocurre la primera vez que ejecutas el programa (el archivo no existe aún)
        return []

def guardar_datos(registro):
    # Traducimos la lista de Objetos a una lista de diccionarios
    datos_a_guardar = []
    for persona in registro:
        diccionario = {"nombre": persona.nombre, "telefono": persona.telefono}
        datos_a_guardar.append(diccionario)
        
    # Guardamos la lista de diccionarios en el archivo JSON
    # 'w' significa Write (escribir). Si el archivo no existe, lo crea.
    with open("mis_contactos.json", "w") as archivo:
        json.dump(datos_a_guardar, archivo, indent=4)  # indent=4 lo hace fácil de leer para humanos

# --- FUNCIONES DEL MENÚ ---

def agregar(registro):
    ciclo_nombre = True
    ciclo_telefono = True

    while ciclo_nombre:
        nombre = input("Ingresa el nombre completo del personal a registrar: ")
        if nombre.strip() != "":
            ciclo_nombre = False

    while ciclo_telefono:
        try:
            telefono = int(input("Ingresa el número telefónico: "))
            ciclo_telefono = False
        except ValueError:
            print("Debes ingresar un número de teléfono válido.")

    nuevo_contacto = Contacto(nombre, telefono)
    registro.append(nuevo_contacto)
    
    # ¡Llamamos a guardar_datos inmediatamente después de agregar!
    guardar_datos(registro)
    print("Registro exitoso y guardado correctamente.")

def listar(registro):
    if len(registro) == 0:
        print("No hay personal registrado.")
    else:
        for persona in registro:
            print(persona.mostrar_info())

# --- BLOQUE PRINCIPAL ---

print("Directorio de personal (Versión POO + JSON)")

# Al iniciar el programa, la lista ya no está vacía, se llena con lo que haya en el archivo
directorio = cargar_datos()
activo = True

while activo:
    print("\nOpciones de directorio:")
    print("1) Agregar nuevo personal.")
    print("2) Ver directorio.")
    print("3) Salir.")

    try:
        valor_menu = int(input("Ingresa el número de la opción: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")
        continue

    if valor_menu == 1:
        agregar(directorio)
    elif valor_menu == 2:
        listar(directorio)
    elif valor_menu == 3:
        print("Gracias por usar el sistema... Hasta pronto")
        activo = False
    else:
        print("Opción no válida. Intenta de nuevo.")