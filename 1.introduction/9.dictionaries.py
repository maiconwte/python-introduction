# O que são Dicionários?
# Dicionários são coleções não ordenadas (até Python 3.6), mutáveis e indexadas por chaves. Armazenam pares chave:valor.

# Sintaxe: {chave1: valor1, chave2: valor2}
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Criação de Dicionários

# Formas de criar dicionários
dicionario_vazio = {}
dicionario1 = {"a": 1, "b": 2, "c": 3}
dicionario2 = dict(a=1, b=2, c=3)  # Usando construtor dict()

# De lista de tuplas
pares = [("nome", "Maria"), ("idade", 25)]
dicionario3 = dict(pares)  # {'nome': 'Maria', 'idade': 25}

# Com fromkeys() - todas chaves com mesmo valor
chaves = ["nome", "idade", "cidade"]
dicionario4 = dict.fromkeys(chaves, "desconhecido")
# {'nome': 'desconhecido', 'idade': 'desconhecido', 'cidade': 'desconhecido'}

# Acesso aos Elementos

pessoa = {"nome": "Ana", "idade": 28, "cidade": "Rio de Janeiro"}

# Acesso por colchetes
print(pessoa["nome"])   # "Ana"
print(pessoa["idade"])  # 28

# get() - acesso seguro (não gera erro se chave não existir)
print(pessoa.get("nome"))      # "Ana"
print(pessoa.get("email"))     # None
print(pessoa.get("email", "Não informado"))  # "Não informado"

# keys() - retorna todas as chaves
print(pessoa.keys())    # dict_keys(['nome', 'idade', 'cidade'])

# values() - retorna todos os valores
print(pessoa.values())  # dict_values(['Ana', 28, 'Rio de Janeiro'])

# items() - retorna pares (chave, valor)
print(pessoa.items())   # dict_items([('nome', 'Ana'), ('idade', 28), ('cidade', 'Rio de Janeiro')])

# Modificação de Dicionários
# Adicionar/Atualizar Elementos:

pessoa = {"nome": "Carlos", "idade": 35}

# Adicionar nova chave
pessoa["cidade"] = "Belo Horizonte"
# {'nome': 'Carlos', 'idade': 35, 'cidade': 'Belo Horizonte'}

# Atualizar valor existente
pessoa["idade"] = 36
# {'nome': 'Carlos', 'idade': 36, 'cidade': 'Belo Horizonte'}

# update() - atualizar múltiplos valores
pessoa.update({"idade": 37, "profissao": "Engenheiro"})
# {'nome': 'Carlos', 'idade': 37, 'cidade': 'Belo Horizonte', 'profissao': 'Engenheiro'}

# setdefault() - adiciona se chave não existir
pessoa.setdefault("email", "carlos@email.com")
pessoa.setdefault("nome", "Outro Nome")  # Não altera, pois chave já existe

# Remover Elementos:

pessoa = {"nome": "Maria", "idade": 25, "cidade": "São Paulo", "email": "maria@email.com"}

# pop() - remove e retorna valor
idade = pessoa.pop("idade")  # idade = 25
# pessoa = {'nome': 'Maria', 'cidade': 'São Paulo', 'email': 'maria@email.com'}

# popitem() - remove e retorna último par (chave, valor)
chave, valor = pessoa.popitem()  # ('email', 'maria@email.com')

# del - remove por chave
del pessoa["cidade"]
# pessoa = {'nome': 'Maria'}

# clear() - esvazia o dicionário
pessoa.clear()  # {}

# Métodos Úteis

dicionario = {"a": 1, "b": 2, "c": 3}

# copy() - cópia superficial
copia = dicionario.copy()

# fromkeys() - criar dicionário com chaves e valor padrão
novas_chaves = ["x", "y", "z"]
novo_dict = dict.fromkeys(novas_chaves, 0)  # {'x': 0, 'y': 0, 'z': 0}

# Compreensão de dicionário
quadrados = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Operações com Dicionários

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# União (Python 3.9+)
combinado = dict1 | dict2  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Verificação
existe = "a" in dict1      # True
nao_existe = "z" in dict1  # False

# Comprimento
tamanho = len(dict1)       # 2

# Iteração em Dicionários

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Iterar pelas chaves
for chave in pessoa:
    print(chave)

# Equivalente a:
for chave in pessoa.keys():
    print(chave)

# Iterar pelos valores
for valor in pessoa.values():
    print(valor)

# Iterar por chaves e valores
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Dictionary Comprehension

# Sintaxe: {chave: valor for item in iterável}

# Quadrados dos números
quadrados = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Transformar valores
pessoa = {"nome": "ana", "idade": "25", "cidade": "são paulo"}
maiusculas = {chave: valor.upper() for chave, valor in pessoa.items()}
# {'nome': 'ANA', 'idade': '25', 'cidade': 'SÃO PAULO'}

# Filtrar elementos
numeros = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
pares = {chave: valor for chave, valor in numeros.items() if valor % 2 == 0}
# {'b': 2, 'd': 4}

# Inverter chave e valor
invertido = {valor: chave for chave, valor in numeros.items()}
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# Dicionários Aninhados

