import pygame
pygame.init()

screen = pygame.display.set_mode((512, 512))
font = pygame.font.SysFont(None, 48)

black_screen = pygame.Surface((512, 512), pygame.SRCALPHA)

def nextDay(text, font, background):
    global play_scene
    opacity = 255
    date_display = font.render(text, True, (255, 255, 255)).convert_alpha()
    date_rect = date_display.get_rect(center=(256, 256))
    fade_speed = 1 

        
    while opacity >= 0:
        screen.fill((255,255,255))  # Clear screen first

        # Fade background
        background.fill((0, 0, 0, opacity))
        screen.blit(background, (0, 0))

        # Fade text
        faded_text = date_display.copy()
        faded_text.set_alpha(opacity)
        screen.blit(faded_text, date_rect)

        pygame.display.flip()
        pygame.time.delay(20)
        fade_speed += 0.2
        opacity -= fade_speed
nextDay("Saturday 7th February 2026", font, black_screen)
pygame.quit()
