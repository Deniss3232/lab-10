import unittest
from grafo import Grafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.g = Grafo()
        self.g.cargar_desde_archivo("logistica.txt")

    def test_ruta_mas_corta(self):
        ruta, costo = self.g.obtener_ruta("BuenosAires", "Quito")
        self.assertEqual(ruta, ["BuenosAires", "SaoPaulo", "Quito"])
        self.assertEqual(costo, 15)

    def test_centro(self):
        centro = self.g.encontrar_centro()
        self.assertEqual(centro, "Quito")  # Según el grafo de ejemplo

    def test_ciudades(self):
        self.assertIn("Lima", self.g.ciudades)
        self.assertIn("Caracas", self.g.ciudades)

if __name__ == '__main__':
    unittest.main()
