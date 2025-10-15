name = "Maico Silva."
name_complete = """Maicon
Silva."""

name_break = "Maico \
    Silva."""

print(name, name_complete, name_break)

# Formatação de Strings

name = "Maico Silva"
age = 30
height = 1.77

print(f"Name: {name}, Age: {age}, Height: {height}")
print("Name: {}, Age: {}, Height: {}".format(name, age, height))
print("Name: {0}, Age: {1}, Height: {2}".format(name, age, height))
print("Name: {name}, Age: {age}, Height: {height}".format(name=name, age=age, height=height))
print("My name is: %s" % name)

# Template de mensagem
template = """
Prezado {nome},

Seu pedido {codigo} foi processado.
Valor total: R$ {valor:.2f}

Atenciosamente,
Equipe {empresa}
"""

mensagem = template.format(
    nome="Carlos",
    codigo="ABC123",
    valor=157.50,
    empresa="Loja XPTO"
)

print(mensagem)

# Métodos de Transformação


texto = "  Hello, Python World!  "

# upper() - Maiúsculas
maiusculas = texto.upper()        # "  HELLO, PYTHON WORLD!  "

# lower() - Minúsculas
minusculas = texto.lower()        # "  hello, python world!  "

# capitalize() - Primeira maiúscula
capitalizado = "python".capitalize()  # "Python"

# title() - Cada palavra com inicial maiúscula
titulo = "hello world".title()    # "Hello World"

# swapcase() - Inverte maiúsculas/minúsculas
invertido = "PyThOn".swapcase()   # "pYtHoN"

# strip() - Remove espaços nas extremidades
limpo = texto.strip()             # "Hello, Python World!"

# lstrip() / rstrip() - Remove espaços à esquerda/direita
esquerda_limpa = texto.lstrip()   # "Hello, Python World!  "
direita_limpa = texto.rstrip()    # "  Hello, Python World!"

# Métodos de Busca e Verificação

frase = "Python é uma linguagem de programação"

# find() - Encontra a posição da substring
posicao = frase.find("linguagem")     # 12
nao_encontrado = frase.find("Java")   # -1

# index() - Como find(), mas gera erro se não encontrar
pos = frase.index("Python")           # 0

# count() - Conta ocorrências
quantidade = frase.count("a")         # 4

# startswith() - Verifica se começa com
comeca = frase.startswith("Python")   # True

# endswith() - Verifica se termina com
termina = frase.endswith("programação")  # True

# in - Verifica se contém (operador)
contem = "linguagem" in frase        # True

# Métodos de Divisão e Junção

# split() - Divide string em lista
csv = "maçã,banana,laranja,uva"
frutas = csv.split(",")              # ['maçã', 'banana', 'laranja', 'uva']

texto = "um dois três quatro"
palavras = texto.split()             # ['um', 'dois', 'três', 'quatro']

# splitlines() - Divide por linhas
texto_multilinha = "Linha 1\nLinha 2\nLinha 3"
linhas = texto_multilinha.splitlines()  # ['Linha 1', 'Linha 2', 'Linha 3']

# join() - Junta lista em string
lista = ['Python', 'Java', 'C++']
juntado = ', '.join(lista)           # "Python, Java, C++"

caminho = '/'.join(['usr', 'local', 'bin'])  # "usr/local/bin"

# Métodos de Substituição e Formatação


texto = "O gato caçou o rato"

# replace() - Substitui partes da string
novo_texto = texto.replace("gato", "cachorro")  # "O cachorro caçou o rato"
sem_espacos = texto.replace(" ", "")           # "Ogatocaçouorato"

# center() - Centraliza em um campo de largura fixa
centralizado = "Python".center(20, '-')  # "-------Python-------"

# ljust() / rjust() - Alinha à esquerda/direita
esquerda = "Python".ljust(10, '.')      # "Python...."
direita = "Python".rjust(10, '.')       # "....Python"

# zfill() - Preenche com zeros à esquerda
numero = "42".zfill(5)                  # "00042"

# Métodos de Verificação de Conteúdo

# isalpha() - Só contém letras?
"Python".isalpha()          # True
"Python3".isalpha()         # False

# isdigit() - Só contém dígitos?
"123".isdigit()             # True
"12.3".isdigit()            # False

# isalnum() - Só letras e números?
"Python3".isalnum()         # True
"Python 3".isalnum()        # False

# isspace() - Só espaços em branco?
"   ".isspace()             # True
" a ".isspace()             # False

# islower() / isupper() - Todas minúsculas/maiúsculas?
"python".islower()          # True
"PYTHON".isupper()          # True

# istitle() - Formato de título?
"Python Programming".istitle()  # True
"python programming".istitle()  # False

# Funções Built-in Úteis

texto = "Python"

# len() - Comprimento da string
tamanho = len(texto)                # 6

# ord() - Código Unicode do caractere
codigo = ord('A')                   # 65

# chr() - Caractere a partir do código Unicode
caractere = chr(65)                 # 'A'

# str() - Converte para string
numero_str = str(42)                # "42"
lista_str = str([1, 2, 3])          # "[1, 2, 3]"

# Métodos Avançados

# partition() - Divide em 3 partes baseado no separador
"python.java.javascript".partition('.')  # ('python', '.', 'java.javascript')

# rpartition() - Divide da direita para esquerda
"python.java.javascript".rpartition('.') # ('python.java', '.', 'javascript')

# removeprefix() / removesuffix() - Remove prefixo/sufixo (Python 3.9+)
"test.py".removeprefix("test.")          # "py"
"arquivo.txt".removesuffix(".txt")       # "arquivo"

# casefold() - Similar a lower(), mas mais agressivo para comparações
"STRASSE".casefold() == "straße".casefold()  # True

# Exemplos Práticos Combinados

# Limpar e formatar entrada do usuário
entrada_usuario = "  João da Silva  "
nome_formatado = entrada_usuario.strip().title()  # "João Da Silva"

# Validar email simples
email = "usuario@example.com"
if "@" in email and "." in email and not email.isspace():
    print("Email válido")

# Extrair extensão de arquivo
arquivo = "documento.pdf"
extensao = arquivo.split('.')[-1].lower()  # "pdf"

# Contar palavras
texto = "Python é uma linguagem poderosa"
quantidade_palavras = len(texto.split())  # 5

# Mascarar dados sensíveis
cpf = "123.456.789-00"
cpf_mascarado = cpf[:7] + "***-**"  # "123.456***-**"

# Gerar username
nome_completo = "Maria da Silva Santos"
username = nome_completo.lower().replace(" ", ".")  # "maria.da.silva.santos"