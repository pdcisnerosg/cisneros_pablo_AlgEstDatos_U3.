import heapq
from collections import deque

# R1 - Grado de cada ciudad
# grados: O(V)
def grados(grafo):
    return {ciudad: len(vecinos) for ciudad, vecinos in grafo.items()}

# R2 - Recorrido BFS
# BFS: O(V + E)
def bfs(grafo, origen):
    escalas = {origen: 0}
    padre = {origen: None}
    cola = deque([origen])
    while cola:
        ciudad = cola.popleft()
        for vecino, _ in grafo[ciudad]:
            if vecino not in escalas:
                escalas[vecino] = escalas[ciudad] + 1
                padre[vecino] = ciudad
                cola.append(vecino)
    return escalas, padre

def ruta_bfs(padre, destino):
    ruta = []
    ciudad = destino
    while ciudad is not None:
        ruta.insert(0, ciudad)
        ciudad = padre[ciudad]
    return ruta

# R3 - Ruta más barata (Dijkstra entregado en el enunciado)
# Dijkstra: O((V + E) log V)
def dijkstra(grafo, origen):
    """Devuelve {ciudad: distancia_minima_desde_origen}."""
    dist = {ciudad: float('inf') for ciudad in grafo}
    dist[origen] = 0
    heap = [(0, origen)]          # cola de prioridad
    while heap:
        d, u = heapq.heappop(heap)      # el mas cercano pendiente
        if d > dist[u]:
            continue                    # ya teniamos una ruta mejor
        for vecino, peso in grafo[u]:
            if dist[u] + peso < dist[vecino]:    # relajacion
                dist[vecino] = dist[u] + peso
                heapq.heappush(heap, (dist[vecino], vecino))
    return dist

def cercana_lejana(dist, origen):
    otras = {c: d for c, d in dist.items() if c != origen and d != float('inf')}
    if not otras:
        return None, None
    return min(otras, key=otras.get), max(otras, key=otras.get)

# R4 - Comparación de rutas
# Dijkstra solo devuelve distancias, así que la ruta se arma hacia atrás con ellas
def ruta_minima(grafo, dist, origen, destino):
    ruta = [destino]
    ciudad = destino
    while ciudad != origen:
        for vecino, km in grafo[ciudad]:
            if dist[vecino] + km == dist[ciudad]:
                ciudad = vecino
                break
        ruta.insert(0, ciudad)
    return ruta

def km_ruta(grafo, ruta):
    total = 0
    for a, b in zip(ruta, ruta[1:]):
        for vecino, km in grafo[a]:
            if vecino == b:
                total += km
    return total

# comparar: O((V + E) log V)
def comparar(grafo, origen, destino):
    escalas, padre = bfs(grafo, origen)
    if destino not in escalas:
        return None
    ruta_escalas = ruta_bfs(padre, destino)
    dist = dijkstra(grafo, origen)
    ruta_km = ruta_minima(grafo, dist, origen, destino)
    return ruta_escalas, km_ruta(grafo, ruta_escalas), ruta_km, dist[destino]
