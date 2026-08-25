def palabra_mas_larga(lista):
    maxima = lista[0]
    for i in range(1, len(lista)):
        if len(maxima) < len(lista[i]):
            maxima=lista[i]
        
    return maxima

def palabra_mas_corta(lista):
    minima = lista[0]
    for i in range(1, len(lista)):
        if len(minima) > len(lista[i]):
            minima=lista[i]
        
    return minima

def palabra_5_carac(lista):
    total = 0
    for palabra in lista:
        if len(palabra) > 5:
            total+=1
        
    return total

def palabra_empieza_vocal(lista):
    total = 0
    for palabra in lista:
        if palabra[0] in "aeiou" :
            total+=1
        
    return total

def palabra_con_a(lista):
    total = 0
    for palabra in lista:
        if "a" in palabra:
            total+=1
        
    return total



palabras = []
palabra = input("Ingrese una palabra: ").lower()
while palabra != "fin":
    palabras.append(palabra)
    palabra = input("Ingrese una palabra: ").lower()
    
if palabras:
    print(f"Cantidad de palabras: {len(palabras)}")
    print(f"Palabra mas larga: {palabra_mas_larga(palabras)}")
    print(f"Palabra mas corta: {palabra_mas_corta(palabras)}")
    print(f"Palabras con mas de 5 caracteres: {palabra_5_carac(palabras)}")
    print(f"Palabras que empiezan con vocal: {palabra_empieza_vocal(palabras)}")
    print(f"Palabras que contienen 'a': {palabra_con_a(palabras)}")
else:
    print("No hay una lista de palabras")