import pygame, math, random

# initialize pygame and load some values
pygame.init()

WINDOW_SIZE = (500, 500)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Aim Trainer!")
clock = pygame.time.Clock()
font = pygame.font.Font(None, size=30)

# setting up some values
running = True

x = 250
y = 250
r = 20.0

score = 0

target_click = False

color = (255, 255, 255)

delta_time = 0.1

def m_collision(c_x, c_y, m_x, m_y, radius):
    distance = math.sqrt((c_x-m_x)**2 + (c_y-m_y)**2)
    if distance < radius:
        return True
    else:
        return False

# main game loop
while running:

    screen.fill((0, 0, 0))

    m_pos = pygame.mouse.get_pos()
    m_pressed = pygame.mouse.get_pressed()

    # check whether the ball and the cursor touch, then do the effects
    if m_collision(x, y, m_pos[0], m_pos[1], r) and m_pressed[0] and not target_click:
        color = (255, 0, 0)
        target_click = True
        score += 1
        if score > 30:
            x = random.randint(0 + int(r) + 1, WINDOW_SIZE[0] - int(r) - 1)
            y = random.randint(0+ int(r) + 1, WINDOW_SIZE[1] - int(r) -1)
        elif score > 20:
            x = random.randint(int(WINDOW_SIZE[0]/6), int(WINDOW_SIZE[0]/6)*5)
            y = random.randint(int(WINDOW_SIZE[1]/6), int(WINDOW_SIZE[1]/6)*5)
        else:
            x = random.randint(int(WINDOW_SIZE[0]/6)*2, int(WINDOW_SIZE[0]/6)*4)
            y = random.randint(int(WINDOW_SIZE[1]/6)*2, int(WINDOW_SIZE[1]/6)*4)
    elif not m_collision(x, y, m_pos[0], m_pos[1], r):
        color = (255, 255, 255)
        target_click = False

    text = font.render(f"{score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.draw.circle(screen, color, (x, y), r)

    # take user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    delta_time = clock.tick(60) / 1000
    pygame.display.flip()

pygame.quit()