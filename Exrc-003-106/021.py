#import pygame
#pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load('m021.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()


#Solução para o bug da musica não tocar por completa! OBS: ChatGPT
import pygame
import time

# Inicializa o mixer do pygame
pygame.init()
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('musica/m021.mp3')

# Inicia a reprodução
pygame.mixer.music.play()

# Aguarda enquanto a música estiver tocando
while pygame.mixer.music.get_busy():
    time.sleep(1)
