import os
os.system("cls")

class ListaFrutas:
    def __init__(self):
        self.frutas = []
    
    def pedir_frutas(self):
        otra_fruta = 's'
        while otra_fruta.lower() == 's':
            fruta = input("Ingresa una fruta: ")
            self.frutas.append(fruta)
            otra_fruta = input("¿Otra fruta? (s/n): ")
    
    def guardar_archivo(self):
        with open("frutas.txt", "w", encoding="utf-8") as archivo:
            for fruta in self.frutas:
                archivo.write(fruta + "\n")
        print("\nArchivo 'frutas.txt' creado con éxito 🍇")
    

lista = ListaFrutas()
lista.pedir_frutas()
lista.guardar_archivo()

print("\nFrutas ingresadas:")
for fruta in lista.frutas:
    print(fruta)
