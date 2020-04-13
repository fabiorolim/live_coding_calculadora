from abc import ABC, abstractmethod


class OperacaoInvalida(Exception):
    pass


class Operacao(ABC):

    @abstractmethod
    def __call__(self, *numeros):
        pass


class Soma(Operacao):

    def __call__(self, *numeros):
        return numeros[0] + numeros[1]


class Subtracao(Operacao):

    def __call__(self, *numeros):
        return numeros[0] - numeros[1]


class Multiplicacao(Operacao):

    def __call__(self, *numeros):
        return numeros[0] * numeros[1]


class Divisao(Operacao):

    def __call__(self, *numeros):
        return numeros[0] / numeros[1]


class CalculadoraOO:
    """
    Para criar sua calculadora herde de calculadora. Para criar suas operações
    herde de operações e implemente o método __call__
    """

    def __init__(self):
        self._numeros = []
        self._operacoes = {}
        self.adicionar_operacao('+', Soma())
        self.adicionar_operacao('-', Subtracao())
        self.adicionar_operacao('*', Multiplicacao())
        self.adicionar_operacao('/', Divisao())

    @property
    def numeros(self):
        return self._numeros

    @numeros.setter
    def numeros(self, numeros):
        self._numeros = numeros

    @property
    def sinal(self):
        return self._sinal

    @sinal.setter
    def sinal(self, sinal):
        self._sinal = sinal

    def calcular(self):
        try:
            operacao = self._operacoes[self.sinal]
            resultado = operacao(self._numeros[0], self._numeros[1])
        except KeyError:
            raise OperacaoInvalida('Operação inválida')
        return resultado

    def adicionar_operacao(self, sinal, operacao):
        self._operacoes[sinal] = operacao

    def extrair_input(self):
        self.numeros.append(int(input('Número  1: ')))
        self._sinal = input('Informe a operação: ')
        self.numeros.append(int(input('Número  2: ')))
