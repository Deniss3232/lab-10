from grafo import Grafo

def main():
    g = Grafo()
    g.cargar_desde_archivo('logistica.txt')

    while True:
        print("\n--- Menú ---")
        print("1. Buscar ruta más corta entre dos ciudades")
        print("2. Mostrar ciudad centro del grafo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            origen = input("Ciudad origen: ").strip()
            destino = input("Ciudad destino: ").strip()
            if origen not in g.ciudades or destino not in g.ciudades:
                print("Ciudad no encontrada.")
                continue
            ruta, costo = g.obtener_ruta(origen, destino)
            if ruta:
                print(f"Ruta más corta: {' -> '.join(ruta)}")
                print(f"Tiempo total: {costo} horas")
            else:
                print("No hay camino entre esas ciudades.")
        elif opcion == '2':
            print(f"El centro del grafo es: {g.encontrar_centro()}")
        elif opcion == '3':
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
