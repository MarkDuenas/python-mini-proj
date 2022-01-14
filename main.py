import pygame

from game_classes import Player, Projectile, Boss

pygame.init()

S_WIDTH = 500
S_HEIGHT = 500

win = pygame.display.set_mode((S_WIDTH, S_HEIGHT))

pygame.display.set_caption("Game")

bg = pygame.image.load("./sprites/battleback1.png")

clock = pygame.time.Clock()

# X = 50
# Y = 400
# WIDTH = 24
# HEIGHT = 24
# VEL = 5
# left = False
# right = True
# isJump = False
# jumpCount = 10


def redraw_game_window():

    win.blit(bg, (0, 0))
    hero.draw(win)
    enemy.draw(win)
    for fireball in fireballs:
        fireball.draw(win)
    pygame.display.update()


# main loop
hero = Player(300, 410, 48, 48)
enemy = Boss(100, 410, 48, 48, 450)
fireballs = []
fireball_delay = 0
run = True
while run:
    clock.tick(27)

    if fireball_delay > 0:
        fireball_delay += 1
    if fireball_delay > 5:
        fireball_delay = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for fireball in fireballs:

        if (
            fireball.y - fireball.radius < enemy.hitbox[1] + enemy.hitbox[3]
            and fireball.y + fireball.radius > enemy.hitbox[1]
        ):
            if (
                fireball.x + fireball.radius > enemy.hitbox[0]
                and fireball.x - fireball.radius < enemy.hitbox[0] + enemy.hitbox[2]
            ):
                enemy.hit()
                fireballs.remove(fireball)

        if fireball.x < 500 and fireball.x > 0:
            fireball.fire()
        else:
            fireballs.remove(fireball)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and fireball_delay == 0:
        if hero.left:
            direction = "left"
        else:
            direction = "right"

        if len(fireballs) < 5:
            fireballs.append(
                Projectile(round(hero.x + hero.width // 2), round(hero.y + hero.height // 2), 6, (255, 0, 0), direction)
            )
        fireball_delay = 1

    if keys[pygame.K_LEFT] and hero.x > hero.vel:
        hero.x -= hero.vel
        hero.left = True
        hero.right = False
    elif keys[pygame.K_RIGHT] and hero.x < S_WIDTH - hero.width - hero.vel:
        hero.x += hero.vel
        hero.left = False
        hero.right = True
    # else:
    #     hero.left = False
    #     hero.right = True

    if not hero.isJump:
        if keys[pygame.K_UP]:
            hero.isJump = True
    else:
        if hero.jumpCount >= -10:
            neg = 1
            if hero.jumpCount < 0:
                neg = -1
            hero.y -= (hero.jumpCount ** 2) / 2 * neg
            hero.jumpCount -= 1
        else:
            hero.isJump = False
            hero.jumpCount = 10

    redraw_game_window()

pygame.quit()
