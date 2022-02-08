import PySimpleGUIWeb as sg

def main():
    layout = [
        [sg.Text('Input text to leet')],
        [sg.Input('', size=(30,1), key='_TEXT_')],
        [sg.Text(key='_RESULT_')],
        [sg.Ok(), sg.Cancel()]
    ]

    window = sg.Window('Leet Converter', layout)
    i = 0
    while True:
        event, values = window.read(timeout=1)
        if event == 'Ok':
            text = window['_TEXT_'].get()
            string_list = []
            edited_text = ''
            dictionary = {'E':'3','e':'3','l':'1','L':'1','t':'7', 'T':'7','a':'4','A':'4','s':'5','S':'5',' ': ''}
            for x in text:
                if dictionary.get(x):
                    char = dictionary.get(x)
                    string_list.append(char)
                else:
                    string_list.append(x.upper())

            edited_text = edited_text.join(string_list)
            window['_RESULT_'].update(edited_text)
        if event == 'Cancel':
            window['_TEXT_'].update('')
            window['_RESULT_'].update('')
        if event != sg.TIMEOUT_KEY:
            print(event, values)
        i += 1

main()