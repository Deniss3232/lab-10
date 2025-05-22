import unittest
from grafo import Grafo
// pruebas unitarias 
// se corre el programa con este comando
//python -m unittest test_grafo.py
//en logistica.txt
class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.g = Grafo()
        self.g.cargar_desde_archivo("logistica.txt")

    def test_ciudades_existentes(self):
        self.assertIn("Lima", self.g.ciudades)
        self.assertIn("Quito", self.g.ciudades)

    def test_ruta_mas_corta(self):
        ruta, costo = self.g.obtener_ruta("BuenosAires", "Quito")
        self.assertEqual(ruta, ["BuenosAires", "SaoPaulo", "Quito"])
        self.assertEqual(costo, 15)

    def test_centro_del_grafo(self):
        centro = self.g.encontrar_centro()
        self.assertEqual(centro, "Quito")  # Depende del grafo de ejemplo

    def test_eliminar_conexion(self):
        self.g.eliminar_conexion("BuenosAires", "SaoPaulo")
        ruta, costo = self.g.obtener_ruta("BuenosAires", "Quito")
        self.assertNotEqual(ruta, ["BuenosAires", "SaoPaulo", "Quito"])

    def test_agregar_conexion(self):
        self.g.agregar_conexion("Caracas", "SaoPaulo", [9, 15, 20, 40])
        ruta, costo = self.g.obtener_ruta("Caracas", "SaoPaulo")
        self.assertEqual(ruta, ["Caracas", "SaoPaulo"])
        self.assertEqual(costo, 9)

    def test_cambio_de_clima(self):
        self.g.cambiar_clima(3)  # Tormenta
        ruta, costo = self.g.obtener_ruta("BuenosAires", "SaoPaulo")
        self.assertEqual(costo, 50)

if __name__ == '__main__':
    unittest.main()
