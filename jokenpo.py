# OBS: Eu estou utilizando um teclado americano, por isso que esta sem os acentos.

import random

usuario = int(input("Digite um dessas 3 opcoes:\n 0: Pedra, 1: Papel, 2: Tesoura \n"))

computador = random.randint(0,2)

# Pedra perde para papel
# Papel perde para tesoura
# Tesoura perde para pedra

# Teste para verificar se o usuario vai ganhar
if usuario == 1 and computador == 0:
    print("O usuario ganhou")
elif usuario == 2 and computador == 1:
    print("O usuario ganhou")
elif usuario == 0 and computador == 2:
    print("O usuario ganhou")

# Teste para verificar se o computador vai ganhar
if computador == 1 and usuario == 0:
    print("O computador ganhou")
elif computador == 2 and usuario == 1:
    print("O computador ganhou")
elif computador == 0 and usuario == 2:
    print("O computador ganhou")

# Teste para verificar se vai ser empate
if usuario == 0 and computador == 0:
    print("Deu empate")
elif usuario == 1 and computador == 1:
    print("Deu empate")
elif usuario == 2 and computador == 2:
    print("Deu empate")

print("\n")

# Essa parte do pograma imprimi a opcao escolhida pelo computador
print("O computador escolheu:")
if computador == 0:
    print("Pedra")
elif computador == 1:
    print("Papel")
elif computador == 2:
    print("Tesoura")

# Essa parte do pograma imprimi a opcao escolhida pelo usuario
print("O usuario escolheu:")
if usuario == 0:
    print("Pedra")
elif usuario == 1:
    print("Papel")
elif usuario == 2:
    print("Tesoura")
else:
    print("Opcao invalida")
