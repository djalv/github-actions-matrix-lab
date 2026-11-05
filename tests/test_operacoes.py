"""Testes unitários independentes de sistema operacional."""

import unittest

from calculadora import dividir, multiplicar, potencia, somar, subtrair


class TestOperacoes(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(somar(2, 3), 5)

    def test_soma_com_negativos(self):
        self.assertEqual(somar(-4, -6), -10)

    def test_subtracao(self):
        self.assertEqual(subtrair(10, 7), 3)

    def test_multiplicacao(self):
        self.assertEqual(multiplicar(-3, 4), -12)

    def test_divisao(self):
        self.assertEqual(dividir(9, 2), 4.5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_potencia(self):
        self.assertEqual(potencia(2, 4), 16)

    def test_potencia_com_expoente_negativo(self):
        self.assertEqual(potencia(2, -2), 0.25)

    def test_potencia_rejeita_expoente_fracionario(self):
        with self.assertRaises(TypeError):
            potencia(2, 1.5)


if __name__ == "__main__":
    unittest.main()
