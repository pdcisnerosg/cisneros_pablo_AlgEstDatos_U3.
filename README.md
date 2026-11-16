# Red de ciudades

Programa de consola en Python que modela una red de ciudades con carreteras como un grafo ponderado y calcula recorridos y rutas mínimas con las estructuras de la Unidad 3.

Autor: Pablo Cisneros. Materia: Algoritmos y Estructuras de Datos (Ciencia de Datos).

## Cómo ejecutar

Requiere Python 3 y no usa librerías externas (solo `heapq` y `collections`, que vienen con Python).

```
python main.py
```

En Mac o Linux, si `python` no funciona, usa `python3 main.py`. La red de ejemplo ya viene cargada, así que se puede probar de inmediato.

## Archivos

| Archivo | Contenido |
|---|---|
| `main.py` | Red de ejemplo y menú de consola |
| `utilidades.py` | Funciones de los cuatro requerimientos |

## Red de ejemplo

Tiene 9 ciudades. Las carreteras van en los dos sentidos y el peso de cada una son los kilómetros.

| Ciudad | Carreteras |
|---|---|
| Quito | Ambato 130, Guayaquil 420 |
| Ambato | Quito 130, Riobamba 55 |
| Riobamba | Ambato 55, Cuenca 215 |
| Guayaquil | Quito 420, Cuenca 200, Machala 180 |
| Cuenca | Riobamba 215, Guayaquil 200, Machala 190, Loja 210, Macas 200 |
| Machala | Guayaquil 180, Cuenca 190, Loja 190 |
| Loja | Cuenca 210, Machala 190 |
| Macas | Cuenca 200 |
| Puerto Ayora | sin carreteras |

Puerto Ayora (Galápagos) no tiene carreteras hacia el continente, y con eso se comprueba cómo el programa detecta una ciudad aislada. Si se quita esa línea de `main.py`, la red queda completamente conectada. Las distancias son aproximadas.

## Requerimientos

**R1 – Lista de adyacencia (opción 1).** El grafo es un diccionario `{ciudad: [(ciudad_vecina, km), ...]}`. La opción 1 muestra las carreteras de cada ciudad y su grado, que es la cantidad de vecinos.

**R2 – Recorrido BFS (opción 2).** Pide una ciudad de origen y recorre la red por niveles con una cola. Muestra cada ciudad alcanzable con su número de escalas. Si alguna ciudad no se alcanza, avisa que la red no está completamente conectada y la nombra; si se alcanzan todas, avisa que está conectada.

**R3 – Distancias mínimas (opción 3).** Usa la función `dijkstra` entregada en el enunciado, sin cambios. Muestra los kilómetros mínimos desde el origen hasta cada ciudad (o "sin ruta" si no se llega) e indica la ciudad más cercana y la más lejana.

**R4 – Menos escalas contra menos kilómetros (opción 4).** Pide origen y destino y muestra dos rutas: la de menos escalas (BFS) y la de menos kilómetros (Dijkstra). La red está armada para que no coincidan. Con Quito y Cuenca, la ruta de menos escalas es Quito -> Guayaquil -> Cuenca (2 escalas, 620 km) y la de menos kilómetros es Quito -> Ambato -> Riobamba -> Cuenca (3 escalas, 400 km). BFS cuenta carreteras sin importar su longitud, y Dijkstra suma kilómetros sin importar cuántas carreteras use.

## Complejidades

V es el número de ciudades y E el número de carreteras.

| Función | Complejidad | Justificación |
|---|---|---|
| `grados` | O(V) | Cuenta los vecinos de cada ciudad una sola vez. |
| `bfs` | O(V + E) | Cada ciudad entra una vez a la cola y cada carretera se revisa una vez. |
| `dijkstra` | O((V + E) log V) | Cada inserción o extracción del heap cuesta O(log V). |
| `comparar` | O((V + E) log V) | Corre un BFS y un Dijkstra; domina Dijkstra. |
