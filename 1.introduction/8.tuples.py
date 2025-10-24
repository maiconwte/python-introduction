# O que são Tuplas?
#Tuplas são coleções ordenadas, imutáveis e que permitem elementos duplicados.

# Sintaxe: elementos entre parênteses (), separados por vírgula
minha_tupla = (1, 2, 3, 4, 5)
frutas = ("maçã", "banana", "laranja")
mista = (1, "texto", 3.14, True)

# Tupla com um elemento (precisa da vírgula no final)
tupla_um_elemento = (1,)  # ✅ Correto
nao_e_tupla = (1)        # ❌ Isso é um inteiro!

# Criação de Tuplas

# Formas de criar tuplas
tupla_vazia = ()
tupla1 = (1, 2, 3)
tupla2 = tuple([1, 2, 3])  # Usando construtor tuple()
tupla3 = tuple("abc")       # ('a', 'b', 'c')

# Sem parênteses (tupla por vírgula)
tupla4 = 1, 2, 3           # (1, 2, 3)
tupla5 = 1,                # (1,)

# De outros iteráveis
lista = [1, 2, 3]
tupla_da_lista = tuple(lista)  # (1, 2, 3)

# Características Principais
# Imutabilidade:

tupla = (1, 2, 3)

# ❌ NÃO pode fazer isso:
# tupla[0] = 10        # TypeError
# tupla.append(4)      # AttributeError
# tupla.remove(2)      # AttributeError

# ✅ Pode criar nova tupla:
nova_tupla = tupla + (4, 5)  # (1, 2, 3, 4, 5)

# Acesso aos Elementos
# Indexação Positiva e Negativa:

cores = ("vermelho", "azul", "verde", "amarelo", "roxo")

print(cores[0])    # "vermelho" - primeiro elemento
print(cores[2])    # "verde" - terceiro elemento
print(cores[-1])   # "roxo" - último elemento
print(cores[-2])   # "amarelo" - penúltimo elemento

# Fatiamento (Slicing):

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numeros[2:5])     # (2, 3, 4)       - posição 2 até 4
print(numeros[:4])      # (0, 1, 2, 3)    - do início até 3
print(numeros[5:])      # (5, 6, 7, 8, 9) - da posição 5 até fim
print(numeros[::2])     # (0, 2, 4, 6, 8) - cada 2 elementos
print(numeros[::-1])    # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0) - inverte

# Operações com Tuplas

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenação
combinada = tupla1 + tupla2  # (1, 2, 3, 4, 5, 6)

# Repetição
repetida = tupla1 * 3        # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Verificação
existe = 2 in tupla1         # True
nao_existe = 7 in tupla1     # False

# Comprimento
tamanho = len(tupla1)        # 3

# Métodos Disponíveis

tupla = (1, 2, 3, 2, 5, 2)

# count() - conta ocorrências
quantidade = tupla.count(2)  # 3

# index() - retorna índice da primeira ocorrência
posicao = tupla.index(3)     # 2
posicao2 = tupla.index(2, 2)  # 3 (busca a partir da posição 2)

# Desempacotamento de Tuplas

# Desempacotamento simples
coordenadas = (10, 20)
x, y = coordenadas
print(f"x: {x}, y: {y}")  # x: 10, y: 20

# Troca de valores (sem variável temporária)
a, b = 5, 10
a, b = b, a  # Agora a=10, b=5

# Desempacotamento com * (empacota o restante)
valores = (1, 2, 3, 4, 5)
primeiro, *meio, ultimo = valores
print(primeiro)  # 1
print(meio)      # [2, 3, 4]  # Vira lista!
print(ultimo)    # 5

# Ignorar elementos
primeiro, _, terceiro, *_ = (1, 2, 3, 4, 5, 6)
print(primeiro)  # 1
print(terceiro)  # 3

# Tuplas vs Listas
# Quando usar tuplas:
# Dados que não devem ser modificados

# Chaves em dicionários (por serem imutáveis)

# Retorno múltiplo de funções

# Dados heterogêneos (diferentes tipos)

# Quando usar listas:
# Dados que precisam ser modificados

# Coleções homogêneas (mesmo tipo)
# Quando precisa adicionar/remover elementos

# Retorno Múltiplo de Funções:

def calcular_estatisticas(numeros):
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return media, maior, menor  # Retorna uma tupla

resultado = calcular_estatisticas([10, 20, 30, 40, 50])
# resultado = (30.0, 50, 10)

# Desempacotando o retorno
media, maximo, minimo = calcular_estatisticas([10, 20, 30, 40, 50])
print(f"Média: {media}, Máximo: {maximo}, Mínimo: {minimo}")

# Coordenadas e Pontos:

# Pontos no plano cartesiano
ponto_a = (3, 4)
ponto_b = (7, 1)

def calcular_distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

distancia = calcular_distancia(ponto_a, ponto_b)
print(f"Distância: {distancia:.2f}")  # Distância: 5.00

# Configurações Imutáveis:

# Configurações que não devem ser alteradas
CONFIGURACOES = (
    "localhost",  # host
    8080,         # port
    True,         # debug mode
)

HOST, PORT, DEBUG = CONFIGURACOES
print(f"Servidor: {HOST}:{PORT}")  # Servidor: localhost:8080

# Chaves em Dicionários:

# Tuplas podem ser chaves de dicionário (listas não!)
coordenadas_cidades = {
    ("São Paulo", "SP"): (23.5505, 46.6333),
    ("Rio de Janeiro", "RJ"): (22.9068, 43.1729),
    ("Belo Horizonte", "MG"): (19.9167, 43.9345)
}

# Acesso por tupla
sp_coords = coordenadas_cidades[("São Paulo", "SP")]
print(f"Coordenadas de SP: {sp_coords}")  # (23.5505, 46.6333)

# Tuplas Aninhadas

# Matriz como tupla de tuplas
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matriz[0][1])    # 2 - linha 0, coluna 1

# Percorrer tupla aninhada
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()

# Conversões

# Tupla para lista
tupla = (1, 2, 3)
lista = list(tupla)    # [1, 2, 3]

# Lista para tupla
lista = [4, 5, 6]
tupla = tuple(lista)   # (4, 5, 6)

# String para tupla
texto = "hello"
tupla_chars = tuple(texto)  # ('h', 'e', 'l', 'l', 'o')

# Funções Úteis com Tuplas

tupla = (3, 1, 4, 1, 5, 9, 2)

# min() e max()
menor = min(tupla)        # 1
maior = max(tupla)        # 9

# sum() - soma dos elementos
soma = sum(tupla)         # 25

# sorted() - retorna lista ordenada
ordenada = sorted(tupla)  # [1, 1, 2, 3, 4, 5, 9]

# any() e all()
valores = (True, False, True)
print(any(valores))  # True (pelo menos um True)
print(all(valores))  # False (nem todos são True)

# enumerate() - percorre com índice
for indice, valor in enumerate(tupla):
    print(f"Índice {indice}: {valor}")

# Vantagens das Tuplas
# Performance: Mais rápidas que listas

# Segurança: Dados protegidos contra modificação

# Hashable: Podem ser usadas como chaves em dicionários

# Elegância: Sintaxe limpa para retorno múltiplo

# Benchmark simples (tupla vs lista)
import timeit

tempo_tupla = timeit.timeit('x = (1, 2, 3, 4, 5)', number=1000000)
tempo_lista = timeit.timeit('x = [1, 2, 3, 4, 5]', number=1000000)

print(f"Tupla: {tempo_tupla:.4f}s")  # Geralmente mais rápido
print(f"Lista: {tempo_lista:.4f}s")
