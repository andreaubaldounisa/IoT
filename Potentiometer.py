"""!
@package Potentiometer
Modulo per la gestione di un potenziometro
"""
from machine import Pin, ADC

class Potentiometer:
    """!
    @brief Classe per la gestione di un potenziometro
    """
    def __init__(self,pin):
        """!
        @brief Costruisce un potenziometro.
        @param[in] pin Pin dell'ESP32 cui è associato il potenziometro
        @pre pin Deve essere un pin esistente dell'ESP32 e deve essere adatto alla lettura tramite ADC
        """
        self.potentiometer = ADC(Pin(pin,Pin.IN))
        self.potentiometer.atten(ADC.ATTN_11DB) #Legge da 0.0 a 3.3V
    
    def read(self):
        """!
        @brief Legge il valore di tensione del potenziometro
        @return valore(int) Valore letto dal potenziometro [0,4095]
        """
        return int(self.potentiometer.read())
    
    def value(self,min_value,max_value):
        """!
        @brief Legge il valore di tensione del potenziometro e lo restituisce normalizzato
        @param[in] min_value Valore minimo dell'intervallo
        @param[in] max_value Valore massimo dell'intervallo
        @pre min_value Deve essere <= max_value
        @return valore(int) Valore del potenziometro normalizzato tra [min_value,max_value]
        """
        valore_adc = self.read()
        valore_normalizzato = int(min_value + valore_adc * (max_value - min_value) / 4095)
        return valore_normalizzato