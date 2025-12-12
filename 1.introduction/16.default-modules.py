# Módulos Padrão do Python - Resumo
# Módulos padrão (também chamados de "biblioteca padrão") vêm pré-instalados com o Python, prontos p ara uso sem instalação adicional.

import math # importando o módulo math

print(math.sqrt(16)) # raiz quadrada de 16

# 1. os - Interação com Sistema Operacional

import os

# 1. Verificar se arquivo existe
if os.path.exists("meuarquivo.txt"):
    print("Arquivo existe!")
else:
    print("Arquivo não encontrado")

# 2. Listar arquivos de um diretório
arquivos = os.listdir(".")
print(f"Arquivos no diretório: {arquivos}")

# 3. Obter diretório atual
diretorio_atual = os.getcwd()
print(f"Diretório atual: {diretorio_atual}")

# 4. Criar diretório
os.makedirs("novo_diretorio", exist_ok=True)

# 5. Juntar caminhos (evita problemas com / ou \)
caminho = os.path.join("pasta", "subpasta", "arquivo.txt")
print(f"Caminho: {caminho}")

# 2. datetime - Trabalhar com Datas e Horas

from datetime import datetime, date, timedelta

# 1. Data e hora atual
agora = datetime.now()
print(f"Agora: {agora}")
print(f"Data: {agora.date()}")
print(f"Hora: {agora.time()}")

# 2. Criar data específica
aniversario = date(2024, 12, 25)
print(f"Natal: {aniversario}")

# 3. Formatar data
formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Formatada: {formatada}")

# 4. Calcular diferença entre datas
hoje = date.today()
amanha = hoje + timedelta(days=1)
diferenca = amanha - hoje
print(f"Dias até amanhã: {diferenca.days}")

# 5. Extrair partes da data
print(f"Ano: {agora.year}, Mês: {agora.month}, Dia: {agora.day}")

# 3. random - Geração de Números Aleatórios

import random

# 1. Número aleatório entre 0 e 1
print(f"Random float: {random.random()}")

# 2. Número inteiro em um intervalo
dado = random.randint(1, 6)
print(f"Lançamento de dado: {dado}")

# 3. Escolher elemento aleatório de uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
sorteada = random.choice(frutas)
print(f"Fruta sorteada: {sorteada}")

# 4. Embaralhar lista
cartas = ["Ás", "Rei", "Rainha", "Valete"]
random.shuffle(cartas)
print(f"Cartas embaralhadas: {cartas}")

# 5. Amostra aleatória sem repetição
numeros = list(range(1, 51))
sorteio = random.sample(numeros, 5)
print(f"Números da loteria: {sorted(sorteio)}")

# 4. json - Trabalhar com JSON

import json

# Dados de exemplo
dados_pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo",
    "hobbies": ["leitura", "futebol", "viagem"]
}

# 1. Converter dicionário para JSON (serialização)
json_string = json.dumps(dados_pessoa, indent=2, ensure_ascii=False)
print("JSON string:")
print(json_string)

# 2. Salvar JSON em arquivo
with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_pessoa, arquivo, indent=2, ensure_ascii=False)

# 3. Ler JSON de string
dados_recuperados = json.loads(json_string)
print(f"\nNome: {dados_recuperados['nome']}")

# 4. Ler JSON de arquivo
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados_arquivo = json.load(arquivo)
    print(f"Cidade: {dados_arquivo['cidade']}")

# 5. Tipos de dados suportados automaticamente
dados_complexos = {
    "string": "texto",
    "numero": 42,
    "float": 3.14,
    "lista": [1, 2, 3],
    "dicionario": {"chave": "valor"},
    "booleano": True,
    "nulo": None
}
print(f"\nTipos suportados: {list(dados_complexos.keys())}")

# 5. collections - Estruturas de Dados Avançadas

from collections import Counter, defaultdict, deque, namedtuple

# 1. Counter - contar elementos
texto = "banana"
contador = Counter(texto)
print(f"Contagem de 'banana': {contador}")
print(f"'a' aparece {contador['a']} vezes")

# 2. defaultdict - dicionário com valor padrão
contatos = defaultdict(list)  # Valor padrão é lista vazia
contatos["João"].append("1111-1111")
contatos["Maria"].append("2222-2222")
contatos["João"].append("3333-3333")  # Adiciona à lista existente
print(f"\nContatos: {dict(contatos)}")

# 3. deque - lista otimizada para ambas as extremidades
fila = deque(["Alice", "Bob", "Charlie"])
fila.append("David")  # Adiciona no final
fila.appendleft("Zoe")  # Adiciona no início
print(f"\nFila: {fila}")
print(f"Próximo: {fila.popleft()}")  # Remove do início

# 4. namedtuple - tupla com campos nomeados
Pessoa = namedtuple("Pessoa", ["nome", "idade", "cidade"])
p1 = Pessoa("Maria", 25, "Rio de Janeiro")
print(f"\nNamedtuple: {p1}")
print(f"Nome: {p1.nome}, Idade: {p1.idade}")

# 5. Exemplo prático combinado
# Contar palavras em um texto
frase = "o gato caçou o rato e o rato fugiu do gato"
palavras = frase.split()
contador_palavras = Counter(palavras)
print(f"\nContagem de palavras: {contador_palavras}")

# Outros Módulos Úteis:

# sys - interação com o interpretador Python
import sys
print(f"Versão Python: {sys.version}")

# math - funções matemáticas
import math
print(f"Raiz quadrada de 16: {math.sqrt(16)}")

# re - expressões regulares
import re
email = "usuario@exemplo.com"
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Email válido")

# csv - trabalhar com arquivos CSV
import csv

# statistics - estatísticas básicas
import statistics
dados = [1, 2, 3, 4, 5]
print(f"Média: {statistics.mean(dados)}")

# Como Saber o que um Módulo Oferece:

import math

# 1. Listar todas as funções/variáveis
print(dir(math)[:10])  # Primeiros 10 itens

# 2. Ver documentação
# print(help(math.sqrt))

# 3. Ver que tipo é
print(type(math.pi))  # <class 'float'>
print(type(math.sqrt))  # <class 'builtin_function_or_method'>

# Importação Alternativa:

# Importar apenas o necessário
from math import sqrt, pi
print(f"√16 = {sqrt(16)}")
print(f"π = {pi}")

# Renomear módulo/função
import datetime as dt
from math import factorial as fat
print(f"5! = {fat(5)}")