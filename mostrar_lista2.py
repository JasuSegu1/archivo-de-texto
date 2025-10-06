import os
os.system("cls")
#cambio1 de lista
class ListaFrutas:
    def __init__(self):
        self.frutas = []
    
    def pedir_frutas(self):
        otra_fruta = 's'
        while otra_fruta.lower() == 's':
            fruta = input("Ingresa una fruta: ")
            self.frutas.append(fruta)
            otra_fruta = input("¿Otra fruta? (s/n): ")
    
    def mostrar_lista(self):
        print("\n" + "="*40)
        print("       LISTA DE FRUTAS INGRESADAS")
        print("="*40)
        
        if not self.frutas:
            print("No hay frutas en la lista ")
            return
        
        for i, fruta in enumerate(self.frutas, 1):
            print(f"{i}. {fruta}")
        
        print(f"\nTotal de frutas: {len(self.frutas)}")
        print("="*40)
    
    def guardar_archivo(self):
        with open("frutas.txt", "w", encoding="utf-8") as archivo:
            for fruta in self.frutas:
                archivo.write(fruta + "\n")
        print("\nArchivo 'frutas.txt' creado con éxito 🍇")
    

lista = ListaFrutas()
lista.pedir_frutas()
lista.mostrar_lista() 
lista.guardar_archivo()