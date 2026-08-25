import json

class Contacto:
    def __init__(self,nombre,telefono,edad):
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, telefono: {self.telefono}, edad: {self.edad}"

def buscar(clave, contactos):
    encontrado = None
    for contacto in contactos:
        if contacto.nombre == clave:
            encontrado=contacto
            
    return encontrado
def prom(contactos):
    total=0
    for contacto in contactos:
        total+= contacto.edad
            
    return total/len(contactos)

def mostrar_menu():
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Mostrar estadísticas")
    print("6. Salir")
    return

def mas_grande(contactos):
    maximo = contactos[0]
    for contacto in contactos:
        if maximo.edad < contacto.edad:
            maximo=contacto
    return maximo.nombre

def mas_chico(contactos):
    minimo = contactos[0]
    for contacto in contactos:
        if minimo.edad > contacto.edad:
            minimo=contacto
    return minimo.nombre

def dict_a_contacto(d):
    return Contacto(**d)

def pedir_opcion():
    opcion = None
    while opcion is None:
        try:
            opcion = int(input("Ingrese una opcion: \n"))
        except ValueError:
            print("Ingrese un numero como opcion")
    return opcion

try :
    with open('contactos.json', 'r') as f:
        contactos = json.load(f,object_hook=dict_a_contacto)
    
except FileNotFoundError:
    print("No existe el archivo contactos.json")
    contactos = []
    
mostrar_menu()
opcion = pedir_opcion()
while opcion != 6:
    if opcion == 1:
        print("Para ingresar un contacto, ingrese: ")
        nombre=input("Ingrese nombre del contacto: \n")
        telefono=input("Ingrese telefono del contacto: \n")
        edad=int(input("Ingrese edad del contacto: \n"))
        contacto = Contacto(nombre, telefono, edad)
        contactos.append(contacto)
    elif opcion == 2: 
        clave= input("Para buscar un contacto, ingrese su nombre: \n")
        encontrado = buscar(clave, contactos)
        if encontrado is None:
            print("No se encontró el contacto.")
        else:
                print(encontrado)
            
    elif opcion == 3: 
        for indice, cont in enumerate(contactos, start=1):
            print(f"---Contacto {indice}---")
            print(cont)
    elif opcion == 4 :
        clave = input("Para eliminar un contacto, ingrese un nombre: \n")
        encontrado = buscar(clave,contactos)
        if encontrado is None:
            print("El contacto no esta en la agenda")
        else:
            contactos.remove(encontrado)
            print("El contacto se elimino la agenda")
            
    elif opcion == 5 : 
        if contactos:
            print(f"Cantidad de contactos: {len(contactos)}")
            print(f"Edad promedios: {prom(contactos)}")
            print(f"Persona mas grande: {mas_grande(contactos)}")
            print(f"Persona mas joven: {mas_chico(contactos)}")
        else:
            print("No hay contactos")
    else:
        print("Opcion incorrecta, reingresar")
            
            
    mostrar_menu()        
        
    opcion=pedir_opcion()
            
print("Saliendo del programa..")

with open("contactos.json", "w") as f:
    json.dump(contactos, f,default=lambda c: c.__dict__)


