# tests.py

from calculadora import somar, subtrair, multiplicar, dividir

def test_calculadora():
    assert somar(2, 3) == 5
    assert subtrair(5, 3) == 2
    assert multiplicar(2, 3) == 6
    assert dividir(6, 3) == 2
    assert dividir(6, 0) == 'Erro: Divisão por 0'

if __name__ == "__main__":
    test_calculadora()
    print("Todos os testes passaram!")
