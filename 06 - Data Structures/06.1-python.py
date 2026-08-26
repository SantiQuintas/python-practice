
class Pila:
    def __init__(self):
        self.items =[]
        
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        try:
            return self.items.pop(-1)
        except IndexError:
            raise Exception("Pila Vacia")
        
    def ver_tope(self):
        try:
            return self.items[-1]
        except IndexError:
            raise Exception("Pila Vacia")
    def esta_vacia(self):
        if self.items:
            return False
        else:
            return True
    def tamano(self):
        return len(self.items)
        
        
def parentesis_balanceado(cadena):
    apertura = Pila()
    for letra in cadena:
        if letra == "(":
            apertura.apilar(letra)
        elif letra == ")":
            try:
                apertura.desapilar()
            except Exception:
                return False
            
    return apertura.esta_vacia()

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
class Pila:
    def __init__(self):
        self.items =[]
        
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        try:
            return self.items.pop(-1)
        except IndexError:
            raise Exception("Pila Vacia")
        
    def ver_tope(self):
        try:
            return self.items[-1]
        except IndexError:
            raise Exception("Pila Vacia")
    def esta_vacia(self):
        if self.items:
            return False
        else:
            return True
    def tamano(self):
        return len(self.items)
        
        
def parentesis_balanceado(cadena):
    apertura = Pila()
    for letra in cadena:
        if letra == "(":
            apertura.apilar(letra)
        elif letra == ")":
            try:
                apertura.desapilar()
            except Exception:
                return False
            
    return apertura.esta_vacia()

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