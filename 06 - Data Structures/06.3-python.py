class Nodo:
    def __init__(self):
        self.dato=None
        self.siguiente=None
    def __str__(self):
        return f"dato: {self.dato} siguiente: {self.siguiente}"

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar_al_final(self, dato):
        nodo = Nodo()
        nodo.dato=dato
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            actual=self.cabeza
            while actual.siguiente is not None:
                actual=actual.siguiente
            actual.siguiente=nodo
    def imprimir(self):
        imprimir = self.cabeza
        while imprimir is not None:
            print(imprimir.dato)
            imprimir = imprimir.siguiente
    def buscar(self, dato):
        buscar = self.cabeza
        while buscar is not None:
            if buscar.dato == dato:
                return True
            buscar = buscar.siguiente
        return False
    def eliminar(self, dato):
            anterior = None
            actual=self.cabeza
            while actual is not None:
                if actual.dato==dato:
                    if anterior is None:
                        self.cabeza=actual.siguiente
                    else: 
                        anterior.siguiente = actual.siguiente
                    return True
                anterior = actual
                actual = actual.siguiente
            return False


    