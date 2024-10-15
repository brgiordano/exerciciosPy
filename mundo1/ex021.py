# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import time
import pygame

#define o nome do arquivo
source: str = "ex21.mp3"

#inicia o módulo pygame
pygame.mixer.init()

#carrega o áudio
pygame.mixer.music.load(source)

#toca o áudio
pygame.mixer.music.play()

print(f"Tocando o áudio \"{source}\"")

#get_busy() verifica se o áudio ainda está tocando
paused = False
while pygame.mixer.music.get_busy() or paused :
    comando = int(input("[1] Play\n"
                        "[2] Pause\n"
                        "[3] Stop\nDigite a opção desejada: "))
    if comando == 1:
        pygame.mixer.music.unpause()
        paused = False
    elif comando == 2:
        pygame.mixer.music.pause()
        paused = True
    elif comando == 3:
        pygame.mixer.music.stop()
        break
print("Áudio encerrado!")