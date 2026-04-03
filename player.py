import pygame

class Player:
    def __init__(self, color, x_pos, y_pos, width, height):
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def draw_player(self, screen):
        player = pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height))

    def update_player_pos(self, key_pressed, dt):

        if key_pressed[pygame.K_w]:
            self.y_pos -= 300 * dt
            if self.y_pos <= 10.00:
                self.y_pos = 10

        if key_pressed[pygame.K_s]:
            self.y_pos += 300 * dt
            if self.y_pos >= 630.00:
                self.y_pos = 630

    def collide_detection(self, x_coord, y_coord, screen, show_collision=False):
        collission = pygame.draw.rect(screen, self.color, (self.x_pos, self.y_pos, self.width, self.height))

        if collission.collidepoint(x_coord, y_coord):
            if show_collision:
                collision = pygame.draw.rect(screen, "white", (self.x_pos, self.y_pos, self.width, self.height))

            return True
