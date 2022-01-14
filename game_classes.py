import pygame

walk_right = pygame.image.load("./sprites/charactersR.png")
walk_left = pygame.transform.flip(walk_right, True, False)
enemy_left = pygame.image.load("./sprites/enemyLeft.png")
enemy_right = pygame.transform.flip(enemy_left, True, False)


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, win):
        if self.left:
            win.blit(walk_left, (self.x, self.y))
        if self.right:
            win.blit(walk_right, (self.x, self.y))

        self.hitbox = (self.x, self.y, 45, 55)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class Projectile:
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 8

    def fire(self):
        if self.direction == "left":
            self.x -= self.vel
        elif self.direction == "right":
            self.x += self.vel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Boss:
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = 3
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, win):
        self.move()

        if self.vel > 0:
            win.blit(enemy_right, (self.x, self.y))
        else:
            win.blit(enemy_left, (self.x, self.y))

        self.hitbox = (self.x, self.y, 60, 65)

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1

    def hit(self):
        print("hit")
