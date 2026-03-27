import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, BLACK, FPS, BLOCK_SIZE, WHITE
from food import generate_food, draw_food
from snake import draw_snake_part
import pygame.mixer

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
score = 0

font = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()
direction = "RIGHT"
pygame.display.set_caption("mini snake v2.0")

snake = [(5, 3), (4, 3), (3, 3)]
head_x, head_y = snake[0]

max_width = SCREEN_WIDTH // BLOCK_SIZE
max_height = SCREEN_HEIGHT // BLOCK_SIZE

foods = [generate_food(snake) for _ in range(5)]

eat_sound = pygame.mixer.Sound("chomp.wav")
eat_channel = pygame.mixer.Channel(0)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    if direction == "UP":
        new_head = (head_x, head_y - 1)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 1)
    elif direction == "LEFT":
        new_head = (head_x - 1, head_y)
    elif direction == "RIGHT":
        new_head = (head_x + 1, head_y)

    head_x, head_y = new_head

    screen.fill(BLACK)
    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

    
    for (fx, fy) in foods:
        draw_food(fx, fy, screen)

    if new_head in snake[1:]:
        running = False

    snake.insert(0, new_head)

    for (x, y) in snake:
        draw_snake_part(x, y, screen)

    pygame.display.update()

    
    if new_head in foods:
        score += 1
        foods.remove(new_head)
       
        foods.append(generate_food(snake + foods))
        eat_channel.play(eat_sound)
        if score >= 30:
            screen.fill(BLACK)
            win_text = font.render("You Win!!!", True, WHITE)
            screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2,
                                SCREEN_HEIGHT // 2 - win_text.get_height() // 2))
            pygame.display.update()
            
            pygame.time.delay(3000)  
            
            running = False  
    
    else:
        snake.pop()

    
    if head_x < 0 or head_x >= max_width or head_y < 0 or head_y >= max_height:
        running = False


