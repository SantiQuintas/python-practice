class Cola:
    def __init__(self):
        self.lista=[]
    def encolar(self, item):
        self.lista.append(item)
    def desencolar(self):
        try:
            return self.lista.pop(0)
        except IndexError:
            raise Exception("COLA VACIA")
    def ver_Frente(self):
        try:
            return self.lista[0]
        except IndexError:
            raise Exception("COLA VACIA")
    def esta_vacia(self):
        return len(self.lista) == 0
    
    def tamanho(self):
        return len(self.lista)
        


nombres = ["me", "entro", "la", "balubi", "badre"]
cola = Cola()
for nombre in nombres:
    cola.encolar(nombre)

#Atender
while not cola.esta_vacia():
    print(f"Atendiendo a: {cola.desencolar()}")
    
try:
    cola.desencolar()
except Exception as e:
        print(e)