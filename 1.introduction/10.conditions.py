# Exemplo 1: Verificação Simples

idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
# Output: "Maior de idade"

# Exemplo 2: Múltiplas Condições

nota = 85

if nota >= 90:
    print("Conceito A")
elif nota >= 80:
    print("Conceito B")
elif nota >= 70:
    print("Conceito C")
elif nota >= 60:
    print("Conceito D")
else:
    print("Conceito F")
# Output: "Conceito B"

# Operadores de Comparação

a = 10
b = 5

# Igualdade
if a == b:
    print("São iguais")
else:
    print("São diferentes")  # Este será executado

# Maior/Menor
if a > b:
    print("a é maior que b")  # Executado

if a < b:
    print("a é menor que b")
else:
    print("a não é menor que b")  # Executado

# Diferente
if a != b:
    print("a é diferente de b")  # Executado

# Maior/Menor ou igual
if a >= 10:
    print("a é maior ou igual a 10")  # Executado

# Operadores Lógicos: and, or, not
# Exemplo 3: Condições Compostas

idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")  # Executado
else:
    print("Não pode dirigir")

# Com parênteses para clareza
if (idade >= 18) and (tem_carteira):
    print("Pode dirigir")  # Executado

# Exemplo 4: Verificando Múltiplas Opções

dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Fim de semana!")  # Executado
else:
    print("Dia de semana")

# Com not
chovendo = False

if not chovendo:
    print("Pode sair sem guarda-chuva")  # Executado
else:
    print("Melhor levar guarda-chuva")

# Condicionais Aninhadas
# Exemplo 5: Sistema de Login

usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto:
    if senha == senha_correta:
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")

# Exemplo 6: Verificação de Número

numero = 15

if numero > 0:
    print("Número positivo")
    if numero % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")  # Executado
elif numero < 0:
    print("Número negativo")
else:
    print("Número zero")

# Condicionais com Strings
# Exemplo 7: Validação de Email

email = "usuario@example.com"

if email:
    if "@" in email and "." in email:
        print("Email válido")  # Executado
    else:
        print("Email inválido")
else:
    print("Email não pode estar vazio")

# Exemplo 8: Menu de Opções

opcao = input("Escolha uma opção (1-3): ")

if opcao == "1":
    print("Opção 1 selecionada: Cadastrar usuário")
elif opcao == "2":
    print("Opção 2 selecionada: Listar usuários")
elif opcao == "3":
    print("Opção 3 selecionada: Sair")
else:
    print("Opção inválida!")

# Condicionais com Listas
# Exemplo 9: Verificando Listas

lista_compras = ["leite", "pão", "ovos"]

if lista_compras:  # Verifica se a lista não está vazia
    print("Lista de compras:")
    for item in lista_compras:
        print(f"- {item}")
else:
    print("Lista de compras vazia")

# Verificando se elemento existe na lista
if "leite" in lista_compras:
    print("Leite está na lista")  # Executado

# Exemplo 10: Sistema de Notas com Lista

notas = [7.5, 8.0, 6.5, 9.0]

if notas:  # Se a lista não estiver vazia
    media = sum(notas) / len(notas)

    if media >= 7:
        print(f"Aprovado com média {media:.2f}")
    elif media >= 5:
        print(f"Recuperação com média {media:.2f}")
    else:
        print(f"Reprovado com média {media:.2f}")
else:
    print("Nenhuma nota informada")

# Condicionais com Dicionários
# Exemplo 11: Sistema de Permissões


usuario = {
    "nome": "João",
    "idade": 25,
    "nivel_acesso": "admin"
}

if usuario.get("nivel_acesso") == "admin":
    print("Acesso total ao sistema")  # Executado
elif usuario.get("nivel_acesso") == "usuario":
    print("Acesso limitado")
else:
    print("Acesso negado")

# Verificando múltiplas chaves
if usuario.get("nome") and usuario.get("idade"):
    print("Usuário completo")  # Executado
else:
    print("Dados incompletos")

# Operador Ternário
# Exemplo 12: Sintaxe Curta

