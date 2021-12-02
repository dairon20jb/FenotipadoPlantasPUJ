# This file is executed on every boot (including wake-boot from deepsleep)
import os
import esp
#import webrepl
#webrepl.start()


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.ifconfig(('192.168.1.10','255.255.255.0','192.168.1.1','192.168.1.1'))
        sta_if.connect('Prueba_Tesis', 'tesisfenotipado')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
do_connect()