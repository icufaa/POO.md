import csv
import time

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol: 
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self.__agregar_recursivo(self.raiz, dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def inorden(self, nodo,nivel=0,prefijo ="Raiz: "):
        if nodo is not None:
            self.inorden(nodo.izquierda,nivel + 1, "\t\tIzq---: ")
            print(" " * (nivel*4)+ prefijo + str(nodo.dato))
            self.inorden(nodo.derecha,nivel + 1, "\t\tDer---: ")

    def preorden(self, nodo,nivel=0,prefijo ="Raiz: "):
        if nodo is not None:
            print(" " * (nivel*4)+ prefijo + str(nodo.dato))
            self.preorden(nodo.izquierda,nivel + 1, "\t\tIzq---: ")
            self.preorden(nodo.derecha,nivel + 1, "\t\tDer---: ")

    def postorden(self, nodo,nivel=0,prefijo ="Raiz: "):
        if nodo is not None:
            self.postorden(nodo.izquierda,nivel + 1, "\t\tIzq---: ")
            self.postorden(nodo.derecha,nivel + 1, "\t\tDer---: ")
            print(" " * (nivel*4)+ prefijo + str(nodo.dato))

    def buscar_dfs (self,dato):
        return self.__buscar_dfs_recursivo(self.raiz,dato)
    
    def __buscar_dfs_recursivo(self,nodo,dato):
        if nodo is None:
            return None
        if nodo.dato == dato:
            return nodo
        print(f"Buscando en nodo: {nodo.dato}")
        resultado_izquierda = self.__buscar_dfs_recursivo(nodo.izquierda ,dato)
        if resultado_izquierda is not None:
            return resultado_izquierda
        return self.__buscar_dfs_recursivo(nodo.derecha , dato)
    
    def buscar_bfs(self,dato):
        if self.raiz is None:
            return None
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            print(f'Buscando en nodo: {nodo.dato}')
            if nodo.dato == dato:
                return nodo
            if nodo.izquierda is not None:
                cola.append(nodo.izquierda)
            if nodo.derecha is not None:
                cola.append(nodo.derecha)
        return None


arbol = Arbol()


with open('MOCK_DATA.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)
    for fila in lector_csv:
        
        apellido = fila[1]
        arbol.agregar(apellido)


def salir():
    print("Saliendo del programa.")
    exit()


def menu():
    while True:
        print("1. Imprimir Recorrido Inorden")
        print("2. Imprimir Recorrido Preorden")
        print("3. Imprimir Recorrido Postorden")
        print("4. Buscar Persona por (DFS)")
        print("5. Buscar Persona por (BFS)")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("Recorrido Inorden:")
            inicio= time.time()
            arbol.inorden(arbol.raiz)
            fin = time.time()
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar el recorrido: {tiempo_total:.5f} segundos")
        elif opcion == "2":
            print("\nRecorrido Preorden:")
            inicio= time.time()
            arbol.preorden(arbol.raiz)
            fin = time.time()
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar el recorrido: {tiempo_total:.5f} segundos")
        elif opcion == "3":
            print("\nRecorrido Postorden:")
            inicio= time.time()
            arbol.postorden(arbol.raiz)
            fin = time.time()
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar el recorrido: {tiempo_total:.5f} segundos")
        elif opcion == "4":
            dato = input("Ingresa el apellido a buscar por (DFS): ")
            inicio = time.time()
            resultado = arbol.buscar_dfs(dato.capitalize())
            fin = time.time()
            if resultado:
                print(f"Persona encontrada: {resultado.dato}")
            else:
                print("Persona no encontrada")
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar la busqueda: {tiempo_total:.5f} segundos")
        elif opcion == "5":
            dato = input("Ingrese el apellido a buscar (BFS): ")
            inicio = time.time()
            resultado = arbol.buscar_bfs(dato.capitalize())
            fin = time.time()
            if resultado:
                print(f"Persona encontrada: {resultado.dato}")
            else:
                print("Persona no encontrada")
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar la búsqueda: {tiempo_total:.5f} segundos")
        elif opcion == "6":
            salir()
        else:
            print("Opción inválida. Inténtalo de nuevo.")

menu()