idade = 20
status = "Maior" if idade >= 18 else "Menor"
print(status)  # "Maior"

# Equivalente a:
if idade >= 18:
    status = "Maior"
else:
    status = "Menor"

# Exemplo 13: Múltiplas Condições no Ternário

nota = 85
resultado = "Aprovado" if nota >= 70 else "Recuperação" if nota >= 50 else "Reprovado"
print(resultado)  # "Aprovado"

# Equivalente:
if nota >= 70:
    resultado = "Aprovado"
elif nota >= 50:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

# Exemplos Práticos do Mundo Real
# Exemplo 14: Calculadora de IMC

peso = 70
altura = 1.75

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"  # Executado
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade Grau I"
elif imc < 40:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

print(f"IMC: {imc:.2f} - {classificacao}")

# Exemplo 15: Sistema de Desconto


valor_compra = 250
cliente_fidelidade = True
primeira_compra = False

desconto = 0

if valor_compra > 200:
    desconto = 0.10  # 10%
elif valor_compra > 100:
    desconto = 0.05  # 5%

if cliente_fidelidade:
    desconto += 0.05  # +5%

if primeira_compra:
    desconto += 0.02  # +2%

valor_final = valor_compra * (1 - desconto)
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto: {desconto*100:.0f}%")
print(f"Valor final: R$ {valor_final:.2f}")

# Exemplo 16: Validação de Formulário

nome = "João Silva"
email = "joao@email.com"
idade = "25"

erros = []

if not nome or len(nome.strip()) < 2:
    erros.append("Nome deve ter pelo menos 2 caracteres")

if not email or "@" not in email:
    erros.append("Email inválido")

if not idade.isdigit() or not (18 <= int(idade) <= 120):
    erros.append("Idade deve ser entre 18 e 120 anos")

if erros:
    print("Erros no formulário:")
    for erro in erros:
        print(f"- {erro}")
else:
    print("Formulário válido!")

# Condicionais com Match-Case (Python 3.10+)
# Exemplo 17: Pattern Matching

def classificar_pontuacao(pontos):
    match pontos:
        case 0:
            return "Zero pontos"
        case 1 | 2 | 3:
            return "Poucos pontos"
        case 4 | 5 | 6:
            return "Pontos médios"
        case 7 | 8 | 9:
            return "Muitos pontos"
        case 10:
            return "Pontuação máxima"
        case _:
            return "Pontuação inválida"

print(classificar_pontuacao(5))  # "Pontos médios"

# Dicas e Boas Práticas
# Exemplo 18: Código Limpo

# ❌ Evite condições muito complexas
if (idade >= 18 and tem_carteira and not suspenso and horas_dormidas > 6):
    print("Pode dirigir")

# ✅ Melhor: divida em variáveis com nomes descritivos
pode_dirigir_idade = idade >= 18
pode_dirigir_carteira = tem_carteira and not suspenso
pode_dirigir_descansado = horas_dormidas > 6

if pode_dirigir_idade and pode_dirigir_carteira and pode_dirigir_descansado:
    print("Pode dirigir")

# Exemplo 19: Early Return

def verificar_acesso(usuario, recurso):
    # Retornos antecipados para casos de erro
    if not usuario:
        return "Usuário não autenticado"

    if not usuario.get("ativo"):
        return "Usuário inativo"

    if recurso not in usuario.get("permissoes", []):
        return "Acesso negado ao recurso"

    # Caso de sucesso
    return "Acesso permitido"

resultado = verificar_acesso({"ativo": True, "permissoes": ["admin"]}, "admin")
print(resultado)  # "Acesso permitido"

# Exemplo 20: Condicionais com Funções

def e_numero_par(n):
    return n % 2 == 0

def e_numero_positivo(n):
    return n > 0

numero = 10

if e_numero_par(numero) and e_numero_positivo(numero):
    print("Número par e positivo")  # Executado

# Usando funções em condicionais complexas
if all([e_numero_par(numero), e_numero_positivo(numero), numero < 100]):
    print("Número atende a todos os critérios")  # Executado
