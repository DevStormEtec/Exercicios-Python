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
    # Ajustado para o novo total de 60 perguntas (índices 0 a 59)
    questao = random.randint(0, 59)
    while questao in lista:
        questao = random.randint(0, 59)
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
    #perguntas[2,3,4,5] = respostas erradas
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
        ],
        [
            "O que faz um transistor em um circuito?",
            "Amplificar ou chavear sinais",
            "Armazenar energia",
            "Medir corrente",
            "Emitir luz",
            "Converter sinais digitais"
        ],
        [
            "Qual é a função de um diodo em um circuito?",
            "Permitir fluxo de corrente em uma só direção",
            "Aumentar a corrente",
            "Armazenar energia elétrica",
            "Reduzir a tensão em metade",
            "Medir a temperatura"
        ],
        [
            "O que é um pull-up resistor?",
            "Resistor que garante nível alto quando o botão está aberto",
            "Resistor que diminui ruído",
            "Circuito integrado para USB",
            "Componente que emite luz",
            "Sensor de temperatura"
        ],
        [
            "Qual sensor é comumente usado para medir luminosidade?",
            "LDR (fotoresistor)",
            "DHT11",
            "HC-SR04",
            "PIR",
            "MPU6050"
        ],
        [
            "O que significa PWM no contexto do Arduino?",
            "Pulse Width Modulation (modulação por largura de pulso)",
            "Power With Microcontroller",
            "Programming With Memory",
            "Phase Wave Modulation",
            "Porta de leitura analógica"
        ],
        [
            "Qual biblioteca Arduino é usada para controlar servomotores?",
            "Servo.h",
            "Wire.h",
            "SPI.h",
            "LiquidCrystal.h",
            "EEPROM.h"
        ],
        [
            "Como se lê um valor analógico no Arduino?",
            "analogRead(pin)",
            "digitalRead(pin)",
            "analogWrite(pin)",
            "digitalWrite(pin)",
            "readAnalog(pin)"
        ],
        [
            "Qual componente é usado para armazenar um estado sem energia?",
            "EEPROM",
            "RAM",
            "CPU",
            "LED",
            "Resistor"
        ],
        [
            "Para que serve um capacitor em circuitos digitais?",
            "Filtrar ruídos e estabilizar tensões",
            "Aumentar a corrente de saída",
            "Converter corrente em tensão",
            "Ler sinais digitais",
            "Gerar pulso PWM"
        ],
        [
            "Qual sensor mede aceleração e giros (6 eixos)?",
            "MPU6050",
            "HC-SR04",
            "DHT11",
            "LDR",
            "PIR"
        ],
        [
            "Qual módulo é usado para conectar o Arduino à rede Wi-Fi?",
            "ESP8266/ESP32",
            "HC-SR04",
            "BMP280",
            "DHT22",
            "NRF24L01"
        ],
        [
            "O que faz um conversor ADC?",
            "Converte sinais analógicos em digitais",
            "Converte sinais digitais em analógicos",
            "Amplifica sinais",
            "Armazena dados",
            "Gera sinais PWM"
        ],
        [
            "Qual é a cor do fio geralmente usado como terra (GND)?",
            "Preto",
            "Vermelho",
            "Amarelo",
            "Branco",
            "Verde"
        ],
        [
            "Qual protocolo é usado para comunicação entre sensores e microcontroladores com linhas SDA/SCL?",
            "I2C",
            "SPI",
            "UART",
            "1-Wire",
            "CAN"
        ],
        [
            "O que é debounce em botões?",
            "Ignorar os múltiplos contatos elétricos do botão ao pressionar",
            "Aumentar a sensibilidade do botão",
            "Diminuir a corrente do botão",
            "Medir o tempo de pressão",
            "Converter analógico para digital"
        ],
        [
            "Qual sensor é ideal para medir pressão atmosférica?",
            "BMP280",
            "DHT11",
            "HC-SR04",
            "PIR",
            "LDR"
        ],
        [
            "Qual componente permite alterar resistência com um eixo giratório?",
            "Potenciômetro",
            "Capacitor",
            "Indutor",
            "Transistor",
            "Diodo"
        ],
        [
            "O que faz a função digitalWrite()?",
            "Configura um pino digital como HIGH ou LOW",
            "Lê um valor analógico",
            "Inicia a comunicação serial",
            "Define a frequência PWM",
            "Alimenta o microcontrolador"
        ],
        [
            "Qual protocolo é orientado a alta velocidade e usa MOSI/MISO/SCK?",
            "SPI",
            "I2C",
            "UART",
            "1-Wire",
            "CAN"
        ],
        [
            "Qual é a unidade de capacitância?",
            "Farad (F)",
            "Ohm (Ω)",
            "Henry (H)",
            "Volt (V)",
            "Ampere (A)"
        ],
        [
            "O que é um relé em eletrônica?",
            "Um interruptor controlado eletricamente",
            "Um tipo de capacitor",
            "Um sensor de distância",
            "Um regulador de tensão",
            "Um conversor ADC"
        ],
        [
            "Qual biblioteca facilita o uso de displays LCD 16x2 no Arduino?",
            "LiquidCrystal",
            "Servo",
            "SPI",
            "Ethernet",
            "Wire"
        ],
        [
            "Qual é a função de um regulador de tensão linear (ex: 7805)?",
            "Fornecer saída de tensão fixa estável",
            "Medir tensão de entrada",
            "Armazenar energia",
            "Multiplicar a tensão",
            "Converter AC em DC"
        ],
        [
            "O que faz o comando millis() no Arduino?",
            "Retorna o tempo em milissegundos desde o início do programa",
            "Pausa o programa por milissegundos",
            "Reinicia o Arduino",
            "Retorna o tempo em segundos",
            "Zera o contador de tempo"
        ],
        [
            "Qual sensor é adequado para detectar presença humana por movimento?",
            "PIR",
            "DHT11",
            "LDR",
            "HC-SR04",
            "BMP280"
        ],
        [
            "O que indica um LED acendendo em um circuito?",
            "Passagem de corrente e queda de tensão no LED",
            "Aumento de resistência",
            "Erro no circuito",
            "Baixa voltagem apenas",
            "Alta temperatura"
        ],
        [
            "Qual é a função do comando pinMode(pin, INPUT_PULLUP)?",
            "Ativar resistor pull-up interno",
            "Configurar pino como saída",
            "Ler valor analógico",
            "Gerar PWM no pino",
            "Desligar o pino"
        ],
        [
            "Qual componente é comumente usado para controlar cargas AC (como lâmpadas) em eletrônica de potência?",
            "Triac",
            "Transistor bipolar",
            "LED",
            "Relé reed",
            "Capacitor eletrolítico"
        ],
        [
            "Qual sensor é usado para medir a umidade do solo em projetos de irrigação?",
            "Sensor de umidade resistivo",
            "DHT11",
            "HC-SR04",
            "BMP280",
            "LDR"
        ],
        [
            "Qual componente converte tensão alternada (AC) em tensão contínua (DC)?",
            "Ponte retificadora (diodos)",
            "Transformador",
            "Capacitor eletrolítico",
            "Indutor",
            "Regulador linear"
        ],
        [
            "Qual comando envia dados pela Serial sem pular linha?",
            "Serial.print()",
            "Serial.println()",
            "Serial.read()",
            "Serial.begin()",
            "Serial.available()"
        ],
        [
            "Qual pino do Arduino UNO fornece 5V regulados?",
            "Pino 5V",
            "Pino 3.3V",
            "Pino GND",
            "Pino Vin",
            "Pino A0"
        ],
        [
            "Qual sensor é mais preciso que o DHT11 para temperatura e umidade?",
            "DHT22",
            "BMP280",
            "HC-SR04",
            "LDR",
            "MPU6050"
        ],
        [
            "Qual biblioteca facilita a comunicação I2C no Arduino?",
            "Wire.h",
            "SPI.h",
            "Servo.h",
            "Ethernet.h",
            "LiquidCrystal.h"
        ],
        [
            "Para que serve o botão RESET em uma placa Arduino?",
            "Reiniciar o microcontrolador",
            "Entrar no modo de bootloader permanentemente",
            "Limpar a EEPROM",
            "Ativar o modo de programação USB",
            "Forçar saída HIGH em todos os pinos"
        ],
        [
            "O que é um osciloscópio?",
            "Instrumento para visualizar formas de onda e sinais elétricos",
            "Fonte de alimentação regulada",
            "Sensor de movimento",
            "Conversor ADC",
            "Gerador de sinal apenas"
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