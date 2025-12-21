import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

font = pygame.font.SysFont(None, 30)
text = font.render("Hello Pygame", True, (255, 255, 255))

running = True
while running:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 125, 255), (50, 50, 100, 80))
    screen.blit(text, (50, 150))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()