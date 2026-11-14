"""
@package Led
Modulo di gestione di un Led
"""
from machine import Pin
from time import sleep_ms

class Led:
    """
    Classe che rappresenta un led gestito senza PWM
    """
    def __init__(self,pin):
        """!
        @brief Inizializza un led associato ad un pin di GPIO
        @param[in] pin Pin di GPIO cui è collegato il led
        @pre pin Deve essere un pin esistente dell'ESP32 adatto all'output digitale
        """
        self.led = Pin(pin,Pin.OUT)
    

    def on(self):
        """!
        @brief Accende il led
        """
        self.led.value(1)
    
    def off(self):
        """!
        @brief Spegne il led
        """
        self.led.value(0)
    
    def blink(self,time, k):
        """!
        @brief Fa lampeggiare per k volte il led. Il tempo di accessione è di time ms
        @param[in] time Tempo di on in ms
        @param[in] k (int) Il numero di lampeggi da fare.
        @pre time Deve essere >= 0
        """
        for i in range(k):
            self.on()
            sleep_ms(time)
            self.off()
            sleep_ms(10)
