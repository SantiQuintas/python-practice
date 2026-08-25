contactos = []
with open('file.txt', 'r', encoding="utf-8") as f:
    for linea in f:
        contacto={}
        texto = linea.strip()
        nuevo=(texto.split(','))
        contacto["nombre"]=nuevo[0]
        contacto["telefono"]=nuevo[1]
        contacto["edad"]=int(nuevo[2])
        contactos.append(contacto)
        

print(contactos)
