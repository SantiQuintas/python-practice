def suma(lista):
    total=0
    for i in range(len(lista)):
        total+=lista[i]


    return total

def prom(lista):
   return suma(lista)/len(lista)

def maxi(lista):
    maximo = lista[0]
    for i in range(1, len(lista)):
        if lista[i]> maximo:
            maximo = lista[i]


    return maximo

def mini(lista):
    minimo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]


    return minimo

def pares(lista):
    cant=0
    for i in range(0, len(lista)):
        if lista[i]%2 == 0:
            cant+=1


    return cant
def inpares(lista):
    cant=0
    for i in range(0, len(lista)):
        if lista[i]%2 != 0:
            cant+=1


    return cant


numeros = []
num = int(input("Ingrese un numero: \n"))

while num != 0 :
    numeros.append(num)
    num = int(input("Ingrese un numero: \n"))

if numeros :
    print(f"Cantidad de numeros: {len(numeros)}")
    print(f"Suma de los numeros: {suma(numeros)}")
    print(f"Promedio de los numeros: {prom(numeros)}")
    print(f"Numero Maximo: {maxi(numeros)}")
    print(f"Numero Minimo: {mini(numeros)}")
    print(f"Numeros Pares: {pares(numeros)}")
    print(f"Numeros Inpares: {inpares(numeros)}")
else:
    print("No ingreso ningun numero, no hay lista para mostrar")