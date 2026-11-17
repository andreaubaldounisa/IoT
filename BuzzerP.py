"""!
@package BuzzerP
Modulo per la gestione di un buzzer passivo
"""
from machine import Pin, PWM
from time import sleep_ms

class BuzzerP:
    """!
    @brief Classe per la gestione di un buzzer passivo
    """
    
    def __init__(self,pin):
        """!
        @brief Costruttore di un buzzer passio
        @param[in] pin Pin cui è associato il buzzer passivo
        @pre pin Deve essere un pin dell'ESP32 che supporti l'ouput e il PWM
        """
        self.buzzer = PWM(Pin(pin,Pin.OUT))
        self.buzzer.freq(440) #Inizializza la frequenza ad un La4 (scelta personale)
        self.buzzer.duty(0) #Inizialmente il buzzer non riproduce alcun suono
    
    #TODO: modificarla in modo da supportare melodie con note di durate diverse
    def play(self, melodia, durata_nota, duty):
        """!
        @brief Fa riprodurre al buzzer una melodia con una certa intensità
        @param[in] melodia Lista delle note da suonare (nota==0 indica una pausa)			
        @param[in] durata_nota(int) Tempo in ms per la quale ogni nota deve essere riprodotta
        @param[in] duty(int) Intensità del suono (512 è il valore ottimale)
        @pre melodia Deve essere una lista nella quale il massimo valore della frequenza ed il minimo siano accettabile per il dispositivo usato
        @pre durata_nota Deve essere >= 0
        @pre duty Deve essere 0<=x<= 1023
        @ref note.py 
        """
        for nota in melodia:
            if nota == 0:
                self.buzzer.duty(0) #Fai una psausa
            else: #Altrimenti, riproduci la nota con la giusta frequenza e intensità
                self.buzzer.freq(nota)
                self.buzzer.duty(duty) 
            sleep_ms(durata_nota) #Durata della nota
        self.stop() # Ferma il suono alla fine
    
    def stop(self):
        """!
        @brief Interrompe la riproduzione
        """
        self.buzzer.duty(0)