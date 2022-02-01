let value = 0
let lista = [1, 2, 3]
lista = []
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    value += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    lista.push(value)
    value = 0
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    let i: number;
    
    basic.showString("Cresc")
    for (i = 0; i < lista.length; i++) {
        basic.showNumber(lista[i])
    }
    basic.showString("Invers")
    for (i = 0; i < lista.length; i++) {
        basic.showNumber(lista[lista.length - i - 1])
    }
})
