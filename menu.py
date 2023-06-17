import PySimpleGUI as psg

psg.theme('DarkRed1')

menu = [
    [psg.Text('Pokédex')],
    [psg.Button('Ver pokémon')]
]

window = psg.Window('Menu Inicial', menu, element_justification='c')

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED: 
        break
    
window.close()