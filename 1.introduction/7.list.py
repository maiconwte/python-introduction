first_list = [1, 2, 3, 4, "Maico", True, False, 3.14, 2+3j, 5 - 6j, type(1-1j)]

print(first_list)
print(type(first_list))
print(len(first_list))
print(first_list)

# O que são Listas?
# Listas são coleções ordenadas, mutáveis e que permitem elementos duplicados.

# Sintaxe: elementos entre colchetes [], separados por vírgula
minha_lista = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
mista = [1, "texto", 3.14, True]

# Criação de Listas

# Formas de criar listas
lista_vazia = []
lista1 = [1, 2, 3]
lista2 = list([1, 2, 3])  # Usando construtor list()
lista3 = list("abc")       # ['a', 'b', 'c']

# Lista com repetição
repetida = [0] * 5         # [0, 0, 0, 0, 0]

# Range para lista
numeros = list(range(5))   # [0, 1, 2, 3, 4]

# Acesso aos Elementos
#Indexação Positiva e Negativa:

frutas = ["maçã", "banana", "laranja", "uva", "manga"]

print(frutas[0])    # "maçã" - primeiro elemento
print(frutas[2])    # "laranja" - terceiro elemento
print(frutas[-1])   # "manga" - último elemento
print(frutas[-2])   # "uva" - penúltimo elemento

# Fatiamento - Slice

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:5])     # [2, 3, 4]       - posição 2 até 4
print(numeros[:4])      # [0, 1, 2, 3]    - do início até 3
print(numeros[5:])      # [5, 6, 7, 8, 9] - da posição 5 até fim
print(numeros[::2])     # [0, 2, 4, 6, 8] - cada 2 elementos
print(numeros[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - inverte

# Modificação de Listas
# Alterar Elementos:

frutas = ["maçã", "banana", "laranja"]
frutas[1] = "morango"        # ["maçã", "morango", "laranja"]

# Alterar com slicing
frutas[0:2] = ["pera", "kiwi"]  # ["pera", "kiwi", "laranja"]

# Adicionar Elementos:

lista = [1, 2, 3]

# append() - adiciona ao final
lista.append(4)              # [1, 2, 3, 4]

# insert() - adiciona em posição específica
lista.insert(1, 1.5)         # [1, 1.5, 2, 3, 4]

# extend() - adiciona elementos de outra lista
lista.extend([5, 6])         # [1, 1.5, 2, 3, 4, 5, 6]

# Operador +
outra_lista = lista + [7, 8]  # [1, 1.5, 2, 3, 4, 5, 6, 7, 8]

# Remover Elementos:

lista = [1, 2, 3, 2, 4, 2]

# remove() - remove primeira ocorrência do valor
lista.remove(2)              # [1, 3, 2, 4, 2]

# pop() - remove e retorna elemento da posição
elemento = lista.pop(1)      # elemento = 3, lista = [1, 2, 4, 2]
ultimo = lista.pop()         # ultimo = 2, lista = [1, 2, 4]

# del - remove por índice ou slicing
del lista[0]                 # [2, 4]
del lista[1:]                # [2]

# clear() - esvazia a lista
lista.clear()                # []

# Métodos Úteis

numeros = [1, 2, 3, 2, 5, 2]

# index() - retorna índice da primeira ocorrência
posicao = numeros.index(3)   # 2

# count() - conta ocorrências
quantidade = numeros.count(2)  # 3

# sort() - ordena a lista
numeros.sort()               # [1, 2, 2, 2, 3, 5]
numeros.sort(reverse=True)   # [5, 3, 2, 2, 2, 1]

# reverse() - inverte a ordem
numeros.reverse()            # [1, 2, 2, 2, 3, 5]

# copy() - cria cópia superficial
copia = numeros.copy()       # nova lista independente

# Operações com Listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenação
combinada = lista1 + lista2  # [1, 2, 3, 4, 5, 6]

# Repetição
repetida = lista1 * 3        # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Verificação
existe = 2 in lista1         # True
nao_existe = 7 in lista1     # False

# Comprimento
tamanho = len(lista1)        # 3

# List Comprehension
# Forma concisa de criar listas:

# Sintaxe: [expressão for item in iterável if condição]

# Quadrados dos números
quadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Números pares
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Transformar strings
nomes = ["ana", "joão", "maria"]
maiusculas = [nome.upper() for nome in nomes]  # ["ANA", "JOÃO", "MARIA"]

# Lista de tuplas
coordenadas = [(x, x**2) for x in range(3)]  # [(0, 0), (1, 1), (2, 4)]

# Listas Aninhadas (Matrizes)

# Matriz 2x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][1])    # 2 - linha 0, coluna 1
print(matriz[1][2])    # 6 - linha 1, coluna 2

# Acessar linha inteira
print(matriz[1])       # [4, 5, 6]

# Percorrer matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# Funções Úteis com Listas

numeros = [3, 1, 4, 1, 5, 9, 2]

# min() e max()
menor = min(numeros)        # 1
maior = max(numeros)        # 9

# sum() - soma dos elementos
soma = sum(numeros)         # 25

# sorted() - retorna nova lista ordenada
ordenada = sorted(numeros)  # [1, 1, 2, 3, 4, 5, 9]
decrescente = sorted(numeros, reverse=True)  # [9, 5, 4, 3, 2, 1, 1]

# enumerate() - percorre com índice
for indice, valor in enumerate(numeros):
    print(f"Índice {indice}: {valor}")

# zip() - combina listas
nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 35]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

# Exemplos Práticos
# Gerenciamento de Tarefas:

tarefas = []

# Adicionar tarefas
tarefas.append("Estudar Python")
tarefas.append("Fazer compras")
tarefas.insert(0, "Reunião importante")

print(f"Tarefas pendentes: {len(tarefas)}")  # 3

# Completar primeira tarefa
tarefa_concluida = tarefas.pop(0)
print(f"Concluída: {tarefa_concluida}")  # "Reunião importante"

# Análise de Dados:

notas = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5]

# Estatísticas básicas
media = sum(notas) / len(notas)
melhor_nota = max(notas)
pior_nota = min(notas)

print(f"Média: {media:.2f}")        # Média: 7.75
print(f"Melhor nota: {melhor_nota}") # Melhor nota: 9.0
print(f"Pior nota: {pior_nota}")     # Pior nota: 6.5

# Notas acima da média
acima_media = [nota for nota in notas if nota > media]
print(f"Notas acima da média: {acima_media}")  # [8.0, 9.0, 8.5]

# Manipulação de Strings:

texto = "Python é uma linguagem poderosa"
palavras = texto.split()  # Divide por espaços

print(f"Número de palavras: {len(palavras)}")  # 5
print(f"Palavras em maiúsculo: {[p.upper() for p in palavras]}")

# Juntar novamente
novo_texto = " ".join(palavras)  # "Python é uma linguagem poderosa"

# Importante: Referências vs Cópias

# Cópia superficial (shallow copy)
original = [1, 2, 3]
copia = original.copy()  # ou list(original) ou original[:]
copia[0] = 99

print(original)  # [1, 2, 3] - não foi alterada
print(copia)     # [99, 2, 3]

# Referência (cuidado!)
referencia = original
referencia[0] = 100
print(original)  # [100, 2, 3] - foi alterada!