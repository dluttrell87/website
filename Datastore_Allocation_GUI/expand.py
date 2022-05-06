#!/usr/bin/env python3
class ExpandDatastore:
    import PySimpleGUI as sg

    def __init__(self, x, y, z):
        self.size = x
        self.usage = y
        self.request = z
        self.layout = []
        self.event, self.values = [0, 0]
        self.window = []
        self.update_window()

    def needs_expansion(self):
        if (self.size-(self.usage+self.request))/self.size*100 <= 20:
            return True
        else:
            return False

    def get_total(self):
        if (self.usage + self.request) >= (.80*self.size):
            return (self.usage+self.request)*1.25
        else:
            return "N/A"

    def calc_expand(self):
        if (self.usage + self.request) >= (.80*self.size):
            return ((self.usage+self.request)*1.25) - self.size
        else:
            return "N/A"

    def get_usable(self):
        if (self.usage + self.request) < (.80*self.size):
            return round(((.80*self.size) - (self.usage + self.request)), 5)
        else:
            return "N/A"

    def create_window(self):
        expand_datastore_image = "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"
        # Build PySimpleGUI window
        self.sg.theme('DarkBlue13')
        self.layout = [
            [self.sg.Frame(layout=[[self.sg.Image(data=expand_datastore_image),
             self.sg.Text('Expand Datastore', font=('Helvetica', 20), size=(20, 1))],
            [self.sg.Text('  Datastore Capacity:', font='Helvetica', size=(20, 1)), self.sg.InputText('0', size=(15, 1)),
             self.sg.Combo(('GiB', 'TiB'), enable_events=True, readonly=True, key='-cu-', default_value='GiB')],
            [self.sg.Text('  Datastore Used:', font='Helvetica', size=(20, 1)), self.sg.InputText('0', size=(15, 1)),
             self.sg.Combo(('GiB', 'TiB'), enable_events=True, readonly=True, key='-uu-', default_value='GiB')],
            [self.sg.Text('  *Requested Amount:', font='Helvetica', size=(20, 1)), self.sg.InputText('0', size=(15, 1)),
             self.sg.Combo(('GiB', 'TiB'), enable_events=True, readonly=True, key='-su-', default_value='GiB')],
            [self.sg.Text('*Note: Requested Amount is before overhead')],
            [self.sg.Button('Calculate', font='Helvetica', pad=(15), mouseover_colors='#06193d', bind_return_key=True),
             self.sg.Button('Exit', mouseover_colors='#06193d', font='Helvetica')],
            [self.sg.Text('_______________________________________________________________________', pad=0)],
            [self.sg.Text(' Assuming 20% overhead')],

            [self.sg.Text('  Available Storage:', font='Helvetica', size=(20, 1)),
             self.sg.InputText(size=(15, 1), key='-calcusable-', readonly=True, disabled_readonly_background_color='grey',
                               text_color='black'),
             self.sg.Combo(('GiB', 'TiB'), enable_events=True, readonly=True, key='-rs-', default_value='GiB')],
            [self.sg.Text('  Request Storage:', font='Helvetica', size=(20, 1)),
             self.sg.InputText(size=(15, 1), key='-calculate-', readonly=True, disabled_readonly_background_color='grey',
                               text_color='black'),
             self.sg.Combo(('GiB', 'TiB'), enable_events=True, readonly=True, key='-ru-', default_value='GiB')],
            [self.sg.Text('  New Datastore Capacity:', font='Helvetica', size=(20, 1)),
             self.sg.InputText(size=(15, 1), key='-calctotal-', readonly=True, disabled_readonly_background_color='grey',
                               text_color='black'),
             self.sg.Combo(('GiB', 'TiB'), enable_events=True, readonly=True, key='-rtu-', default_value='GiB')],
            [self.sg.Text(key='status', font='Helvetica')], [self.sg.Text()]], title='', pad=1, relief=self.sg.RELIEF_RAISED)],
        ]

    def update_window(self):
        # window event loop
        self.create_window()
        self.window = self.sg.Window("Expand Datastore", self.layout, use_custom_titlebar=True, titlebar_icon='', titlebar_background_color='#06193d', grab_anywhere=True)
        while True:
            self.event, self.values = self.window.read()
            if self.event == self.sg.WIN_CLOSED or self.event == 'Exit':  # Breaks the loop if exit is triggered
                self.window.close()
                break
            if self.event in ('Calculate', None) and (self.validate() is True):
                self.size = float(self.values[1])
                self.usage = float(self.values[2])
                self.request = float(self.values[3])
                # convert values depending on unit
                if str(self.values['-cu-']) == 'GiB':
                    self.size = self.size * 1
                else:
                    self.size = self.size * 1024
                if str(self.values['-uu-']) == 'GiB':
                    self.usage = self.usage*1
                else:
                    self.usage = self.usage*1024
                if str(self.values['-su-']) == 'GiB':
                    self.request = self.request*1
                else:
                    self.request = self.request*1024
                # create/update Datastore object

                if self.needs_expansion() is True:
                    self.window['status'].update(' ')
                    self.window['-calcusable-'].update('N/A')
                    if str(self.values['-ru-']) == 'GiB':
                        self.window['-calculate-'].update(float(round(self.calc_expand(),5)))
                    elif str(self.values['-ru-']) == 'TiB':
                        self.window['-calculate-'].update(float(round((self.calc_expand()/1024),5)))
                    if str(self.values['-rtu-']) == 'GiB':
                        self.window['-calctotal-'].update(float(round(self.get_total(),5)))
                    elif str(self.values['-rtu-']) == 'TiB':
                        self.window['-calctotal-'].update(float(round((self.get_total()/1024),5)))
                elif self.needs_expansion() is False:
                    if str(self.values['-rs-']) == 'GiB':
                        self.window['-calcusable-'].update(float(round(self.get_usable(),5)))
                    elif str(self.values['-rs-']) == 'TiB':
                        self.window['-calcusable-'].update(float(round((self.get_usable()/1024),5)))
                    self.window['-calculate-'].update('N/A')
                    self.window['-calctotal-'].update('N/A')
                    self.window['status'].update('  Note: No expansion required', text_color='lime')
            else:
                self.window['status'].update(' ')
                self.window['-calculate-'].update('N/A')
                self.window['-calctotal-'].update('N/A')
                self.window['-calcusable-'].update('N/A')

            if self.event in ('Exit', None):
                self.window.close()
                break

    def validate(self):
        x = self.values[1]
        print(x)
        y = self.values[2]
        print(y)
        z = self.values[3]
        print(z)
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            if str(self.values['-cu-']) == 'GiB':
                x = x * 1
            else:
                x = x * 1024
            if str(self.values['-uu-']) == 'GiB':
                y = y * 1
            else:
                y = y * 1024
            if str(self.values['-su-']) == 'GiB':
                z = z * 1
            else:
                z = z * 1024
        except:
            return False
        if x < 0 or y < 0 or z < 0:
            return False
        if x == 0:
            return False
        if x < y:
            return False
        return True


def expand():
    datastore = ExpandDatastore(0, 0, 0)




