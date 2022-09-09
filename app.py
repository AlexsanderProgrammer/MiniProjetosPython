
import PySimpleGUI as sg
import random as rd


sg.theme('Black')
#LAYOUT PYSIMPLEGUI
layoult = [
            [sg.Text('Digite seu nome:')],
            [sg.Input(key = 'nome')],
            [sg.Button('Gerar Código')],
            [sg.Text('Digite o código:')],
            [sg.Input(key = 'codigo')],
            [sg.Text('', key='mensagem')],
            [[sg.Button('Logar'),sg.Button('cancelar')]]
        ]

janela = sg.Window('One-Time-Password',layoult)
while True:
   

    evento,valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'cancelar':
        break

    if evento == 'Gerar Código':
        gerador = str(rd.randint(000000,100000))
        sg.Popup('Seu código de acesso é: ',gerador)
    
    if evento == 'Logar':
        codigo = valores['codigo']
        if codigo == gerador:
            sg.Popup('Bem Vindo!', valores['nome'])
        else:
            sg.Popup('Código invalido, Tente novamente!')
janela.close()
    
