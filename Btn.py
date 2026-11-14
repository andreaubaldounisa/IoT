"""!
@package Btn
Modulo per il controllo dello stato di un pulsante.
In base ad esso viene modificato un attribito d'istanza in base al numero di pressioni (alternate)
del pulsante: False, True, False, True...
"""
from machine import Pin
from time import sleep_ms, ticks_ms, ticks_diff
class Btn:
    """!
    @brief Classe che rappresenta un pulsante
    """
    def __init__(self,pin,pull_down=True):
        """!
        @brief Costruisce un pulsante.
        @param[in] pin Pin a cui è collegato il pulsante
        @param[in] pull_down Facoltativo, indica se usare le resistenze (interne) di PullDown o PullUp 
        """
        self.stato = False
        self.last = ticks_ms()

        if pull_down:
            self.btn = Pin(pin,Pin.IN,Pin.PULL_DOWN)
            self.btn.irq(trigger=Pin.IRQ_RISING, handler=self.pressed)
        else:
            self.btn = Pin(pin,Pin.IN,Pin.PULL_UP)
            self.btn.irq(trigger=Pin.IRQ_FALLING, handler=self.pressed)
        
    def debounce(self):
        """!
        @brief Verifica se è trascorso abbastanza tempo dall'ultima pressione.
        @brief Serve per evitarere il bouncing
        @return True se la pressione è da considerarsi valida; False altrimenti
        """
        if ticks_diff(ticks_ms(),self.last) > 200:
            self.last = ticks_ms()
            return True
        return False
    
    def pressed(self):
        """!
        @brief Funzione di callBack invocata all'atto della pressione del pulsante
        @brief Aggiorna il valore, laddove la pressione risultasse valida, della variabile di stato in maniera alternata
        @post La variabile di stato è stata aggiornata
        """
        if self.debounce():
            self.stato = not(self.stato)