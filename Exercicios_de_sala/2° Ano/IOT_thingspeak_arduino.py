
""" Código de comunicação entre arduino e Thingspeak, lendo valores e monitorando por LED """

import requests
from time import sleep
from pyfirmata import Arduino, util, OUTPUT
import random

def enviar_dado(): #Ou fake_iot.py, para os íntimos
    key_write = ''
    temp = round(random.uniform(0,40),1)
    umidade = random.randint(0,100)
    requests.get('https://api.thingspeak.com/update?api_key='+key_write+'&field1='+str(temp)+'&field2='+str(umidade))

def coletar_dados():
    key_read = ''
    server_return = requests.get('https://api.thingspeak.com/channels/1504510/feeds.json?api_key='+key_read+'&results=2')
    retorno_json = server_return.json()
    var1 = float(retorno_json['feeds'][0]['field1'])
    var2 = int(retorno_json['feeds'][0]['field2'])
    return [var1, var2]

def led_temperatura():
    if (temp >= 0 and temp <=15):
        led_vermelho_temp.write(0)
        led_amarelo_temp.write(0)
        led_verde_temp.write(1)
        print('Temperatura baixa', temp, '°C')
        
    elif (temp > 15 and temp <= 30):
        led_vermelho_temp.write(0)
        led_amarelo_temp.write(1)
        led_verde_temp.write(0)
        print('Temperatura média', temp, '°C')
        
    elif (temp > 30):
        led_vermelho_temp.write(1)
        led_amarelo_temp.write(0)
        led_verde_temp.write(0)
        print('Temperatura alta', temp, '°C')
        
def led_umidade():
    if (umidade >= 0 and umidade <=50):
        led_vermelho_umid.write(1)
        led_amarelo_umid.write(0)
        led_verde_umid.write(0)
        print('Umidade baixa', umidade, '%')
        
    elif (umidade > 50 and umidade <= 75):
        led_vermelho_umid.write(0)
        led_amarelo_umid.write(1)
        led_verde_temp.write(0)
        print('Umidade média', umidade, '%')
        
    elif (umidade > 75):
        led_vermelho_umid.write(0)
        led_amarelo_umid.write(0)
        led_verde_umid.write(1)
        print('Umidade Boa', umidade, '%')


""" Configuração do arduino """

PORTA = '' #especificar_porta_serial
arduino = Arduino(PORTA) #Inserir porta
it = util.Iterator(arduino)
it.start()

#Pinos LED
led_vermelho_temp = arduino.digital[2]
led_amarelo_temp = arduino.digital[3]
led_verde_temp = arduino.digital[4]
led_vermelho_umid = arduino.digital[5]
led_amarelo_umid = arduino.digital[6]
led_verde_umid = arduino.digital[7]

#Entradas LED
led_vermelho_temp.mode = OUTPUT
led_amarelo_temp.mode = OUTPUT
led_verde_temp.mode = OUTPUT
led_vermelho_umid.mode = OUTPUT
led_amarelo_umid.mode = OUTPUT
led_verde_umid.mode = OUTPUT


while True:
    enviar_dado()
    
    temp = coletar_dados()[0]
    umidade = coletar_dados()[1]
    
    led_temperatura()
    
    led_umidade()
    
    sleep(60) 