'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame

# 1. Inicializar o Pygame
pygame.init()

# 2. Carregar o arquivo MP3
pygame.mixer.music.load('Sepultura - Roots Bloody Roots.mp3')

# 3. Reproduzir a música
pygame.mixer.music.play()

# Só funcionou depois que acrescentei input, deve ter mudado algo lógica da biblioteca. 
input()

pygame.event.wait()