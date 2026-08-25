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

        
        
        
cadena = "(()())"
cadena2 = "(()"
cadena3 = ")("

print(parentesis_balanceado(cadena))
print(parentesis_balanceado(cadena2))
print(parentesis_balanceado(cadena3))