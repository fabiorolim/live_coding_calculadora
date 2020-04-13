from unittest import TestCase

from calculadora import calcular
from calculadora_oo import CalculadoraOO, OperacaoInvalida


class TestCalculadora(TestCase):

    def test_soma_2_2(self):
        self.assertEqual(calcular(2, '+', 2), 4)

    def test_sub_10_5(self):
        self.assertEqual(calcular(10, '-', 5), 5)

    def test_mul_4_10(self):
        self.assertEqual(calcular(4, '*', 10), 40)

    def test_div_10_2(self):
        self.assertEqual(calcular(10, '/', 2), 5)

    def test_pow_10_2(self):
        self.assertEqual(calcular(10, '**', 2), 100)

    def test_op_invalida(self):
        self.assertEqual(calcular(10, 'u', 2), 'Operação inválida')


class TestCalculadoraOO(TestCase):

    def setUp(self):
        self.calculadora = CalculadoraOO()

    def test_soma_2_2(self):
        self.calculadora.numeros = [2, 2]
        self.calculadora.sinal = '+'
        self.assertEqual(self.calculadora.calcular(), 4)

    def test_sub_1_1(self):
        self.calculadora.numeros = [1, 1]
        self.calculadora.sinal = '-'
        self.assertEqual(self.calculadora.calcular(), 0)

    def test_mulitplicar_10_5(self):
        self.calculadora.numeros = [10, 5]
        self.calculadora.sinal = '*'
        self.assertEqual(self.calculadora.calcular(), 50)

    def test_div_45_9(self):
        self.calculadora.numeros = [45, 9]
        self.calculadora.sinal = '/'
        self.assertEqual(self.calculadora.calcular(), 5)

    def test_operacao_invalida(self):
        self.calculadora.numeros = [3, 4]
        self.calculadora.sinal = '&'
        self.assertRaises(OperacaoInvalida)
