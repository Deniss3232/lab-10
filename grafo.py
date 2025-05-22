import sys

INF = float('inf')

class Grafo:
    def __init__(self):
        self.ciudades = []
        self.indices = {}
        self.tiempos = {}  # (origen, destino) -> [normal, lluvia, nieve, tormenta]
        self.clima = 0  # 0 = normal, 1 = lluvia, 2 = nieve, 3 = tormenta
        self.adj_matrix = []

    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as file:
            conexiones = file.readlines()
        conexiones = [line.strip().split() for line in conexiones]

        for origen, destino, *_ in conexiones:
            if origen not in self.ciudades:
                self.ciudades.append(origen)
            if destino not in self.ciudades:
                self.ciudades.append(destino)

        self.ciudades.sort()
        self.indices = {ciudad: i for i, ciudad in enumerate(self.ciudades)}

        for origen, destino, n, l, ni, t in conexiones:
            self.tiempos[(origen, destino)] = [int(n), int(l), int(ni), int(t)]

        self.actualizar_matriz()

    def actualizar_matriz(self):
        n = len(self.ciudades)
        self.adj_matrix = [[INF]*n for _ in range(n)]
        for i in range(n):
            self.adj_matrix[i][i] = 0
        for (origen, destino), tiempos in self.tiempos.items():
            i = self.indices[origen]
            j = self.indices[destino]
            self.adj_matrix[i][j] = tiempos[self.clima]

    def floyd_warshall(self):
        n = len(self.adj_matrix)
        dist = [row[:] for row in self.adj_matrix]
        next_hop = [[None if dist[i][j] == INF else j for j in range(n)] for i in range(n)]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_hop[i][j] = next_hop[i][k]

        return dist, next_hop

    def encontrar_centro(self):
        dist, _ = self.floyd_warshall()
        excentricidades = [(max(row), i) for i, row in enumerate(dist)]
        centro = min(excentricidades)
        return self.ciudades[centro[1]]

    def obtener_ruta(self, origen, destino):
        dist, next_hop = self.floyd_warshall()
        i, j = self.indices[origen], self.indices[destino]
        if dist[i][j] == INF:
            return None, INF
        ruta = [origen]
        while i != j:
            i = next_hop[i][j]
            ruta.append(self.ciudades[i])
        return ruta, dist[self.indices[origen]][self.indices[destino]]

    def eliminar_conexion(self, origen, destino):
        if (origen, destino) in self.tiempos:
            del self.tiempos[(origen, destino)]
            self.actualizar_matriz()

    def agregar_conexion(self, origen, destino, tiempos):
        if origen not in self.ciudades:
            self.ciudades.append(origen)
        if destino not in self.ciudades:
            self.ciudades.append(destino)
        self.ciudades.sort()
        self.indices = {ciudad: i for i, ciudad in enumerate(self.ciudades)}
        self.tiempos[(origen, destino)] = tiempos
        self.actualizar_matriz()

    def cambiar_clima(self, nuevo_clima):
        self.clima = nuevo_clima
        self.actualizar_matriz()
