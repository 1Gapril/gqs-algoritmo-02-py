# gqs-algoritmo-02-py

AQUI EMBAIXO ESTA O CODIGO NO MOMENTO
--------------------------------------------------------------------------------------
import math

# Códigos de cores para o terminal
VERDE = "\033[92m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

# Cabeçalho em formato de caixa colorida
print(f"{AZUL}{NEGRITO}╔══════════════════════════════════════════════════════════════╗")
print("║    CALCULADORA DE HIPOTENUSA (SUPORTE A NÚMEROS NEGATIVOS)   ║")
print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")

print(f"{VERDE}Calculadora Iniciada com Sucesso!{RESET}")

while True:
    print(f"\n{AMARELO}--- Novo Cálculo ---{RESET}")
    
    # O bloco try vai tentar capturar os dados e calcular
    try:
        a = float(input("Digite o valor do lado A: "))
        b = float(input("Digite o valor do lado B: "))
        c = float(input("Digite o valor do lado C: "))

        # Cálculo da hipotenusa
        hipotenusa = math.sqrt(a**2 + b**2 + c**2)
        
        # Regra para valores negativos
        if a < 0 and b < 0 and c < 0:
            hipotenusa = -hipotenusa

        # Exibe o resultado final em VERDE
        print(f"{VERDE}{NEGRITO}Hipotenusa: {hipotenusa:.2f}{RESET}")
        
    except ValueError:
        # Se o usuário digitar letras, o Python entra aqui e mostra o aviso em VERMELHO
        print(f"{VERMELHO}{NEGRITO}[ERRO] Comando inválido! Digite apenas números.{RESET}")
        continue # Faz o programa pular o resto e voltar para o começo do 'while' de forma limpa
    
    # Pergunta para continuar (só aparece se os números estiverem certos)
    opcao = input("\nDeseja fazer outro cálculo? (S para Sim / N para Não): ")
    if opcao.upper() == "N":
        print(f"\n{AZUL}Obrigado por usar a calculadora! Até logo.{RESET}")
        break
