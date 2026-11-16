from utilidades import grados, bfs, dijkstra, cercana_lejana, comparar

red = {
    "Quito": [("Ambato", 130), ("Guayaquil", 420)],
    "Ambato": [("Quito", 130), ("Riobamba", 55)],
    "Riobamba": [("Ambato", 55), ("Cuenca", 215)],
    "Guayaquil": [("Quito", 420), ("Cuenca", 200), ("Machala", 180)],
    "Cuenca": [("Riobamba", 215), ("Guayaquil", 200), ("Machala", 190), ("Loja", 210), ("Macas", 200)],
    "Machala": [("Guayaquil", 180), ("Cuenca", 190), ("Loja", 190)],
    "Loja": [("Cuenca", 210), ("Machala", 190)],
    "Macas": [("Cuenca", 200)],
    "Puerto Ayora": [],
}

def pedir_ciudad(texto):
    ciudad = input(texto).strip().title()
    if ciudad not in red:
        print("La ciudad no existe en la red")
        return None
    return ciudad

def ver_red():
    for ciudad, grado in grados(red).items():
        carreteras = ", ".join(f"{vecino} {km} km" for vecino, km in red[ciudad])
        print(f"{ciudad} (grado {grado}): {carreteras or 'sin carreteras'}")

def recorrido():
    origen = pedir_ciudad("Ciudad de origen: ")
    if origen is None:
        return
    escalas, _ = bfs(red, origen)
    for ciudad, n in escalas.items():
        print(f"{ciudad}: {n} {'escala' if n == 1 else 'escalas'}")
    sin_ruta = [ciudad for ciudad in red if ciudad not in escalas]
    if sin_ruta:
        print(f"La red no está completamente conectada. Sin ruta desde {origen}: {', '.join(sin_ruta)}")
    else:
        print("La red está completamente conectada")

def rutas_minimas():
    origen = pedir_ciudad("Ciudad de origen: ")
    if origen is None:
        return
    dist = dijkstra(red, origen)
    for ciudad, km in sorted(dist.items(), key=lambda par: par[1]):
        if km == float("inf"):
            print(f"{ciudad}: sin ruta")
        else:
            print(f"{ciudad}: {km} km")
    cercana, lejana = cercana_lejana(dist, origen)
    if cercana:
        print(f"Más cercana: {cercana} ({dist[cercana]} km)")
        print(f"Más lejana: {lejana} ({dist[lejana]} km)")

def comparar_rutas():
    origen = pedir_ciudad("Ciudad de origen: ")
    if origen is None:
        return
    destino = pedir_ciudad("Ciudad de destino: ")
    if destino is None:
        return
    if origen == destino:
        print("Elige dos ciudades distintas")
        return
    resultado = comparar(red, origen, destino)
    if resultado is None:
        print("No hay ruta entre esas ciudades")
        return
    ruta_escalas, km_escalas, ruta_km, km_minimos = resultado
    print(f"Menos escalas: {' -> '.join(ruta_escalas)} ({len(ruta_escalas) - 1} escalas, {km_escalas} km)")
    print(f"Menos kilómetros: {' -> '.join(ruta_km)} ({len(ruta_km) - 1} escalas, {km_minimos} km)")
    if ruta_escalas == ruta_km:
        print("Las dos rutas coinciden")
    else:
        print("Las rutas no coinciden")

def main():
    try:
        while True:
            print("\nRed de ciudades")
            print("1. Ver la red y el grado de cada ciudad")
            print("2. Recorrido BFS desde una ciudad")
            print("3. Distancias mínimas con Dijkstra")
            print("4. Comparar menos escalas y menos kilómetros")
            print("0. Salir")
            opcion = input("Opción: ").strip()
            if opcion == "1":
                ver_red()
            elif opcion == "2":
                recorrido()
            elif opcion == "3":
                rutas_minimas()
            elif opcion == "4":
                comparar_rutas()
            elif opcion == "0":
                print("Hasta luego")
                break
            else:
                print("Opción no válida")
    except (EOFError, KeyboardInterrupt):
        print("\nHasta luego")

if __name__ == "__main__":
    main()
