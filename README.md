# 🧮 Calculadora de Hipotenusa

Este projeto é uma calculadora de hipotenusa que, após receber os valores dos lados A e B determinados pelo usuário, utiliza o Teorema de Pitágoras para calcular a hipotenusa. O projeto também possui suporte a números negativos, tratamento de entradas inválidas e permite que o usuário realize diversos cálculos sem que o programa seja finalizado.

# 📦 Instalação

Para utilizar o programa, é necessário ter o **Python 3** instalado em seu computador.

Não é necessário instalar bibliotecas externas, pois o projeto utiliza apenas a biblioteca `math`, que já está incluída no Python.

# ▶️ Como executar

Após baixar ou clonar o repositório, abra o terminal na pasta onde o arquivo `main.py` está localizado e execute:

```bash
python main.py
```

# 🧪 Exemplo

## Entrada

```text
╔══════════════════════════════════════════════════════════════════════╗
║      CALCULADORA DE HIPOTENUSA (SUPORTE A NÚMEROS NEGATIVOS)         ║
╚══════════════════════════════════════════════════════════════════════╝

Calculadora Iniciada com Sucesso!

--- Novo Cálculo ---

Digite o valor do lado A: 3
Digite o valor do lado B: 4
```

## Saída

```text
Hipotenusa: 5.00

Deseja fazer outro cálculo? (S para Sim / N para Não): N

Obrigado por usar a calculadora! Até logo.
```

# 🧮 Como funciona

O programa utiliza o **Teorema de Pitágoras** para calcular a hipotenusa:

```text
h = √(A² + B²)
```

No código Python, o cálculo é realizado através da biblioteca `math`:

```python
hipotenusa = math.sqrt(a**2 + b**2)
```

Por exemplo:

```text
A = 3
B = 4

h = √(3² + 4²)
h = √25
h = 5
```

# ➖ Suporte a números negativos

O programa também permite a utilização de números negativos.

Quando os dois valores informados são negativos, o resultado também recebe o sinal negativo.

Exemplo:

```text
Digite o valor do lado A: -3
Digite o valor do lado B: -4

Hipotenusa: -5.00
```

# ⚠️ Tratamento de erros

Caso o usuário digite letras ou outro valor que não possa ser convertido para número, o programa apresenta uma mensagem de erro:

```text
[ERRO] Comando inválido! Digite apenas números.
```

Depois disso, o programa retorna para um novo cálculo.

# 🔄 Repetição

Após realizar um cálculo, o programa pergunta:

```text
Deseja fazer outro cálculo? (S para Sim / N para Não):
```

Caso o usuário escolha `S`, um novo cálculo é iniciado.

Caso escolha `N`, o programa é encerrado:

```text
Obrigado por usar a calculadora! Até logo.
```

# 👨‍💻 Sobre o Autor

Projeto desenvolvido por **Gabriel Ferreira** para a disciplina de **Garantia da Qualidade de Software / Gestão e Qualidade de Software**.

**Professor:** Daniel Henrique Matos de Paiva

**Repositório:** `gqs-algoritmo-02-py`
