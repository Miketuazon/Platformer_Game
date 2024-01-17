# Dynamically load sprite sheets and images
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

# somehow fixed alsa errors
os.environ['SDL_AUDIODRIVER'] = 'dsp'

# Initialize pygame module
pygame.init()

# Set caption on top of the screen
pygame.display.set_caption("Platformer")

# Define global variables
BG_COLOR = (255, 255, 255)  # White
WIDTH, HEIGHT = 1000, 800   # Width/height for screen
FPS = 60                    # Frames per second
PLAYER_VEL = 5              # Speed player moves on screen

# Setup game window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Create main function to run and start the game
def main(window):
    clock = pygame.time.Clock()

    # Event loop that handles collision, moving char, redrawing the window
    run = True
    while run:
        # Ensure while loop will run 60fps
        clock.tick(FPS)

        for event in pygame.event.get():
            # 1. Case for when user quits the game
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()

# Only call main function if we run this file directly
if __name__ == "__main__":
    main(window)
