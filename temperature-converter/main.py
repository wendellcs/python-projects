import tkinter as tk

from converter import Converter
c = Converter()

def calculate():
    if not isNumber(entry1.get()):
        configLabel('Please enter a valid number.')
        return
    
    x = float(entry1.get())

    op1 = optionV.get()
    op2 = optionVSec.get()

    if(op1 == op2):
        configLabel('Please select different units.')
        return

    if op1 == 'Celsius':
        if op2 == 'Fahrenheit':
            configLabel(f'{c.celsius_to_fahrenheit(x)}F°')
        elif op2 == 'Kelvin':
            configLabel(f'{c.celsius_to_kelvin(x)}K')

    elif op1 == 'Fahrenheit':
        if op2 == 'Celsius':
            configLabel(f'{c.fahrenheit_to_celsius(x)}C°')
        elif op2 == 'Kelvin':
            configLabel(f'{c.fahrenheit_to_kelvin(x)}K')

    elif op1 == 'Kelvin':
        if op2 == 'Celsius':
            configLabel(f'{c.kelvin_to_celsius(x)}C°')
        elif op2 == 'Fahrenheit':
            configLabel(f'{c.kelvin_to_fahrenheit(x)}F°')

def isNumber(num):
    try: 
        float(num)
        return True 
    except ValueError:
        return False

def configLabel(msg):
    label.config(text = msg)

# UI

root = tk.Tk()
root.title('Temperature Converter')

options = [
    'Celsius',
    'Fahrenheit',
    'Kelvin'
]

# Selects
optionV = tk.StringVar(root)
optionV.set(options[0])

firstSelect = tk.OptionMenu(root, optionV, *options)
firstSelect.grid(row = 0, column = 0, pady = 10, padx = 15)

optionVSec = tk.StringVar(root)
optionVSec.set(options[1])

secondSelect = tk.OptionMenu(root, optionVSec, *options)
secondSelect.grid(row = 0, column = 1, pady = 10, padx = 15)

# Inputs
entry1 = tk.Entry(root, width = 10)
entry1.grid(row = 1, column = 0, pady = 10, padx = 15)

label = tk.Label(root)
label.grid(row = 1, column = 1)

button = tk.Button(root, text='Calculate', command=calculate)
button.grid(row = 2 , column = 0)

root.mainloop()