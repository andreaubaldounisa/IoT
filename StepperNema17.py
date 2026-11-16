"""!
@package StepperNema17
Modulo per la gestione di un motore Nema17 con driver a4988
"""
from machine import Pin
from time import sleep_us

class StepperNema17:
    """!
    @brief Classe per gestire uno stepper motor Nema17 col driver a4988
    """
    
    def __init__(self,pinDir, pinStep):
        """!
        @brief Costruisce un motore Nema17
        @param[in] pinDir Pin dell'Esp32 cui è connesso il pin Dir del driver
        @param[in] pinStep Pin dell'Esp32 cui è connesso il pin Step del driver
        @pre pinDir Deve essere un pin di GPIO
        @pre pinStep Deve essere un pin di GPIO
        """
        self.nema = Pin(pinStep,Pin.OUT)
        self.direction = Pin(pinDir, Pin.OUT)
        
    def __make_one_step(self,delay):
        """!
        @brief Fa fare al motore 1 passo. E' da considerarsi privata.
        @param[in] delay Pausa tra un passo e l'altro (da misurare in us)
        @pre delay Deve essere >= 0
        """
        self.nema.value(1)
        sleep_us(int(delay/2))
        self.nema.value(0)
        sleep_us((delay/2))
        
    def step(self,steps,delay,direction):
        """!
        @brief Fa eseguire steps passi al motore con un delay fisso tra un passo e l'altro
        @param[in] steps Numero di passi da compiere
        @param[in] delay Pausa tra un passo e l'altro (da misurare in us)
        @param[in] direction Indica il verso di rotazione
        @pre steps Deve essere >= 0
        @pre delay Deve essere >= 0
        @pre direction Deve essere 0 o 1
        """
        
        self.direction.value(direction) #Imposta la direzione desiderata
        
        for i in range(steps):
            self.__make_one_step(delay)