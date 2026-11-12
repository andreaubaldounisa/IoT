"""!
@package LedPWM
Modulo per la gestione di un Led con PWM
"""
from machine import Pin, PWM
from time import sleep_ms

class LedPWM:
    """!
    @brief Classe per la gestione di un Led con PWM
    """
    def __init__(self,pin):
        """!
        @brief Costruttore di un Led da gestire col PWM
        @param[in] pin Pin dell'ESP32 cui è collegato il Led
        """
        self.led = PWM(Pin(pin,Pin.OUT))
        self.led.freq(5000) #Frequenza operativa del led per evitare sfarfalli e sprechi energetici
    
    def on(self,duty):
        """!
        @brief Accende il led con una luminosità decisa dal duty cycle
        @param[in] duty Duty cycle = (on_time/period) del led. Da esso dipende la tensione media cui è soggetto il led
        @pre duty Deve essere compreso tra 0 e 1023
        """
        self.led.duty(duty)
        
    def off(self):
        """!
        @brief Spegne il led
        """
        self.led.duty(0)
    
    def blink(self,time,k,duty):
        """!
        @brief Fa lampeggiare (col duty cycle specificato) il led per k volte mantendolo acceso per time ms
        @param[in] duty Duty cycle = (on_time/period) del led. Da esso dipende la tensione media cui è soggetto il led
        @param[in] time Quanto tempo il led deve rimanere acceso in ms
        @param[in] k Quanti lampeggi far fare al led
        @pre duty Deve essere compreso tra 0 e 1023
        """
        for i in range(k):
            self.on(duty)
            sleep_ms(time)
            self.off()
            sleep_ms(10)

        