# calculadora.py

def calcular(op, a, b):
    """Retorna o resultado da operação especificada.
    
    Args:
        op (str): A operação selecionada pelo usuário (1, 2, 3, 4).
        a (float): O primeiro número.
        b (float): O segundo número.

    Returns:
        float or str: O resultado da operação ou uma mensagem de erro.
    """
    
    
    # Dicionário para mapear operações para suas respectivas funções
    return {
        '1': a + b,           # Soma
        '2': a - b,           # Subtração
        '3': a * b,           # Multiplicação
        '4': a / b if b != 0 else 'Erro: Divisão por 0'  # Divisão com verificação de zero
    }.get(op, 'Escolha inválida!')  # Retorna mensagem se a operação for inválida
    
    

def calculadora():
    """Função principal que executa a calculadora em loop até que o usuário decida sair."""
    while True:
        # Mensagem de boas-vindas e opções de operação
        print('\nBem-vindo à calculadora!')
        print('Selecione a operação:')
        print('1. Soma')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('5. Sair')
        
        
    
        # Captura a escolha do usuário
        escolha = input('Digite o número da operação (1/2/3/4/5): ')

        # Verifica se o usuário deseja sair
        if escolha == '5':
            print('Saindo da calculadora. Até logo!')
            break  # Sai do loop e encerra a calculadora
        
        
        
        try:
            # Solicita a entrada dos números
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            # Chama a função de calcular e armazena o resultado
            
            resultado = calcular(escolha, num1, num2)
            # Exibe o resultado
            
            print(f'Resultado: {resultado}')
        except ValueError:
            
            # Trata erros de entrada se o usuário não digitar um número válido
            print('Entrada inválida! Por favor, insira números.')

# Executar a calculadora
if __name__ == "__main__":
    calculadora()
