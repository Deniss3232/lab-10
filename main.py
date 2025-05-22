from grafo import Grafo

def main():
    g = Grafo()
    g.cargar_desde_archivo('logistica.txt')

    while True:
        print("\n--- Menú ---")
        print("1. Buscar ruta más corta entre dos ciudades")
        print("2. Mostrar ciudad centro del grafo")
        print("3. Modificar grafo (eliminar, agregar, cambiar clima)")
        print("4. Salir")
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
            print("\na) Eliminar conexión\nb) Agregar conexión\nc) Cambiar clima")
            sub = input("Seleccione una subopción: ").strip().lower()

            if sub == 'a':
                origen = input("Ciudad origen a eliminar: ").strip()
                destino = input("Ciudad destino a eliminar: ").strip()
                g.eliminar_conexion(origen, destino)
                print("Conexión eliminada.")

            elif sub == 'b':
                origen = input("Ciudad origen: ").strip()
                destino = input("Ciudad destino: ").strip()
                t1 = int(input("Tiempo normal: "))
                t2 = int(input("Tiempo con lluvia: "))
                t3 = int(input("Tiempo con nieve: "))
                t4 = int(input("Tiempo con tormenta: "))
                g.agregar_conexion(origen, destino, [t1, t2, t3, t4])
                print("Conexión agregada.")

            elif sub == 'c':
                print("0: Normal, 1: Lluvia, 2: Nieve, 3: Tormenta")
                clima = int(input("Seleccione nuevo clima: "))
                g.cambiar_clima(clima)
                print("Clima actualizado.")

        elif opcion == '4':
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