# Dicionário dentro de dicionário
empresa = {
    "funcionario1": {
        "nome": "Ana Silva",
        "cargo": "Desenvolvedora",
        "salario": 5000
    },
    "funcionario2": {
        "nome": "Carlos Santos",
        "cargo": "Gerente",
        "salario": 8000
    }
}

# Acesso a elementos aninhados
print(empresa["funcionario1"]["nome"])    # "Ana Silva"
print(empresa["funcionario2"]["salario"]) # 8000

# Adicionar novo funcionário
empresa["funcionario3"] = {
    "nome": "Maria Oliveira",
    "cargo": "Designer",
    "salario": 4500
}

# Casos de Uso Comuns
# Configurações:

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "meu_banco"
    },
    "debug": True,
    "max_connections": 100,
    "allowed_hosts": ["127.0.0.1", "localhost"]
}

print(f"Host do banco: {config['database']['host']}")

# Contagem de Elementos:

# Contar frequência de palavras
texto = "o rato roeu a roupa do rei de roma"
palavras = texto.split()

contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)
# {'o': 2, 'rato': 1, 'roeu': 1, 'a': 1, 'roupa': 1, 'do': 1, 'rei': 1, 'de': 1, 'roma': 1}

# Usando Counter (forma mais eficiente)
from collections import Counter
contagem = Counter(palavras)

# Agrupamento de Dados:

# Agrupar pessoas por cidade
pessoas = [
    {"nome": "Ana", "cidade": "São Paulo"},
    {"nome": "Carlos", "cidade": "Rio de Janeiro"},
    {"nome": "Maria", "cidade": "São Paulo"},
    {"nome": "João", "cidade": "Belo Horizonte"}
]

agrupado = {}
for pessoa in pessoas:
    cidade = pessoa["cidade"]
    if cidade not in agrupado:
        agrupado[cidade] = []
    agrupado[cidade].append(pessoa["nome"])

print(agrupado)
# {'São Paulo': ['Ana', 'Maria'], 'Rio de Janeiro': ['Carlos'], 'Belo Horizonte': ['João']}

# Métodos Avançados

dicionario = {"a": 1, "b": 2, "c": 3}

# setdefault() - útil para valores padrão
dicionario.setdefault("d", 0)  # Se "d" não existe, cria com valor 0

# update() com outro dicionário
dicionario.update({"e": 5, "f": 6})

# fromkeys() com valor calculado
chaves = ["x", "y", "z"]
dicionario_novo = {chave: [] for chave in chaves}  # Cada chave com lista vazia

# Funções Úteis com Dicionários

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# any() / all()
valores_booleanos = {"ativo": True, "bloqueado": False}
print(any(valores_booleanos.values()))  # True (pelo menos um True)
print(all(valores_booleanos.values()))  # False (nem todos são True)

# sorted() - ordenar por chaves
ordenado_por_chave = dict(sorted(pessoa.items()))
# {'cidade': 'São Paulo', 'idade': 30, 'nome': 'João'}

# max() / min() com valores
idades = {"Ana": 25, "Carlos": 30, "Maria": 28}
mais_velho = max(idades, key=idades.get)  # "Carlos"
mais_novo = min(idades, key=idades.get)   # "Ana"

#Exemplos Práticos
# Sistema de Inventário:

inventario = {
    "maçã": {"quantidade": 50, "preco": 2.50},
    "banana": {"quantidade": 30, "preco": 1.80},
    "laranja": {"quantidade": 40, "preco": 3.00}
}

# Adicionar produto
inventario["uva"] = {"quantidade": 25, "preco": 4.50}

# Calcular valor total do inventário
valor_total = 0
for produto, info in inventario.items():
    valor_total += info["quantidade"] * info["preco"]

print(f"Valor total do inventário: R$ {valor_total:.2f}")

# Produtos com menos de 35 unidades
estoque_baixo = {
    produto: info
    for produto, info in inventario.items()
    if info["quantidade"] < 35
}

# Tradução Simples:

traducoes = {
    "hello": "olá",
    "world": "mundo",
    "python": "python",
    "code": "código"
}

def traduzir(texto):
    palavras = texto.lower().split()
    traducao = []
    for palavra in palavras:
        traducao.append(traducoes.get(palavra, palavra))
    return " ".join(traducoes)

texto_ingles = "hello world python code"
texto_portugues = traduzir(texto_ingles)
print(texto_portugues)  # "olá mundo python código"

# Cache Simples:

cache = {}
def calcular_fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = calcular_fibonacci(n-1) + calcular_fibonacci(n-2)
    return cache[n]

print(calcular_fibonacci(10))  # 55

cache = {}

def calculo_demorado(n):
    if n in cache:
        print(f"Usando cache para {n}")
        return cache[n]

    print(f"Calculando para {n}...")
    resultado = n * n  # Simulação de cálculo pesado
    cache[n] = resultado
    return resultado

print(calculo_demorado(5))  # Calcula
print(calculo_demorado(5))  # Usa cache

# Boas Práticas
# 1. Use chaves descritivas
# 2. Prefira get() para acesso seguro
# 3. Use dictionary comprehension para transformações
# 4. Considere collections.defaultdict para valores padrão
# 5. Use json para serialização/deserialização

# Dicionários são extremamente versáteis e uma das estruturas de dados mais úteis em Python, ideais para representar dados estruturados e mapeamentos!