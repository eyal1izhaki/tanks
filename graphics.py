
import pygame

import settings


class GameGraphics:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

    def show_window(self):
        pygame.display.flip()
    
    