"""!
@package LDR
Modulo per la gestione di un Light Dependent Resistor
"""
from machine import Pin, ADC

class LDR:
    """!
    @brief Classe per la gestione di un fotoresistore
    """
    def __init__(self,pin):
        """!
        @brief Costruisce un fotoresistore
        @param[in] pin Pin dell'ESP32 cui è associato il fotoresistore
        @pre pin Deve essere un pin esistente dell'ESP32 e deve essere adatto alla lettura tramite ADC
        """
        self.ldr = ADC(Pin(pin,Pin.IN))
        self.ldr.atten(ADC.ATTN_11DB) #Attenuazione adatta al confronto con i 3.3V
        
    def read(self):
        """!
        @brief Legge il valore di tensione del LDR
        @return valore(int) Valore letto da potenziometro [0,4095]
        """
        return int(self.ldr.read())

    def value(self,min_value,max_value):
        """!
        @brief Legge il valore di tensione del fotoresistore e lo restituisce normalizzato
        @param[in] min_value Valore minimo dell'intervallo
        @param[in] max_value Valore massimo dell'intervallo
        @pre min_value Deve essere <= max_value
        @return valore(int) Valore del fotoresistore normalizzato tra [min_value,max_value]
        """
        valore_adc = self.read()
        valore_normalizzato = int(min_value + valore_adc * (max_value - min_value) / 4095)
        return int(valore_normalizzato)

