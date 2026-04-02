import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player1_x_pos = 40
player1_y_pos = screen.get_height() / 2
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_speed = 300
cpu_x_pos = 1180
cpu_y_pos = screen.get_height() / 2

# These is a switch that help me to invert the axis of the ball
invert_ball_x_pos = False
invert_ball_y_pos = False

while running:
    ball_speed += 0.1
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Ball setup
    ball = pygame.draw.circle(screen, "white", ball_pos, 40)

    if not invert_ball_x_pos:
        ball_pos.x += ball_speed * dt
        if ball_pos.x >= 1200:
            invert_ball_x_pos = True
    else:
        ball_pos.x -= ball_speed * dt
        if ball_pos.x <= 10:
            invert_ball_x_pos = False

    if not invert_ball_y_pos:
        ball_pos.y += ball_speed * dt
        if ball_pos.y >= 630:
            invert_ball_y_pos = True
    else:
        ball_pos.y -= ball_speed * dt
        if ball_pos.y <= 0:
            invert_ball_y_pos = False

    #Player 1 setup
    player1 = pygame.draw.rect(screen, "red", (player1_x_pos, player1_y_pos, 60,80))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y_pos -= 300 * dt
        if player1_y_pos <= 10.00:
            player1_y_pos = 10
    if keys[pygame.K_s]:
        player1_y_pos += 300 * dt
        if player1_y_pos >= 630.00:
            player1_y_pos = 630

    #cpu setup
    cpu = pygame.draw.rect(screen, "green", (cpu_x_pos, cpu_y_pos, 60,80))

    if ball_pos.y >= cpu_y_pos:
        cpu_y_pos += 300 * dt
    else:
        cpu_y_pos -= 300 * dt

    #print to view if the player rect collides with the ball
    #print(player1.collidepoint(ball_pos.x, ball_pos.y))
    if player1.collidepoint(ball_pos.x, ball_pos.y):
        ##ball_pos.x += 300 * dt
        invert_ball_x_pos = False

    #cpu collision setup
    if cpu.collidepoint(ball_pos.x - 50, ball_pos.y - 50):
        invert_ball_x_pos = True


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
#Nothing to see here
