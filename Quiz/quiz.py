import os
import random

def mostrar_menu(): #Menu
    os.system("cls")
    print("Quiz Arduino")
    print("============")
    print("1- Responder Quiz")
    print("2 - Exibir Regras")
    print("3 - Encerrar Programa")

def mostrar_regras(): #Regras
    os.system("cls")
    print("Regras do Jogo")
    print("==============")
    print("1- Selecione apenas uma resposta (Como: A, B, C, D ou E)")
    print("2- Cada resposta correta vale 0,5 pontos")
    input("Pressione Enter para voltar")

def jogo(): #Quiz
    for i in range(1, 20):
        nuquest = sortear_questoes()
        quest = perguntas(nuquest)
        correta = exibir_questao(quest, i)
        respostauser = input("Escolha uma opção: ").lower().strip()#deixa minuscula e sem espaço
        if correta == respostauser: #verifica caso a resposta do usuário for correta
            print("Você acertou! +0,5 pontos")
        else:
            print("Resposta incorreta, a resposta correta era - ", correta.upper())
        input("Pressione Enter para continuar")

def sair():
    os.system("cls")
    print("Obrigado por jogar!")
    print("Volte sempre!")
    exit() #Fecha o programa


lista=[] #Lista para armazenar os números já usados
def sortear_questoes():
    questao = random.randint(0, 5) #Gera um número aleatório para a pergunta
    while questao in lista:
        questao = random.randint(0, 5)
    lista.append(questao)
    return(questao)

def exibir_questao(quest, i):
    correta = 'a' #Por enquanto ⚠️⚠️⚠️⚠️
    #
    # PRECISA FAZER SISTEMA DE ALEATORIEDADE 🤫
    #

    os.system("cls")
    print("Questão de número", i)
    print(quest[0])
    print("=============")
    print("A -", quest[1])
    print("B -", quest[2])
    print("C -", quest[3])
    print("D -", quest[4])
    print("E- ", quest[5])
    print(lista, "teste")
    return(correta)

    
def perguntas(nuquest):
    #perguntas[0] = pergunta
    #perguntas[1] = resposta correta
    #perguntas[2,3,4] = respostas erradas
    perguntas = [
        [
            "Qual componente é usado para limitar a corrente em um circuito?",
            "Resistor",
            "Capacitor",
            "Diodo",
            "Transistor",
            "Placa de prototipagem (breadboard)"
        ],
        [
            "Qual dispositivo converte sinais digitais em sinais analógicos?",
            "Conversor Digital-Analógico (DAC)",
            "Conversor Analógico-Digital (ADC)",
            "Amplificador",
            "Oscilador",
            "Placa de prototipagem (breadboard)"
        ],
        [
            "Qual pino do Arduino é geralmente usado para comunicação serial?",
            "Pino 0 (RX)",
            "Pino 13",
            "Pino A0",
            "Pino 5V",
            "Placa de prototipagem (breadboard)"
        ],
        [
            "Qual linguagem de programação é mais utilizada no Arduino?",
            "C/C++",
            "Python",
            "Java",
            "Scratch",
            "Placa de prototipagem (breadboard)"
        ],
        [
            "Qual componente é usado para armazenar carga elétrica?",
            "Capacitor",
            "Resistor",
            "LED",
            "Transistor",
            "Placa de prototipagem (breadboard)"
        ],
        [
            "Qual comando do Arduino é usado para definir a velocidade de comunicação serial?",
            "Serial.begin()",
            "Serial.print()",
            "Serial.read()",
            "Serial.write()",
            "Placa de prototipagem (breadboard)"
        ]
    ]
    return(perguntas[nuquest])

while True:
    mostrar_menu()
    resposta = int(input("Sua ação:"))
    if resposta == 2:
        mostrar_regras()
    elif resposta == 3:
        sair()
    elif resposta == 1:
        jogo()

