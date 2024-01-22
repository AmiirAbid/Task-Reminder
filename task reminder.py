import os
import time
import PySimpleGUI as sg

path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'tasks.txt')

def add_task(task) :
    with open(path, 'a') as f :
        f.writelines(task+'\n')

def remove_task(r) :
    with open(path, 'r') as f :
        lines = f.readlines()

    with open(path, 'w') as f :
        for number, line in enumerate(lines) :
            if number != int(r)-1 :
                f.write(line)

sg.theme('DarkBlue')

while True:
    if os.path.exists(path) == False :
        with open(path, 'x') as f :
            continue

    else :
        with open(path, 'r') as f :
            tasks = f.read()

    layout = [  [sg.Text('Your Tasks :')],
            [sg.Text(tasks) if tasks!="" else sg.Text("You have no tasks")],
            [sg.Button('Add Task'), sg.Button('Remove Task')]]

    layout1 = [  [sg.Text('Enter your task:')],
            [sg.InputText()],
            [sg.Button('Add'), sg.Button('Close')] ]

    layout2 = [  [sg.Text('Enter task number to remove')],
            [sg.InputText()],
            [sg.Button('Remove'), sg.Button('Close')] ]

    window = sg.Window('Tasks Reminder', layout)
    event, values = window.read()

    if event == sg.WIN_CLOSED :
        window.close()

    elif event == 'Add Task' :
        window.close()
        window1 = sg.Window('Add Task', layout1)
        while True:
            event, values = window1.read()
            if event == 'Close' or 'Add' :
                window1.close()
            add_task(values[0])
            break

    elif event == 'Remove Task' :
        window.close()
        window2 = sg.Window('Remove Task', layout2)
        while True:
            event, values = window2.read()
            if event == 'Close' or 'Remove':
                window2.close()
            remove_task(values[0])
            break

    time.sleep(1800)