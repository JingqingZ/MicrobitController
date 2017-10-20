let accx = 0
let accy = 0
let accz = 0
basic.forever(() => {
    accx = input.acceleration(Dimension.X)
    accy = input.acceleration(Dimension.Y)
    accz = input.acceleration(Dimension.Z)
    serial.writeLine("{'x':" + accx + ", 'y':" + accy + ", 'z':" + accz + "}")
    let ledx = map2led(accx)
    let ledy = map2led(accy)
    led.plot(ledx, ledy)
    basic.pause(300)
    led.unplot(ledx, ledy)
})

control.inBackground(() => {
    while (1) {
        let ba = input.buttonIsPressed(Button.A)
        let bb = input.buttonIsPressed(Button.B)
        if (ba) {
            serial.writeLine("{'button': 'A'}")
        }
        if (bb) {
            serial.writeLine("{'button': 'B'}")
        }
        basic.pause(10)
    }
})

input.onButtonPressed(Button.AB, () => {
    serial.writeLine("{'button': 'AB'}")
})

function map2led(x: number) {
    return (x + 1024) / 410
}

