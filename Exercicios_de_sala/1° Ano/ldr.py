from pyfirmata import Arduino, INPUT, OUTPUT, util, PWM

PORTA = 'COM4'
arduino = Arduino(PORTA)
ldr = 0
botao = 2
ligado = False

it = util.Iterator(arduino)
it.start()

arduino.digital[botao].mode = INPUT
arduino.analog[ldr].enable_reporting()


while True:
    estado = arduino.digital[botao].read()
    if estado == True and ligado == False:
        ligado = True
    elif ligado == True and estado == True:
        ligado = False

    if ligado == True:
        valor_ldr = str(arduino.analog[ldr].read())
        print("Valor da luminosidade: ", valor_ldr)
        arduino.pass_time(0.15)
    
    if ligado == False:
        print("Sistema desligado")
        arduino.pass_time(0.3)
        
    arduino.pass_time(0.1)
