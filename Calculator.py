import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(button_element_size=(6, 3), auto_size_buttons=False, font="Arial 14")
    layout = [
        [sg.Text("0", key="-TEXT-", font="Arial 20", justification="right", expand_x=True, pad=(10, 20), right_click_menu=theme_menu)],
        [sg.Button("Clear", expand_x=True), sg.Button("Enter", expand_x=True)],
        [sg.Button(7), sg.Button(8), sg.Button(9), sg.Button("*")],
        [sg.Button(4), sg.Button(5), sg.Button(6), sg.Button("/")],
        [sg.Button(1), sg.Button(2), sg.Button(3), sg.Button("-")],
        [sg.Button(0, expand_x=True), sg.Button("."), sg.Button("+")]
    ]
    return sg.Window("Calculator", layout)


theme_menu = ["menu", ["LightGray", "dark", "DarkGray", "DarkAmber", "random"]]
window = create_window("LightGray")

curr_num = []
full_operation = []

def get_curr_num():
    return "".join(curr_num)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event.isnumeric() or event == ".":
        curr_num.append(event)
        window["-TEXT-"].update(get_curr_num())

    if event in "+-*/":
        full_operation.append(get_curr_num())
        curr_num.clear()
        full_operation.append(event)
        window["-TEXT-"].update(get_curr_num())

    if event == "Enter":
        full_operation.append(get_curr_num())
        result = eval("".join(full_operation))
        window["-TEXT-"].update(result)
        full_operation.clear()
        curr_num.clear()
        curr_num.append(str(result))

    if event == "Clear":
        curr_num.clear()
        full_operation.clear()
        window["-TEXT-"].update(get_curr_num())

window.close()