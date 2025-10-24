# Valores Falsos (Falsey):

# Todos estes são considerados False em contextos booleanos
bool(False)      # False
bool(0)          # False
bool(0.0)        # False
bool("")         # False - string vazia
bool([])         # False - lista vazia
bool(())         # False - tupla vazia
bool({})         # False - dicionário vazio
bool(None)       # False
bool(set())      # False - conjunto vazio

# Valores Verdadeiros (Truthy):

# Todos estes são considerados True
bool(True)              # True
bool(1)                 # True - qualquer número != 0
bool(-5)                # True
bool(3.14)              # True
bool("hello")           # True - string não vazia
bool([1, 2, 3])         # True - lista não vazia
bool((1, 2))            # True - tupla não vazia
bool({"nome": "João"})  # True - dicionário não vazio

# Operadores Lógicos

# Retorna True se AMBOS forem True
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Exemplos práticos
idade = 25
tem_carteira = True
pode_dirigir = idade >= 18 and tem_carteira  # True

# OR (or)
# Retorna True se PELO MENOS UM for True
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Exemplos práticos\
tem_dinheiro = False
tem_cartao = True
pode_comprar = tem_dinheiro or tem_cartao  # True

# NOT (not)

# Inverte o valor booleano
print(not True)     # False
print(not False)    # True

# Exemplos práticos
chovendo = True
pode_passear = not chovendo  # False

# Operadores de Comparação

x = 10
y = 5

# Igualdade
print(x == y)   # False
print(x == 10)  # True

# Diferença
print(x != y)   # True
print(x != 10)  # False

# Maior/Menor
print(x > y)    # True
print(x < y)    # False
print(x >= 10)  # True
print(x <= 5)   # False

# Exemplos Práticos
# Validação de Formulário:

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if nome and idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

# Validação de Email:
email = input("Digite seu email: ")
if "@" in email and "." in email:
    print("Email válido")
else:
    print("Email inválido")

# Controle de Acesso:

eh_admin = True
tem_permissao = False
modo_manutencao = False

pode_acessar = (eh_admin or tem_permissao) and not modo_manutencao
print(pode_acessar)  # True

# Verificação de Lista:

lista_compras = ["leite", "pão", "ovos"]
carteira = 50.0

tem_itens = bool(lista_compras)  # True (lista não vazia)
tem_dinheiro = carteira > 0      # True

pode_comprar = tem_itens and tem_dinheiro  # True

# Funções Úteis com Boolean
# bool() - Conversão para Boolean

print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Hello"))  # True
print(bool([]))       # False
print(bool([1, 2]))   # True

# any() - Retorna True se qualquer elemento for True

lista = [False, False, True, False]
print(any(lista))       # True

valores = [0, "", None, 5]
print(any(valores))     # True (porque 5 é Truthy)

# all() - Retorna True se TODOS elementos forem True
lista = [True, True, True]
print(all(lista))       # True

lista = [True, False, True]
print(all(lista))       # False

valores = [1, 2, 3]
print(all(valores))     # True

# Short-Circuit Evaluation
# Python para a avaliação quando o resultado já é conhecido:

# AND - para no primeiro False
def funcao_lenta():
    print("Esta função não será executada!")
    return True

resultado = False and funcao_lenta()  # funcao_lenta() NÃO é chamada

# OR - para no primeiro True
resultado2 = True or funcao_lenta()   # funcao_lenta() NÃO é chamada

# Boolean em Estruturas de Controle

idade = 20
tem_convite = True

# If statements
if idade >= 18 and tem_convite:
    print("Pode entrar na festa!")
else:
    print("Não pode entrar.")

# While loops
contador = 3
while contador > 0:  # Condição booleana
    print(contador)
    contador -= 1

# Com list comprehension
numeros = [1, 0, 3, 0, 5]
nao_zeros = [x for x in numeros if x]  # [1, 3, 5] (apenas valores Truthy)

# Truques úteis

# Verificar se string está vazia
nome = ""
if not nome:
    print("Nome não preenchido!")

# Verificar se lista tem elementos
lista = []
if lista:
    print("Lista tem elementos")
else:
    print("Lista vazia")

# Valor padrão com OR
nome = ""
nome_exibicao = nome or "Visitante"  # "Visitante"

cor_configurada = ""
cor_padrao = "azul"
cor_usada = cor_configurada or cor_padrao  # "azul"
