import os
import random

def mostrar_menu():
    os.system("cls")
    print("Quiz Arduino")
    print("============")
    print("1- Responder Quiz")
    print("2 - Exibir Regras")
    print("3 - Encerrar Programa")

def mostrar_regras():
    os.system("cls")
    print("Regras do Jogo")
    print("1- Selecione apenas uma resposta (Como: A,B,C ou D)")
    input("Pressione Enter para voltar")

def jogo():
    for i in range(0, 20):
        nuquest = sortear_questoes()
        quest = exibir_questao(nuquest)

def sortear_questoes():
    lista=[]
    questao = random.randint(1, 50)
    while questao in lista:
        questao = random.randint(1, 50)
    lista.append(questao)
    return(questao)

def exibir_questao(numero):
    print("preto")

    
while True:
    mostrar_menu()
    resposta = int(input("Sua ação:"))
    if resposta == 2:
        mostrar_regras()

