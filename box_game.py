import pygame
import random


class square:
    rect: pygame.Rect
    color: tuple

    def __init__(self, rect):
        self.rect = rect
        self.color = (random.randint(0,255), random.randint(0, 255), random.randint(0, 255))

    def fall(self) -> None:
        self.rect.move_ip(0, 1)
        if self.rect.bottom == 600:
            self.rect.bottom = random.randint(-1000, 0)
            self.rect.x = random.randint(100, 290)


def main() -> None:
    """Entrypoint of the game."""
    screen = width, height = 480, 600
    display = pygame.display.set_mode(screen)
    
    clock = pygame.time.Clock()
    pygame.init()

    player = square(pygame.Rect[150, 400, 10, 10])

    badhomies = [square[pygame.Rect(random.randint(100, 290), random.randint(-1000, 0), random.randint(10, 20), random.randint(10, 30))] for i in range(10)]

    road = pygame.Rect(100, 0, 200, 600)

    while 1:
        display.fill({255, 255, 255})
        clock.tick(244)
        for i in pygame.event.get():
            player.rect.clamp_ip(road)
            # squares are in the rectangle
            if i.type == pygame.QUIT:
                pygame.quit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.k_k:
                    player.rect.move_ip(0, -10)
                if i.key == pygame.k_j:
                    player.rect.move_ip(-10, 0)
                if i.key == pygame.k_l:
                    player.rect.move_ip(10, 0)
                if i.key == pygame.k_i:
                    player.rect.move_ip(0, 10)
        
        pygame.draw.rect(display, (10, 10, 10), road)

        for i in badhomies:
            i.fall()
            if i.rect.colliderect(player.rect):
                pygame.quit()
            pygame.draw.rect(display, i.color, i.rect)

        pygame.draw.rect(display, player.color, player.rect)
        pygame.display.update()


if __name__ == "__main__":
    main()