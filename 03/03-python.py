def buscar(clave, contactos):
    encontrado= None
    for contacto in contactos:
        if contacto["nombre"] == clave:
            encontrado=contacto
            
    return encontrado
def prom(contactos):
    total=0
    for contacto in contactos:
        total+= contacto["edad"]
            
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
        if maximo["edad"] < contacto["edad"]:
            maximo=contacto
    return maximo["nombre"]

def mas_chico(contactos):
    minimo = contactos[0]
    for contacto in contactos:
        if minimo["edad"] > contacto["edad"]:
            minimo=contacto
    return minimo["nombre"]

contactos = [
]

mostrar_menu()
opcion = int(input("Ingrese una opcion: \n"))
while opcion != 6:
        if opcion == 1:
            contacto = {
            "nombre" : "",
            "telefono": "",
            "edad": None
            }
            print("Para ingresar un contacto, ingrese: ")
            contacto["nombre"]=input("Ingrese nombre del contacto: \n")
            contacto["telefono"]=input("Ingrese telefono del contacto: \n")
            contacto["edad"]=int(input("Ingrese edad del contacto: \n"))
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
                for clave, valor in cont.items():
                    print(clave, ":", valor)
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
        elif opcion == 6 : 
            print("Saliendo del programa..")
        else:
            print("Opcion incorrecta, reingresar")
            
            
        mostrar_menu()        
        opcion = int(input("Ingrese una opcion: \n"))
    