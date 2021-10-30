from machine import Pin, ADC, SoftI2C
from bmp180 import BMP180
import dht
from math import pi
from time import sleep, ticks_ms,ticks_diff,time

pin_ldr = 34 
pin_dht = 32
pin_bmp1= 22 #Pino SCL
pin_bmp2 = 21 #Pino SDA
pin_botao = 33

LDR = ADC(Pin(pin_ldr))
LDR.atten(ADC.ATTN_11DB)
DHT = dht.DHT11(Pin(pin_dht))
DHT.measure()
#BMP = I2C(Pin(pin_bmp1),Pin(pin_bmp2),freq=400000)

IC2 = SoftI2C(scl= Pin(pin_bmp1),sda=Pin(pin_bmp2))
BMP = BMP180(IC2)
temp_media = (BMP.temperature + DHT.temperature())/2

botao = Pin(pin_botao,Pin.IN)
momento1 = 0
momento2 = 0

def velocidade(duracao):
    distancia = 2*pi* 0.00009
    tempo = duracao*(1/3600000)
    return distancia/tempo
contador_t_init = time()
contador_t_fin = 0
contador_b = 0
while True:
    contador_t_fin += 1
    #print('contador_t:',contador_t)
    while (contador_t_fin-contador_t_init) < contador_+t_init + 5:
        if botao.value() == 1:
            contador_b +=1
            print('botao')
    
    while botao.value() == 1:
        momento1 = ticks_ms()
    #print('LDR: {}\nTemperatura: {:.2f}°C\nHumildade: {}%\nPressão: {}\nAltitude: {}m'.format(LDR.read(),temp_media,DHT.humidity(),BMP.pressure,int(BMP.altitude)))
    duracao = ticks_diff(momento1,momento2)
    #if duracao >0:
        #print('duracao=',duracao,'ms')
        #print(velocidade(duracao),'km/h')
    momento2 = momento1
    sleep (1)
