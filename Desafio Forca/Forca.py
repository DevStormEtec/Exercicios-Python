import random
import os

palavras = ["MARTELO", "TABUA", "PLANETA", "ARVORE", "TERRA", "PONTE", "HIPOPOTAMO", "PAREDE", "HIDROMASSAGEM", "OLHO", "MOSCA", "ILHA", "LAMPADA", "ARTES", "LOMBADA"]

def desenhar_forca(estagio):
    if estagio == 0:
        print(" _______")
        print("|/      ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
    elif estagio == 1:
        print(" _______")
        print("|/      |")
        print("|      ( )")
        print("|       ")
        print("|       ")
        print("|       ")
    elif estagio == 2:
        print(" _______")
        print("|/      |")
        print("|      ( )")
        print("|       |")
        print("|       |")
        print("|       ")
    elif estagio == 3:
        print(" _______")
        print("|/      |")
        print("|      ( )")
        print("|      /|\\")
        print("|       |")
        print("|       ")
    elif estagio == 4:
        print(" _______")
        print("|/      |")
        print("|      ( )")
        print("|      /|\\")
        print("|       |")
        print("|      /  ")
    elif estagio == 5:
        print(" _______")
        print("|/      |")
        print("|      ( )")
        print("|      /|\\")
        print("|       |")
        print("|      / \\")

def jogar_forca():
    aleatorio = random.randint(0, 14)
    palavraaleatoria = palavras[aleatorio]
    letras_certas = ["_"] * len(palavraaleatoria)
    letras_chutadas = []
    estagio = 0
    max_erros = 5

    while estagio < max_erros and "_" in letras_certas:
        os.system("cls")
        desenhar_forca(estagio)
        print(*letras_certas)
        print("Letras chutadas:", *letras_chutadas)

        chute = input("\nChute uma letra em CAPSLOCK: ")
        letras_chutadas.append(chute)
        
        if len(chute) > 1:
            if chute == palavraaleatoria:
                letras_certas = list(palavraaleatoria)
                break
            else:
                estagio = 5

        if chute in palavraaleatoria:
            for i in range(len(palavraaleatoria)):
                if palavraaleatoria[i] == chute:
                    letras_certas[i] = chute
        else:
            estagio += 1
    os.system("cls")
    desenhar_forca(estagio)
    print("\nPalavra:", *letras_certas)
    if "_" not in letras_certas:
        print("\n Parabéns! Você acertou a palavra:", palavraaleatoria)
    else:
        print("\n Você perdeu! A palavra era:", palavraaleatoria)
    input()
jogar_forca()
