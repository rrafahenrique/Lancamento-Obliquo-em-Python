from tkinter import*
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox
from tkinter.font import *

#Constantes
#Ponto de Lançamento
x_inicial = 30
y_inicial = 300

#Pega os valores iniciais   
def aceitar():

    erro = False

    try:
        vel_inicial = float(texto1.get())
    except:
        erro = True
    if erro or vel_inicial <= 0:
        assinalar_erro(texto1)

    try: 
        angulo = float(texto2.get())
    except: 
        erro = True
    if erro or angulo <= 0:
        assinalar_erro(texto2)

    angulo = angulo*np.pi/180

    return vel_inicial, angulo

#Movimento da simulação
def mover():
    global t, run

    vel, ang = aceitar()
    g = 9.8
    dt = 0.1
    vel_x = vel*np.cos(ang)
    vel_y = vel*np.sin(ang)
    x = x_inicial + vel_x*t
    y = y_inicial - vel_y*t + ((g*(t**2))/2)

    if run:
        if y > 300:
           y = 300
           run = False
        t += dt
        tela.coords(bola, x - 10, y - 10, x + 10, y + 10)
        JANELA.after(25, mover)

    return vel_x, vel_y

#Condição de inicio da simulação
def andar():
    global start, run

    if not start:
        aceitar()
        start = True
    if not run:
        run = True
        mover()

#Reseta a posição da bola e permite uma nova realizar uma nova simulação
def reiniciar():
    global start, run, t

    start = False
    run = False
    t = 0
    num1.set("")
    num2.set("")
    tela.coords(bola, x_inicial - 10, y_inicial - 10, x_inicial + 10, y_inicial + 10)

#Função para fazer o gráfico da trajetoria
def grafico1():
    
    vel, ang = aceitar()
    vx, vy = mover()

    g = 9.8
    dt = 0.1    
    tempoTotal = 2*vel*np.sin(ang)/g
    t = np.arange(0, tempoTotal, dt)

    x = x_inicial + abs(vx)*t
    y = y_inicial + abs(vy)*t - ((g*(t**2))/2)    
    
    plt.title("Trajetória do Projétil")
    plt.xlabel("Distância (m)")
    plt.ylabel("Altura (m)")

    plt.plot(x, y)
    plt.show()   

def assinalar_erro(dado):
    dado.update()
    messagebox.showerror("ATENÇÃO", "Você inseriu um valor inválido!"
                        "\nVerifique se os valores digitados estão de acordo com o fenômeno físico." 
                        "\nPor Favor, clique em REINICIAR e tente novamente")

    dado.after(100, dado.delete(0, len(dado.get())))

#Cria janela
JANELA = Tk()
#Título da Janela
JANELA.title("Lançamento de Projétil")
#Dimensiona o tamanho da Janela
JANELA.geometry("835x470")
#Bloqueia o usuário de mexer no tamanho da tela 
JANELA.resizable(False, False)

letra_fonte = Font(family = "Arial", size = 10)

#Cria a área onde a simulação acontecerá 
tela = Canvas(JANELA, width = 600, height = 400, bg = 'white')
tela.grid(row = 0, column = 0)

#Desenha o chão e a bola
tela.create_rectangle(0, y_inicial + 10, 0 + 600, y_inicial + 100, fill = 'darkgreen')
bola = tela.create_oval(x_inicial - 10, y_inicial - 10, x_inicial + 10, y_inicial + 10, width = 2, fill = 'red')

#=====================BLOCO 1===========================
'''
            ==========================
            Área para inserir os dados
            ==========================
'''
area_dados = Frame(JANELA)
area_dados.grid(row = 1, column = 0, sticky = E+W+N)
area_dados.config(relief = "ridge")
area_dados.config(bd = 10)

#Variaveis (Velocidade Inicial e Ângulo)
num1 = StringVar()
num2 = StringVar()

#Cria o espaço para digitar os dados (Velocidade Inicial e Angulo)
texto1 = Entry(area_dados, textvariable = num1, width = 15, justify = "center")
texto1.grid(row = 0, column = 1, padx = 10, pady = 10)

texto2 = Entry(area_dados, textvariable = num2, width = 15, justify = "center")
texto2.grid(row = 0, column = 3, padx = 10, pady = 10)

#Cria o espaço das legenda (Velocidade Inicial e Angulo)
legenda1 = Label(area_dados, text = "Velocidade Inicial (m/s): ", font = letra_fonte)
legenda1.grid(row = 0, column = 0, sticky = E+W+S+N, padx = 10, pady = 10)

legenda2 = Label(area_dados, text = "Ângulo Inicial (graus): ", font = letra_fonte)
legenda2.grid(row = 0, column = 2, sticky = E+W+S+N, padx = 10, pady = 10)

#==================BLOCO 2========================
'''
            ========================
            #Área dos Botões de Ação
            ========================
'''

area_botao = Frame(JANELA)
area_botao.grid(row = 0, column = 1, sticky = E+W+N)
area_botao.config(relief = "ridge")
area_botao.config(bd = 10)

botao_executar = Button(area_botao, text = 'Executar', font = letra_fonte, command = andar, width = 22, height = 2)
botao_executar.grid(row = 0, column = 0, sticky = E+W+S+N, padx = 5, pady = 5)

botao_reiniciar = Button(area_botao, text = 'Reiniciar', font = letra_fonte, command = reiniciar, width = 22, height = 2)
botao_reiniciar.grid(row = 1, column = 0, sticky = E+W+S+N, padx = 5, pady = 5)

botao_grafico1 = Button(area_botao, text = 'Gráfico', font = letra_fonte, command = grafico1, width = 22, height = 2)
botao_grafico1.grid(row = 2, column = 0, sticky = E+W+S+N, padx = 5, pady = 5)

botao_sair = Button(area_botao, text = 'Sair', font = letra_fonte, command = JANELA.destroy, width = 22, height = 2)
botao_sair.grid(row = 3, column = 0, sticky = E+W+S+N, padx = 5, pady = 5)
reiniciar()

#Executa o Loop
JANELA.mainloop()