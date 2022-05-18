import PySimpleGUI as sg

layout = [
    []
]

window = sg.Window("Calculator", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSE:
        break

window.close()