calculadora_hipotenusa

import math

# Códigos de cores para o terminal
VERDE = "\033[92m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

# Cabeçalho em formato de caixa colorida
print(f"{AZUL}{NEGRITO}╔══════════════════════════════════════════════════════════════════════╗")
print("║      CALCULADORA DE HIPOTENUSA (SUPORTE A NÚMEROS NEGATIVOS)         ║")
print(f"╚══════════════════════════════════════════════════════════════════════╝{RESET}")

print(f"{VERDE}Calculadora Iniciada com Sucesso!{RESET}")

while True:
    print(f"\n{AMARELO}--- Novo Cálculo ---{RESET}")

    try:
        a = float(input("Digite o valor do lado A: "))
        b = float(input("Digite o valor do lado B: "))

        # Cálculo da hipotenusa
        hipotenusa = math.sqrt(a**2 + b**2)

        # Se os dois valores forem negativos, o resultado também será negativo
        if a < 0 and b < 0:
            hipotenusa = -hipotenusa

        print(f"{VERDE}{NEGRITO}Hipotenusa: {hipotenusa:.2f}{RESET}")

    except ValueError:
        print(f"{VERMELHO}{NEGRITO}[ERRO] Comando inválido! Digite apenas números.{RESET}")
        continue

    opcao = input("\nDeseja fazer outro cálculo? (S para Sim / N para Não): ")

    if opcao.upper() == "N":
        print(f"\n{AZUL}Obrigado por usar a calculadora! Até logo.{RESET}")
        break
