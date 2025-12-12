# 5 Exemplos de Funções Síncronas (Sync)

# 1. Função para Cálculo de IMC

def calcular_imc(peso_kg, altura_m):
    """
    Calcula o Índice de Massa Corporal (IMC)
    Args:
        peso_kg: peso em quilogramas
        altura_m: altura em metros
    Returns:
        imc: valor do IMC
        classificacao: classificação do IMC
    """
    imc = peso_kg / (altura_m ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade Grau I"
    elif imc < 40:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III"

    return round(imc, 2), classificacao

# Uso:
peso = 70
altura = 1.75
imc, classificacao = calcular_imc(peso, altura)
print(f"IMC: {imc} - {classificacao}")

# 2. Função para Validar CPF

def validar_cpf(cpf):
    """
    Valida um CPF brasileiro
    Args:
        cpf: string contendo o CPF (com ou sem formatação)
    Returns:
        bool: True se CPF válido, False caso contrário
    """
    import re

    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)

    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

    # Verifica se os dígitos calculados coincidem
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

# Uso:
cpfs = ["123.456.789-09", "111.111.111-11", "529.982.247-25"]
for cpf in cpfs:
    valido = validar_cpf(cpf)
    print(f"CPF {cpf}: {'VÁLIDO' if valido else 'INVÁLIDO'}")

# 3. Função para Processar Arquivo CSV

def processar_csv(nome_arquivo, delimiter=','):
    """
    Lê e processa um arquivo CSV
    Args:
        nome_arquivo: caminho do arquivo CSV
        delimiter: separador de campos
    Returns:
        dict: dicionário com dados processados
    """
    import csv

    dados = {
        'total_linhas': 0,
        'cabecalhos': [],
        'registros': [],
        'estatisticas': {}
    }

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo, delimiter=delimiter)

            # Lê cabeçalho
            cabecalhos = next(leitor)
            dados['cabecalhos'] = cabecalhos

            # Processa linhas
            for linha in leitor:
                if linha:  # Ignora linhas vazias
                    dados['registros'].append(linha)
                    dados['total_linhas'] += 1

            # Calcula estatísticas simples
            if dados['registros']:
                num_colunas = len(cabecalhos)
                dados['estatisticas'] = {
                    'num_colunas': num_colunas,
                    'primeiros_5': dados['registros'][:5],
                    'ultimos_5': dados['registros'][-5:] if len(dados['registros']) > 5 else dados['registros']
                }

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado")
        return None
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None

    return dados

# Uso (criar arquivo de exemplo primeiro):
exemplo_csv = "dados.csv"
conteudo = """nome,idade,cidade
João,25,São Paulo
Maria,30,Rio de Janeiro
Carlos,35,Belo Horizonte
Ana,28,Curitiba
"""

with open(exemplo_csv, 'w', encoding='utf-8') as f:
    f.write(conteudo)

resultado = processar_csv(exemplo_csv)
if resultado:
    print(f"Total de registros: {resultado['total_linhas']}")
    print(f"Cabeçalhos: {resultado['cabecalhos']}")

# 4. Função para Gerar Senha Segura

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    """
    Gera uma senha aleatória segura
    Args:
        tamanho: comprimento da senha
        usar_maiusculas: incluir letras maiúsculas
        usar_numeros: incluir números
        usar_simbolos: incluir símbolos
    Returns:
        str: senha gerada
    """
    import random
    import string

    # Define os conjuntos de caracteres
    caracteres = string.ascii_lowercase  # sempre inclui minúsculas

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += "!@#$%&*()_+-=[]{}|;:,.<>?"

    # Garante que pelo menos um caractere de cada tipo selecionado está presente
    senha = []

    # Adiciona pelo menos uma minúscula
    senha.append(random.choice(string.ascii_lowercase))

    if usar_maiusculas:
        senha.append(random.choice(string.ascii_uppercase))
    if usar_numeros:
        senha.append(random.choice(string.digits))
    if usar_simbolos:
        senha.append(random.choice("!@#$%&*()_+-=[]{}|;:,.<>?"))

    # Completa o restante da senha
    while len(senha) < tamanho:
        senha.append(random.choice(caracteres))

    # Embaralha a senha
    random.shuffle(senha)

    return ''.join(senha)

# Uso:
for i in range(3):
    senha = gerar_senha(tamanho=16)
    print(f"Senha {i+1}: {senha}")

senha_simples = gerar_senha(tamanho=8, usar_simbolos=False)
print(f"Senha simples: {senha_simples}")

# 5. Função para Análise de Texto

def analisar_texto(texto):
    """
    Analisa um texto e retorna diversas estatísticas
    Args:
        texto: string com o texto a analisar
    Returns:
        dict: dicionário com as estatísticas
    """
    import re
    from collections import Counter

    # Remove espaços extras
    texto = texto.strip()

    if not texto:
        return {"erro": "Texto vazio"}

    # Estatísticas básicas
    palavras = re.findall(r'\b\w+\b', texto.lower())
    frases = re.split(r'[.!?]+', texto)
    frases = [f.strip() for f in frases if f.strip()]

    # Contagem
    total_palavras = len(palavras)
    total_caracteres = len(texto)
    total_frases = len(frases)

    # Palavras mais comuns
    contador_palavras = Counter(palavras)
    palavras_comuns = contador_palavras.most_common(5)

    # Palavras únicas
    palavras_unicas = set(palavras)

    # Médias
    media_palavras_por_frase = total_palavras / total_frases if total_frases > 0 else 0
    media_caracteres_por_palavra = total_caracteres / total_palavras if total_palavras > 0 else 0

    # Densidade léxica (palavras únicas / total palavras)
    densidade_lexica = len(palavras_unicas) / total_palavras if total_palavras > 0 else 0

    return {
        'total_palavras': total_palavras,
        'total_caracteres': total_caracteres,
        'total_frases': total_frases,
        'palavras_unicas': len(palavras_unicas),
        'palavras_comuns': palavras_comuns,
        'media_palavras_por_frase': round(media_palavras_por_frase, 2),
        'media_caracteres_por_palavra': round(media_caracteres_por_palavra, 2),
        'densidade_lexica': round(densidade_lexica, 3)
    }

# Uso:
texto_exemplo = """
Python é uma linguagem de programação de alto nível.
Ela é conhecida por sua sintaxe clara e legível.
Muitos programadores usam Python para automação,
análise de dados e desenvolvimento web.
Python é poderosa e fácil de aprender.
"""

analise = analisar_texto(texto_exemplo)
for chave, valor in analise.items():
    print(f"{chave}: {valor}")