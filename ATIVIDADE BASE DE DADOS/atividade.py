nome = input("Digite o seu nome: " )
print(nome)
idade = int(input("Digite sua idade: "))
print(idade)

if idade >= 18:
    print("Bem-vindo a festa")
else:
    print("Você não pode entrar.")
    
with open("baseDeDados.csv", "a") as arquivo:
    arquivo.write(f"{nome}\n")
    arquivo.write(f"{idade}\n")