import pygame
import sys

class Hurdle:
    def __init__(self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw_hurdle(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, (self.rect.x, self.rect.y-14))

class Thief:
    def __init__(self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw_thief(self, surface):
        pygame.draw.rect(surface, (109,23,230), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, self.rect)
        
pygame.init()
screen = pygame.display.set_mode((400, 400))
font = pygame.font.Font("freesansbold.ttf", 16)

hurdle_1 = Hurdle(0, 200, 200, 2)
hurdle_2 = Hurdle(200, 198, 200, 2)
hurdle_change = 1

hurdle_img = pygame.image.load("hurdle.png")
hurdle_img = pygame.transform.scale(hurdle_img, (200,25))

thief = Thief(10, 380, 15, 15)
thief_x_change = 0
thief_y_change = 0

jewel = pygame.Rect(350, 10, 40, 40)
jewel_image = pygame.image.load("jewel.png")
jewel_image = pygame.transform.scale(jewel_image, (50,50))

while True:
    screen.fill((100,255,255))
    
    # Checking if 'quit' event occurs and handle it by calling 'pygame.quit()'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
                # Checking if left arrow key is pressed
                if event.key == pygame.K_LEFT:
                    # Making 'thief_x_change' value to -1
                    thief_x_change = -1
                    
                # Checking if right arrow key is pressed    
                if event.key == pygame.K_RIGHT:
                    # Making 'thief_x_change' value to 1
                    thief_x_change = 1
                    
                # Checking if down arrow key is pressed
                if event.key == pygame.K_DOWN:
                    # Making 'thief_y_change' value to 1
                    thief_y_change = 1
                    
                # Checking if up arrow key is pressed 
                if event.key == pygame.K_UP:
                    # Making 'thief_y_change' value to -1
                    thief_y_change = -1
                    
        if event.type == pygame.KEYUP:
            thief_x_change = 0
            thief_y_change = 0
            
    # Updating the x,y values of the thief
    # Incrementing 'thief.rect.x' with the 'thief_x_change' value                
    thief.rect.x += thief_x_change
    # Incrementing 'thief.rect.y' with the 'thief_y_change' value
    thief.rect.y += thief_y_change
    
    if hurdle_1.rect.y > 398:
        hurdle_change = -1
    elif hurdle_1.rect.y < 0:
        hurdle_change = 1
    
    hurdle_1.rect.y += hurdle_change
    hurdle_2.rect.y -= hurdle_change
    
    hurdle_1.paste_image(hurdle_img)
    hurdle_2.paste_image(hurdle_img)
    thief.draw_thief(screen)
    screen.blit(jewel_image, jewel)
    
    # Checking if 'hurdle_1.rect' or 'hurdle_2.rect' collides with 'thief.rect' 
    # Using 'or' to combine the 2 conditions
    if hurdle_1.rect.colliderect(thief.rect) or hurdle_2.rect.colliderect(thief.rect):
        text = font.render("Failed, you lost", True, (0,0,0))
        screen.blit(text, (125,175))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
        
    # Checking if 'thief.rect' collides with 'jewel'
    if thief.rect.colliderect(jewel):
        text = font.render("Congratulations, you won", True, (0,0,0))
        screen.blit(text, (125,175))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    pygame.time.delay(10)
