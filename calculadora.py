# Construir uma calculadora básica com python utilizando TDD
# Test Driven Development
# Olhar sempre o traceback. Keep calm and read traceback.

def calcular(numero1, sinal, numero2):
    operacoes = {
        '+': numero1.__add__,
        '-': numero1.__sub__,
        '*': numero1.__mul__,
        '/': numero1.__truediv__,
        '**': numero1.__pow__,
    }
    operacao = operacoes.get(sinal)
    return operacao(numero2) if operacao else 'Operação inválida'
