# 1. int (Números Inteiros)

# Números inteiros (positivos, negativos ou zero)
# Sem limite de tamanho (apenas limitado pela memória)

x = 10
y = -5
z = 0
grande = 123456789012345678901234567890

# 2. float (Números de Ponto Flutuante)

# Números decimais (com casas após a vírgula)
#Precisão limitada (cerca de 15-16 casas decimais)

a = 3.14
b = -2.5
c = 4.0
d = 2.998e8  # Notação científica: 2.998 × 10⁸

# 3. complex (Números Complexos)

# Números com parte real e imaginária
# Parte imaginária representada por j

c1 = 3 + 4j
c2 = 2 - 1j
c3 = 5j      # Apenas parte imaginária

# Operações Comuns:

# Aritméticas Básicas:
# Adição, subtração, multiplicação

soma = 5 + 3        # 8
subtracao = 10 - 4  # 6
multiplicacao = 7 * 2  # 14

# Divisão (sempre retorna float)
divisao = 10 / 3    # 3.333...

# Divisão inteira
div_inteira = 10 // 3  # 3

# Módulo (resto da divisão)
resto = 10 % 3      # 1

# Potência
potencia = 2 ** 3   # 8

# Conversões entre Tipos:

# float para int (trunca a parte decimal)
x = int(3.14)       # 3

# int para float
y = float(5)        # 5.0

# string para número
z = int("10")       # 10
w = float("3.14")   # 3.14

# Funções Úteis:

# Type

print(type(c3))
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(abs(-5)))
print(type(round(3.14159, 2)))
print(type(pow(2, 3)))
print(type(min(5, 2, 8)))
print(type(max(5, 2, 8)))

# Valor absoluto
abs(-5)             # 5

# Arredondamento
round(3.14159, 2)   # 3.14

# Potência (alternativa a **)
pow(2, 3)           # 8

# Mínimo e máximo
min(5, 2, 8)        # 2
max(5, 2, 8)        # 8

# Exemplos Práticos:

# Trabalhando com diferentes tipos
idade = 25              # int
altura = 1.75           # float
numero_complexo = 2+3j  # complex

# Operações mistas
resultado = idade + altura  # 26.75 (float)


# Características Importantes:

# Python converte automaticamente em operações mistas (int → float)
# Precisão do float pode causar pequenos erros de arredondamento
# Números complexos são úteis para cálculos matemáticos avançados
# Esses tipos numéricos formam a base para praticamente todos os cálculos matemáticos e científicos em Python!