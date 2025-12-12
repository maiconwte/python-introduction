# Exemplo 1: Menu Interativo

# Sistema de menu com while
saldo = 1000.00

while True:
    print("\n" + "="*30)
    print("BANCO DIGITAL")
    print("="*30)
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    print("="*30)

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        print(f"\nSeu saldo é: R$ {saldo:.2f}")

    elif opcao == "2":
        while True:
            try:
                valor = float(input("\nValor do depósito: R$ "))
                if valor > 0:
                    saldo += valor
                    print(f"Depósito realizado! Novo saldo: R$ {saldo:.2f}")
                    break
                else:
                    print("Valor deve ser positivo!")
            except ValueError:
                print("Digite um valor numérico válido!")

    elif opcao == "3":
        while True:
            try:
                valor = float(input("\nValor do saque: R$ "))
                if valor > saldo:
                    print("Saldo insuficiente!")
                elif valor <= 0:
                    print("Valor deve ser positivo!")
                else:
                    saldo -= valor
                    print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")
                    break
            except ValueError:
                print("Digite um valor numérico válido!")

    elif opcao == "4":
        print("\nObrigado por usar nosso banco!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")

print("Sistema encerrado.")

# Exemplo 2: Jogo de Adivinhação com Limites

import random

print("🎯 JOGO DE ADIVINHAÇÃO 🎯")
print("Adivinhe o número entre 1 e 100")

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 10
acertou = False

while tentativas < max_tentativas and not acertou:
    tentativas += 1
    print(f"\nTentativa {tentativas} de {max_tentativas}")

    while True:
        try:
            palpite = int(input("Seu palpite: "))
            if 1 <= palpite <= 100:
                break
            else:
                print("Digite um número entre 1 e 100")
        except ValueError:
            print("Digite um número válido!")

    if palpite < numero_secreto:
        print("Dica: Tente um número MAIOR!")
    elif palpite > numero_secreto:
        print("Dica: Tente um número MENOR!")
    else:
        acertou = True
        print(f"🎉 PARABÉNS! Você acertou em {tentativas} tentativas!")

if not acertou:
    print(f"\n💀 GAME OVER! O número era {numero_secreto}")

# Perguntar se quer jogar novamente
jogar_novamente = input("\nJogar novamente? (s/n): ").lower()
if jogar_novamente == 's':
    print("Reiniciando o jogo...")
    # Aqui você poderia reiniciar o jogo

# Exemplo 3: Validação de Formulário

print("📝 CADASTRO DE USUÁRIO 📝")

dados_validos = False

while not dados_validos:
    print("\nPreencha os dados abaixo:")

    # Nome (mínimo 3 caracteres)
    while True:
        nome = input("Nome completo: ").strip()
        if len(nome) >= 3:
            break
        print("Nome deve ter pelo menos 3 caracteres")

    # Email (deve conter @ e .)
    while True:
        email = input("Email: ").strip().lower()
        if "@" in email and "." in email:
            break
        print("Email inválido! Deve conter '@' e '.'")

    # Senha (mínimo 6 caracteres)
    while True:
        senha = input("Senha (mínimo 6 caracteres): ")
        if len(senha) >= 6:
            # Confirmação de senha
            confirmacao = input("Confirme a senha: ")
            if senha == confirmacao:
                break
            print("As senhas não coincidem!")
        else:
            print("Senha muito curta!")

    # Idade (entre 0 e 120)
    while True:
        try:
            idade = int(input("Idade: "))
            if 0 <= idade <= 120:
                break
            print("Idade deve estar entre 0 e 120 anos")
        except ValueError:
            print("Digite um número válido!")

    # Exibir resumo e confirmar
    print("\n" + "="*30)
    print("CONFIRMAÇÃO DOS DADOS")
    print("="*30)
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Idade: {idade} anos")
    print("="*30)

    confirmar = input("\nOs dados estão corretos? (s/n): ").lower()
    if confirmar == 's':
        dados_validos = True
        print("\n✅ Cadastro realizado com sucesso!")
    else:
        print("\nVamos começar novamente...")

# Exemplo 4: Simulador de Caixa Eletrônico

print("🏧 SIMULADOR DE CAIXA ELETRÔNICO 🏧")

notas_disponiveis = [100, 50, 20, 10, 5, 2]
continuar = True

