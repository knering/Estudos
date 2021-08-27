from pyfirmata import Arduino, OUTPUT

PORTA = 'COM4'

arduino = Arduino(PORTA)
arduino.digital[13].mode = OUTPUT
arduino.digital[12].mode = OUTPUT
try:
    while True:
        arduino.digital[13].write(1)
        arduino.digital[12].write(0)
        arduino.pass_time(0.5)
        arduino.digital[13].write(0)
        arduino.digital[12].write(1)
        arduino.pass_time(0.5)

except KeyboardInterrupt:
    arduino.exit()