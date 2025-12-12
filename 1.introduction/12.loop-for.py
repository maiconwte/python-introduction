# Exemplo 1: Iteração Básica em Lista

# Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

print("Lista de frutas:")
for fruta in frutas:
    print(f"- {fruta.capitalize()}")

# Com índice usando enumerate()
print("\nFrutas com índice:")
for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}. {fruta}")

# Exemplo 2: Cálculos e Transformações

# Dados de temperatura em Celsius
temperaturas_celsius = [0, 10, 20, 30, 40]

print("Conversão Celsius → Fahrenheit:")
for celsius in temperaturas_celsius:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.1f}°F")

# Soma acumulada
print("\nSoma acumulada dos números:")
numeros = [1, 2, 3, 4, 5]
soma_acumulada = 0
for numero in numeros:
    soma_acumulada += numero
    print(f"Adicionando {numero}: soma = {soma_acumulada}")

# Exemplo 3: Iteração em Dicionário

# Dicionário de alunos e notas
alunos = {
    "Ana": [8.5, 7.0, 9.0],
    "Carlos": [6.0, 7.5, 8.0],
    "Maria": [9.5, 8.5, 10.0],
    "João": [5.5, 6.0, 7.0]
}

print("Médias dos alunos:")
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 7.0 else "Recuperação"
    print(f"{nome}: média = {media:.2f} ({status})")

# Filtrando alunos aprovados
print("\nAlunos aprovados:")
for nome in alunos:
    media = sum(alunos[nome]) / len(alunos[nome])
    if media >= 7.0:
        print(f"✅ {nome}: {media:.2f}")

# Exemplo 4: Aninhado e Padrões

# Tabuada
print("Tabuada do 1 ao 5:")
for i in range(1, 6):  # 1 a 5
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):  # 1 a 10
        print(f"{i} x {j} = {i*j}")

# Padrão de asteriscos
print("\nPadrão de triângulo:")
for linha in range(1, 6):
    print("*" * linha)

# Lista de listas (matriz)
print("\nPercorrendo matriz:")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        print(f"matriz[{i}][{j}] = {valor}")

# Exemplo 5: Processamento de Texto e Arquivos


# Analisando texto
texto = """Python é uma linguagem de programação de alto nível.
Ela é conhecida por sua sintaxe clara e legível.
Muitos programadores usam Python para automação, análise de dados e web."""

print("Análise do texto:")
palavras = texto.split()
total_palavras = len(palavras)

# Contar palavras únicas
palavras_unicas = set()
for palavra in palavras:
    palavras_unicas.add(palavra.lower().strip(".,"))

print(f"Total de palavras: {total_palavras}")
print(f"Palavras únicas: {len(palavras_unicas)}")

# Palavras com mais de 5 letras
print("\nPalavras com mais de 5 letras:")
longas = [palavra for palavra in palavras if len(palavra) > 5]
for palavra in longas:
    print(f"- {palavra}")

# Simulação de leitura de arquivo
print("\nProcessamento linha por linha (simulado):")
linhas = texto.split("\n")
for numero, linha in enumerate(linhas, 1):
    num_palavras = len(linha.split())
    print(f"Linha {numero}: {num_palavras} palavras")
    print(f"  Conteúdo: {linha[:50]}..." if len(linha) > 50 else f"  Conteúdo: {linha}")

# Bônus: Exemplo com range() e condições

# Números pares e ímpares
print("Números de 1 a 20:")
pares = []
impares = []

for numero in range(1, 21):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")

# Fatorial
print("\nFatoriais:")
for n in range(1, 6):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(f"{n}! = {fatorial}")
