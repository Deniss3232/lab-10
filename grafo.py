import sys

# Constante para representar infinito
INF = float('inf')

class Grafo:
    def __init__(self):
        self.ciudades = []
        self.indices = {}
        self.adj_matrix = []

    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as file:
            conexiones = file.readlines()
        conexiones = [line.strip().split() for line in conexiones]

        # Construir lista de ciudades únicas
        for origen, destino, *_ in conexiones:
            if origen not in self.ciudades:
                self.ciudades.append(origen)
            if destino not in self.ciudades:
                self.ciudades.append(destino)

        self.ciudades.sort()
        self.indices = {ciudad: i for i, ciudad in enumerate(self.ciudades)}

        n = len(self.ciudades)
        self.adj_matrix = [[INF] * n for _ in range(n)]
        for i in range(n):
            self.adj_matrix[i][i] = 0

        for origen, destino, tiempoNormal, *_ in conexiones:
            i = self.indices[origen]
            j = self.indices[destino]
            self.adj_matrix[i][j] = int(tiempoNormal)

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
        excentricidades = []

        for i in range(len(self.ciudades)):
            ecc = max(dist[i][j] for j in range(len(self.ciudades)))
            excentricidades.append((ecc, i))

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
