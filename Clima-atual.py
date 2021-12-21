import PySimpleGUI as SG
import requests
import json


# Tela do programa
SG.theme('Dark')

layout = [[SG.Text('Digite o nome da cidade: '), SG.Input()], [SG.Button('Buscar')],
          [SG.Button('Limpar')], [SG.Output(size=(60, 20), font=17, key='-OUTPUT-')]]

window = SG.Window("Clima Atual", layout, size=(370, 400), margins=(1, 1), finalize=True)


# Atulização das informações na tela
while True:
    event, values = window.read()
    if event == SG.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Buscar':
        key = "e914c292f53a903c6202d21e025fdc72"
        params = {'q': values[0], 'units': 'metric', 'appid': key}
        url = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
        if url.status_code == 200:
            text = url.text
            data = json.loads(text)
            user = data['main']
            print('Cidade: ', data['name'])
            print('Pais: ', data['sys']['country'])
            print('Temperatura: ', user['temp'], "C")
            print('Sensação térmica: ', user['feels_like'], "C")
            print('Umidade: ', user['humidity'], "%")
            print('Vento:', data['wind']['speed'], 'Km/h')
        else:
            print('Cidade nao encontrada')

    elif event == 'Limpar':
        window['-OUTPUT-'].update('')

    else:
        window.close()