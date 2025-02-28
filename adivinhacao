import random

# Exibindo o menu de dificuldades
print("### MENU DE DIFICULDADE ###")
print("1 - Fácil (1 a 50, 5 tentativas)")
print("2 - Médio (1 a 100, 4 tentativas)")
print("3 - Difícil (1 a 200, 3 tentativas)")

# O usuário escolhe a dificuldade
opcao = int(input("Digite a opção desejada: "))

# Ajustando as configurações com base na escolha
if opcao == 1:
    numero_max = 50
    tentativas_max = 5
    print("Você escolheu a dificuldade Fácil!")
elif opcao == 2:
    numero_max = 100
    tentativas_max = 4
    print("Você escolheu a dificuldade Média!")
elif opcao == 3:
    numero_max = 200
    tentativas_max = 3
    print("Você escolheu a dificuldade Difícil!")
else:
    print("Opção inválida!")
    exit()  # Sai do programa caso a opção seja inválida

# Gerando o número sorteado
sorteio = random.randint(1, numero_max)

# Iniciando o jogo de adivinhação
print(f"\nAdivinhe o número que estou pensando, de 1 a {numero_max}")
tentativas = 1

# Loop do jogo
while tentativas <= tentativas_max:
    print(f"Tentativa {tentativas}/{tentativas_max}")
    chute = int(input("Digite o seu chute: "))

    if chute == sorteio:
        print(f"Parabéns, você acertou! O número era {sorteio}.")
        break
    elif chute > sorteio:
        print("Chute um número menor.")
    else:
        print("Chute um número maior.")

    tentativas += 1

if chute != sorteio:
    print(f"Você não acertou. O número era {sorteio}.")
