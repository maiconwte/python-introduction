print("Digite seu nome: ")
name = input()
print("Digite sua idade: ")
age = input()

print(f"Seu nome é {name} e sua idade é {age}")

message = "Pode dirigir" if int(age) >= 18 else "Não pode dirigir"

print(message)