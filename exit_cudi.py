import sys
import pygame


def exit_cudi(signal):
    try:
        pygame.quit()
    except Exception as e:
        print(e)
    if signal == 1:
        sys.exit(1)
