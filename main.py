value = 0
lista = [1,2,3]
lista = []

def on_button_pressed_a():
    global value
    value+=1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global value
    lista.append(value)
    value = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global lista
    basic.show_string("Cresc")
    for i in range(0,lista.length):
        basic.show_number(lista[i])
    basic.show_string("Invers")
    for i in range(0,lista.length):
        basic.show_number(lista[lista.length - i - 1])
input.on_button_pressed(Button.AB, on_button_pressed_ab)
