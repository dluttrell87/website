#!/usr/bin/env python3
import PySimpleGUI as sg

class datastore:
    def __init__(self, x, y, z):
        print('init called')
        self.usage = x
        self.request = y
        self.size = z


    def getPercent(self):
        return (self.size-self.usage)/self.size*100

    def getNewPercent(self):
        return (self.size-(self.usage+self.request))/self.size*100

    def needsExpansion(self):
        if (self.size-(self.usage+self.request))/self.size*100 < 20:
            return True
        else:
            return False


    def getTotal(self):
        totalsize = self.size
        while (totalsize-(self.usage+self.request))/totalsize*100 < 20:
            totalsize += 1
        return totalsize


    def getGB(self):
        targetsize = self.size
        while (targetsize-(self.usage+self.request))/targetsize*100 < 20:
            targetsize += 1
        return targetsize-size


sg.theme('DarkGrey7')

layout = [
    [sg.Text('Enter datastore information:', font='Tahoma')],
    [sg.Text('Current used space', font='Tahoma', size=(14, 1)), sg.InputText()],
    [sg.Text('How much to add', font='Tahoma', size=(14, 1)), sg.InputText()],
    [sg.Text('Current total', font='Tahoma', size=(14, 1)), sg.InputText()],
    [sg.Submit('Calculate', font='Tahoma', bind_return_key=True), sg.Cancel('Cancel', font='Tahoma')]
]

window = sg.Window("Datastore Allocation", layout)
event, values = window.read()
window.close()

usage = int(values[0])
request = int(values[1])
size = int(values[2])

Datastore = datastore(usage, request, size)

if Datastore.needsExpansion() is True:
    layout = [
        [sg.Text("Increase datastore by:", font='Tahoma')],
        [sg.InputText(Datastore.getGB(), font='Tahoma')],
        [sg.Text("Datastore total size should be:", font='Tahoma')],
        [sg.InputText(Datastore.getTotal(), font='Tahoma')],
        [sg.Submit("OK", font='Tahoma', bind_return_key=True)]
    ]

    window = sg.Window("Results", layout)
    event, values = window.read()
    window.close()
else:
    print("test")
    layout = [
        [sg.Text("No increase necessary", font='Tahoma')],
        [sg.Text("New Percent used:", font='Tahoma')],
        [sg.InputText(Datastore.getNewPercent(), font='Tahoma')],
        [sg.Submit("OK", font='Tahoma', bind_return_key=True)]
    ]

    window = sg.Window("Results", layout)
    event, values = window.read()
    window.close()
