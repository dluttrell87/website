#!/usr/bin/env python3
import PySimpleGUI as sg

class datastore:
    def __init__(self, x, y, z):
        self.usage = x
        self.request = y
        self.size = z


    #def getPercent(self):
    #    return (self.size-self.usage)/self.size*100

    # def getNewPercent(self):
    #    return (self.size-(self.usage+self.request))/self.size*100

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
        return targetsize-self.size


# Build PySimpleGUI window
sg.theme('DarkGrey7')
layout = [
    [sg.Text('Enter datastore information:', size=(35, 1), font='Tahoma')],[sg.Text()],
    [sg.Text('  Datastore Used:', font='Tahoma', size=(15,1)), sg.InputText(size=(15,1)), sg.Combo(('GB', 'TB'), enable_events=True, readonly=True, key='-uu-', default_value='GB')],
    [sg.Text('  Adding space:', font='Tahoma', size=(15, 1)), sg.InputText(size=(15,1)), sg.Combo(('GB', 'TB'), enable_events=True, readonly=True, key='-su-', default_value='GB')],
    [sg.Text('  Datastore Capacity:', font='Tahoma', size=(15, 1)), sg.InputText(size=(15,1)), sg.Combo(('GB', 'TB'), enable_events=True, readonly=True, key='-cu-', default_value='GB')],[sg.Text()],
    [sg.Text('Results:', font='Tahoma', size=(15,1))],[sg.Text()],
    [sg.Text('  Added Storage:', font='Tahoma', size=(15, 1)), sg.InputText(size=(15,1), key='-calculate-', readonly=True),
     sg.Combo(('GB', 'TB'), enable_events=True, readonly=True, key='-ru-', default_value='GB')],
    [sg.Text('  Datastore Capacity:', font='Tahoma', size=(15, 1)), sg.InputText(size=(15, 1), key='-calctotal-', readonly=True),
     sg.Combo(('GB', 'TB'), enable_events=True, readonly=True, key='-rtu-', default_value='GB')], [sg.Text(key='status',font='Tahoma', text_color='lime')], [sg.Text()],
    [sg.Button('Calculate', font='Tahoma', bind_return_key=True), sg.Cancel('Exit', font='Tahoma')]
]
window = sg.Window("Datastore Allocation", layout)


def validate(values):
    x = values[0]
    y = values[1]
    z = values[2]
    try:
        x = float(x)
        y = float(y)
        z = float(z)
        if str(values['-uu-']) == 'GB':
            x = x * 1
        else:
            x = x * 1024
        if str(values['-su-']) == 'GB':
            y = y * 1
        else:
            y = y * 1024
        if str(values['-cu-']) == 'GB':
            z = z * 1
        else:
            z = z * 1024
    except:
        return False
    if x < 0 or y < 0 or z < 0:
        return False
    if z == 0:
        return False
    if z < x:
        return False
    return True


# window event loop
while True:
    event, values = window.read()
    if event in ('Calculate', None) and (validate(values) is True):
        usage = float(values[0])
        request = float(values[1])
        size = float(values[2])
        if str(values['-uu-']) == 'GB':
            usage = usage*1
        else:
            usage = usage*1024
        if str(values['-su-']) == 'GB':
            request = request*1
        else:
            request = request*1024
        if str(values['-cu-']) == 'GB':
            size = size * 1
        else:
            size = size * 1024

        # create/update Datastore object
        Datastore = datastore(usage, request, size)

        if Datastore.needsExpansion() is True:
            window['status'].update(' ')
            if (str(values['-ru-']) == 'GB'):
                window['-calculate-'].update(float(Datastore.getGB()))
            elif (str(values['-ru-']) == 'TB'):
                window['-calculate-'].update(float(Datastore.getGB())/1024)
            if (str(values['-rtu-']) == 'GB'):
                window['-calctotal-'].update(float(Datastore.getTotal()))
            elif (str(values['-rtu-']) == 'TB'):
                window['-calctotal-'].update(float(Datastore.getTotal())/1024)
        elif Datastore.needsExpansion() is False:
            window['-calculate-'].update('N/A')
            window['-calctotal-'].update('N/A')
            window['status'].update('  Note: No expansion required')
        else:
            window['-calculate-'].update('Error')
            window['-calctotal-'].update('Error')
    else:
        window['status'].update(' ')
        window['-calculate-'].update(' ')
        window['-calctotal-'].update(' ')
    if event in ('Exit', None):
        break
