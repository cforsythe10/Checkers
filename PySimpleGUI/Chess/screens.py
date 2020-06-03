import PySimpleGUI as sg

class Windows:
    def DisplayAbout(self):
        sg.ChangeLookAndFeel('GreenTan')

        about_controls = [[sg.RButton('Back to Main', key='Main')]]

        layout = [[sg.Text('This game was made by Justin Roszko, Sam Platek, Chris Forsythe, and the other Robert Roche.\n\nInstructions for this game can be found at https://www.fgbradleys.com/rules/Checkers.pdf')],
                  [sg.Column(about_controls)]]

        window = sg.Window('About', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()
            print(button, value)

            if button in (None, 'Exit'):
                quit()

            if button == 'Main':
                window.Close()
                Windows.DisplayMain(self)

    def DisplayHostOrClient(self):

        sg.ChangeLookAndFeel('GreenTan')

        hostOrClient_controls = [[sg.RButton('Host', key='Host')],
                                 [sg.RButton('Client', key='Client')]]

        layout = [[sg.Column(hostOrClient_controls)]]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()

            if button == 'Host':
                window.Close()
                Windows.DisplayHost(self)

            if button == 'Client':
                window.Close()
                Windows.DisplayClient(self)


    def DisplayHost(self):

        sg.ChangeLookAndFeel('GreenTan')

        layout = [[sg.Text('Put the connection key here')]]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()

    def DisplayClient(self):

        sg.ChangeLookAndFeel('GreenTan')

        hostOrClient_controls = [[sg.RButton('Join', key='Join')]]

        layout = [[sg.InputText(default_text='Put host key here', key='Host Input')],
            [sg.Column(hostOrClient_controls)]]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()

            if button == 'Join':
                hostKey = value['Host Input']
                print(hostKey)

                window.Close()
                Windows.DisplayWinner(self, 'Everybody')

    def DisplayMain(self):

        sg.ChangeLookAndFeel('GreenTan')

        main_controls = [[sg.RButton('New Game', key='New Game')],
                     [sg.RButton('About', key='About')],
                     [sg.RButton('Exit', key='Quit')]]

        layout = [[sg.Column(main_controls)]]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()
            print(button)

            if button in (None, 'Exit'):
                break

            if button == 'Quit':
                quit()

            if button == 'About':
                window.Close()
                Windows.DisplayAbout(self)

            if button == 'New Game':
                window.Close()
                Windows.DisplayHostOrClient(self)

    def DisplayWinner(self, winner):
        #send winner as a parameter to this

        sg.ChangeLookAndFeel('GreenTan')

        main_controls = [[sg.RButton('Rematch', key='Rematch')],
                     [sg.RButton('Quit', key='Quit')]]

        layout = [[sg.Text(winner + ' wins!')],
            [sg.Column(main_controls)]]

        window = sg.Window('Main', default_button_element_size=(12, 1), auto_size_buttons=False).Layout(layout)

        while True:
            button, value = window.Read()

            if button == 'Rematch':
                #confirm that other player also selects this and initialize new game, if other user does not confirm use below code
                #window.Close()
                #Windows.DisplayMain(self)
                quit()

            if button == 'Quit':
                window.Close()
                Windows.DisplayMain(self)

Windows.DisplayMain(Windows)