import adivinhacao
import forca

print("--------------------------------------")
print("------------Escolha o jogo!-----------")
print("--------------------------------------")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Escolha um aopção: "))

if jogo == 1:
    print()
    print("Jogando forca")
    forca.jogar()  # Inicialziando função dentro de Import!
elif jogo == 2:
    print()
    print("Jogando adivinhação")
    adivinhacao.jogar()  # Inicialziando função dentro de Import!


