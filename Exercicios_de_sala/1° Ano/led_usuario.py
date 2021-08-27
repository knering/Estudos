from pyfirmata import Arduino, OUTPUT

arduino = Arduino('COM4')
arduino.digital[13].mode = OUTPUT
action = ""
entradas = ['Acender','Apagar','Piscar']

try:
    while action == "":
        try:
            action = input("Qual ação deseja executar? (Acender, Apagar, Piscar): ")
            if action not in entradas:
                print("Erro! Digite uma das opções listadas")
                action = ""
        except:
            print("Erro! Digite uma das opções listadas")
    while True:
        if action == "Acender":
            arduino.digital[13].write(1)
        elif action == "Apagar":
            arduino.digital[13].write(0)
        elif action == "Piscar":
            arduino.digital[13].write(1)
            arduino.pass_time(0.5)
            arduino.digital[13].write(0)
            arduino.pass_time(0.5)   

except KeyboardInterrupt:
    arduino.exit()