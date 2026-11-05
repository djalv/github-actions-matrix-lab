"""Operações matemáticas simples com validação de entradas."""


def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def potencia(base: float, expoente: int) -> float:
    if not isinstance(expoente, int) or isinstance(expoente, bool):
        raise TypeError("O expoente deve ser um número inteiro.")
    return base ** expoente