while continuar:
    print("\n" + "="*30)

    while True:
        try:
            valor = int(input("Valor do saque: R$ "))
            if valor <= 0:
                print("Valor deve ser positivo!")
                continue

            # Verifica se o valor pode ser composto com as notas disponíveis
            if valor % 2 != 0 and valor < 5:
                print("Valor não pode ser sacado com as notas disponíveis!")
                print("Notas disponíveis: R$ 100, 50, 20, 10, 5, 2")
                continue

            break
        except ValueError:
            print("Digite um valor numérico válido!")

    valor_restante = valor
    notas_entregues = {}

    print(f"\nSaque de R$ {valor:.2f}:")

    for nota in notas_disponiveis:
        if valor_restante >= nota:
            quantidade = valor_restante // nota
            notas_entregues[nota] = quantidade
            valor_restante %= nota

    if valor_restante == 0:
        print("Notas entregues:")
        total_notas = 0
        for nota, quantidade in sorted(notas_entregues.items(), reverse=True):
            if quantidade > 0:
                print(f"  {quantidade} nota(s) de R$ {nota:.2f}")
                total_notas += quantidade

        print(f"\nTotal de notas: {total_notas}")
    else:
        print("Não foi possível sacar este valor com as notas disponíveis!")
        print(f"Faltou: R$ {valor_restante:.2f}")

    # Perguntar se quer fazer outro saque
    while True:
        resposta = input("\nDeseja fazer outro saque? (s/n): ").lower()
        if resposta in ['s', 'n']:
            continuar = (resposta == 's')
            break
        print("Digite 's' para sim ou 'n' para não")

print("\nObrigado por usar nosso caixa eletrônico!")

# Exemplo 5: Sistema de Temperatura com Média

print("🌡️ SISTEMA DE MONITORAMENTO DE TEMPERATURA 🌡️")

temperaturas = []
continuar_monitoramento = True
alerta_ativo = False

print("Digite as temperaturas (°C). Para parar, digite 'sair'")

while continuar_monitoramento:
    entrada = input(f"\nTemperatura {len(temperaturas) + 1}: ").strip().lower()

    if entrada == 'sair':
        if len(temperaturas) == 0:
            print("Nenhuma temperatura registrada!")
            continuar_monitoramento = False
            continue

        print("\n" + "="*30)
        print("RELATÓRIO FINAL")
        print("="*30)
        continuar_monitoramento = False

    else:
        try:
            temperatura = float(entrada)
            temperaturas.append(temperatura)

            # Verificar alerta (acima de 40°C ou abaixo de 0°C)
            if temperatura > 40:
                print("⚠️  ALERTA: Temperatura muito ALTA!")
                alerta_ativo = True
            elif temperatura < 0:
                print("⚠️  ALERTA: Temperatura muito BAIXA!")
                alerta_ativo = True

            # Estatísticas atuais
            if len(temperaturas) > 0:
                media = sum(temperaturas) / len(temperaturas)
                maxima = max(temperaturas)
                minima = min(temperaturas)

                print(f"Registros: {len(temperaturas)}")
                print(f"Média atual: {media:.1f}°C")
                print(f"Temperatura máxima: {maxima:.1f}°C")
                print(f"Temperatura mínima: {minima:.1f}°C")

                # Tendência
                if len(temperaturas) > 1:
                    if temperatura > temperaturas[-2]:
                        print("Tendência: ↗️ Subindo")
                    elif temperatura < temperaturas[-2]:
                        print("Tendência: ↘️ Descendo")
                    else:
                        print("Tendência: → Estável")

        except ValueError:
            print("❌ Digite um número válido ou 'sair' para encerrar")

# Relatório final
if temperaturas:
    print(f"\nTotal de registros: {len(temperaturas)}")
    print(f"Temperatura média: {sum(temperaturas)/len(temperaturas):.1f}°C")
    print(f"Temperatura máxima: {max(temperaturas):.1f}°C")
    print(f"Temperatura mínima: {min(temperaturas):.1f}°C")

    # Classificação
    media_final = sum(temperaturas) / len(temperaturas)
    if media_final > 30:
        classificacao = "Muito quente"
    elif media_final > 20:
        classificacao = "Agradável"
    elif media_final > 10:
        classificacao = "Fresco"
    else:
        classificacao = "Frio"

    print(f"Classificação: {classificacao}")

    if alerta_ativo:
        print("\n⚠️  ATENÇÃO: Foram detectadas temperaturas extremas!")

print("\nMonitoramento encerrado.")