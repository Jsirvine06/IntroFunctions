import PySimpleGUI as sg

cp = sg.cprint

def main():

    layout = [  [sg.Text('Output Area - Calculations here.', font='Any 15')],
                [sg.Multiline(size=(65,10), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True)],
                [sg.T('Input 2 numbers then select the calculation you would like to perform.')],
                [sg.Input(size=(30,1)), sg.Input(size=(30,1))],
                [sg.B('+'), sg.B('-'), sg.B('*'), sg.B('/'), sg.Button('Exit')]  ]

    window = sg.Window('Calculator', layout, icon='Images/cal.ico', finalize=True)

    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event.startswith('+'):
            cp(f'{int(values[0]) + int(values[1])}', colors='white on red')
        if event.startswith('-'):
            cp(f'{int(values[0]) - int(values[1])}', colors='white on red')
        if event.startswith('*'):
            cp(f'{int(values[0]) * int(values[1])}', colors='white on red')
        if event.startswith('/'):
            cp(f'{int(values[0]) / int(values[1])}', colors='white on red')
    window.close()

if __name__ == '__main__':
    main()