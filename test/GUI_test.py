import PySimpleGUI as sg
import os.path
sg.theme('DarkGrey7')
#sg.Window(title="poop", layout=[[]], margins=(100, 50)).read()

layout = [
    [sg.Text('Enter datastore information:')],
    [sg.Text('Current used space', size=(15, 1)), sg.InputText()],
    [sg.Text('How much to add', size=(15, 1)), sg.InputText()],
    [sg.Text('Current total', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window("Datastore Allocation", layout)
event, values = window.read()


window.close()

layout = [
    [sg.Text("Increase datastore by")],
    [sg.Text(values[0])]
]

window = sg.Window("Results", layout)
event, values = window.read()