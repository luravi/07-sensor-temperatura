let temp = 0
basic.forever(function () {
    // Bucle que muestra la temperatura cada segundo
    temp = input.temperature()
    basic.showString("" + temp + "C")
    basic.pause(1000)
})
