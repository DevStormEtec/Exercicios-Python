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
    os.system("cls") #Limpa a tela
    print("Regras do Jogo")
    print("==============")
    print("1- Selecione apenas uma resposta (Como: A, B, C, D ou E)")
    print("2- Cada resposta correta vale 0,5 pontos")
    input("Pressione Enter para voltar")

def jogo(): #Quiz
    pontos = 0 #Variável para inicializar os pontos do usuário, assim toda vez que iniciar o jogo os pontos começam em 0
    lista.clear() #Limpa a lista de perguntas já feitas
    for i in range(1, 21): #Loop para 20 perguntas
        nuquest = sortear_questoes()
        quest = perguntas(nuquest)
        correta = exibir_questao(quest, i)
        respostauser = input("Escolha uma opção: ").lower().strip()#deixa minuscula e sem espaço
        if correta == respostauser: #verifica caso a resposta do usuário for correta
            print("Você acertou! +0,5 pontos")
            pontos = pontos + 0.5 #Sistema para adicionar pontos ao usuario
        else:
            print("Resposta incorreta, a resposta correta era - ", correta.upper()) #upper() deixa maiuscula
        input("Pressione Enter para continuar")
    os.system("cls") #Limpa a tela
    if pontos == 10:
        print("Parabéns! Você fez a pontuação máxima de 10 pontos!")
    else: 
        print("Fim de jogo! Você fez", pontos, "pontos.")
    input("Pressione Enter para voltar ao menu")

def sair():
    os.system("cls") #Limpa a tela
    print("Obrigado por jogar!")
    print("Volte sempre!")
    exit() #Fecha o programa
    


lista=[] #Lista para armazenar os números já usados
def sortear_questoes():
    questao = random.randint(0, 19) #Gera um número aleatório para a pergunta
    while questao in lista: #Enquanto a questão estiver na lista, gera outro número, para assim nao repetir perguntas
        questao = random.randint(0, 19)
    lista.append(questao)
    return(questao)

def exibir_questao(quest, i):
    #sistema de aleatoriedade
    pergunta = quest[0] #Diz a pergunta
    correta = quest[1] #Guarda a resposta correta

    #OBS: criamos uma lista apenas com as respostas para embaralhar
    resposta = quest[1:6] #Pega as respostas, OBS: o índice 6 não é incluído
    random.shuffle(resposta) #Embaralha as respostas

    ##exibir questão
    os.system("cls") #Limpa a tela
    print("Questão de número", i) 
    print(pergunta) 
    print("=============")
    print("A -", resposta[0]) 
    print("B -", resposta[1])
    print("C -", resposta[2])
    print("D -", resposta[3])
    print("E- ", resposta[4])

    indice_correto = resposta.index(correta) #Encontra o índice da resposta correta na lista embaralhada
    #O .index() retorna o índice da primeira ocorrência do valor especificado
    letras = ['a', 'b', 'c', 'd', 'e'] #Lista de letras correspondentes às opções
    letra_correta = letras[indice_correto] #Obtém a letra correspondente
    return(letra_correta)

    
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
        ],
        [
            "Qual função é utilizada para configurar um pino como entrada ou saída no Arduino?",
            "pinMode()",
            "digitalRead()",
            "digitalWrite()",
            "analogWrite()",
            "analogRead()"
        ],
        [
            "Qual componente é utilizado para emitir luz em projetos Arduino?",
            "LED",
            "Resistor",
            "Capacitor",
            "Transistor",
            "Potenciômetro"
        ],
        [
            "Qual a função do comando delay() no Arduino?",
            "Pausar o programa por milissegundos",
            "Aumentar a velocidade do programa",
            "Encerrar o programa",
            "Reiniciar o Arduino",
            "Medir o tempo decorrido"
        ],
        [
            "Qual é a voltagem típica de operação do Arduino UNO?",
            "5V",
            "3.3V",
            "12V",
            "9V",
            "1.5V"
        ],
        [
            "Qual sensor é usado para medir temperatura em projetos Arduino?",
            "DHT11",
            "HC-SR04",
            "LDR",
            "PIR",
            "MPU6050"
        ],
        [
            "Qual função é executada continuamente em um programa Arduino?",
            "loop()",
            "setup()",
            "main()",
            "start()",
            "run()"
        ],
        [
            "Qual sensor é utilizado para medir distância em projetos Arduino?",
            "HC-SR04",
            "DHT11",
            "LDR",
            "PIR",
            "BMP280"
        ],
        [
            "Como se chama o processo de enviar um programa para o Arduino?",
            "Upload",
            "Download",
            "Install",
            "Copy",
            "Transfer"
        ],
        [
            "Qual componente é usado para controlar a velocidade de motores DC?",
            "Transistor",
            "Resistor",
            "Capacitor",
            "LED",
            "Cristal"
        ],
        [
            "Qual é a função do comando Serial.println()?",
            "Imprimir texto com quebra de linha",
            "Ler dados da porta serial",
            "Configurar velocidade serial",
            "Fechar a porta serial",
            "Limpar o monitor serial"
        ],
        [
            "Qual sensor é usado para detectar movimento em projetos Arduino?",
            "PIR",
            "LDR",
            "DHT11",
            "BMP280",
            "HC-SR04"
        ],
        [
            "Qual componente é usado para variar a resistência manualmente?",
            "Potenciômetro",
            "Resistor",
            "Capacitor",
            "LED",
            "Transistor"
        ],
        [
            "Qual função é executada apenas uma vez quando o Arduino inicia?",
            "setup()",
            "loop()",
            "main()",
            "start()",
            "begin()"
        ],
        [
            "Qual porta analógica do Arduino UNO tem maior resolução?",
            "Todas têm 10 bits",
            "A0",
            "A1",
            "A2",
            "A3"
        ]
    ]
    return(perguntas[nuquest])

while True: #Loop do programa
    mostrar_menu()
    resposta = int(input("Sua ação:"))
    if resposta == 1:
        jogo()
    elif resposta == 2:
        mostrar_regras()
    elif resposta == 3:
        sair()

