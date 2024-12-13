import unittest
from numeroromano import converte

class TestConverteNumerosRomanos(unittest.TestCase):

    def test_numeros_simples(self):
        self.assertEqual(converte("I"), 1)
        self.assertEqual(converte("V"), 5)
        self.assertEqual(converte("X"), 10)
        self.assertEqual(converte("L"), 50)
        self.assertEqual(converte("C"), 100)
        self.assertEqual(converte("D"), 500)
        self.assertEqual(converte("M"), 1000)

    def test_combinacoes_validas(self):
        self.assertEqual(converte("II"), 2)
        self.assertEqual(converte("IV"), 4)
        self.assertEqual(converte("IX"), 9)
        self.assertEqual(converte("XL"), 40)
        self.assertEqual(converte("XC"), 90)
        self.assertEqual(converte("CD"), 400)
        self.assertEqual(converte("CM"), 900)
        self.assertEqual(converte("XXII"), 22)
        self.assertEqual(converte("XXIV"), 24)
        self.assertEqual(converte("MCMXCIV"), 1994)

    def test_numeros_maiores(self):
        self.assertEqual(converte("MMXXIV"), 2024)
        self.assertEqual(converte("MMMCMXCIX"), 3999)

    def test_entradas_invalidas(self):
        with self.assertRaises(ValueError):
            converte("")
        with self.assertRaises(ValueError):
            converte("IIII")
        with self.assertRaises(ValueError):
            converte("VV")
        with self.assertRaises(ValueError):
            converte("MMMM")
        with self.assertRaises(ValueError):
            converte("ABC")
        with self.assertRaises(ValueError):
            converte("123")

if __name__ == "__main__":
    unittest.main()
