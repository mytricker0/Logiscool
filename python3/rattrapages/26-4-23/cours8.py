import pygame
import random


pygame.init()

white = (255,255,255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height)) # taille de la fenetre
pygame.display.set_caption('Snake') # titre de la fenetre
clock = pygame.time.Clock()


snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("Arial", 25)
score_font = pygame.font.SysFont("Arial", 35)


def Your_score(score):
    value = score_font.render("Your Score is: " + str(score), True, yellow) # affiche le score
    dis.blit(value, [0, 0]) # affiche le score en haut a gauche

def our_snake(snake_block, snake_list): # dans snake_list il y a des coordonnées [x,y] de chaque bloc du serpent

    for x in snake_list: # pour chaque bloc du serpent
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block]) # dessine le serpent

def message(msg, color):
    mesg = font_style.render(msg, True, color) # affiche le message
    dis.blit(mesg, [dis_width / 6, dis_height / 3]) # affiche le message au centre de la fenetre

def gameLoop():  # création de la fonction gameLoop
    game_over = False
    game_close = False
    x1 = dis_width / 2 # position x du serpent
    y1 = dis_height / 2 # position y du serpent

    x1_change = 0
    y1_change = 0

    snake_List = [] # liste des coordonnées de chaque bloc du serpent
    Length_of_snake = 1 # longueur du serpent

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # position x de la nourriture
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 # position y de la nourriture
    # on utilise round pour que la nourriture soit sur un multiple de 10

    while not game_over: # tant que le jeu n'est pas fini

        while game_close: # si le jeu est fini
            dis.fill(blue) # fond bleu
            message("You Lost! Press Q-Quit or C-Play Again", red) # affiche le message
            Your_score(Length_of_snake - 1) # affiche le score
            pygame.display.update() # met a jour l'affichage
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False # quitte le jeu
                    if event.key == pygame.K_c:
                        gameLoop() # recommence le jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN: # si une touche est appuyée
                if event.key == pygame.K_LEFT: # si c'est la touche gauche
                    x1_change = -snake_block # le serpent va a gauche
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: # si c'est la touche droite
                    x1_change = snake_block # le serpent va a droite
                    y1_change = 0
                elif event.key == pygame.K_UP: # si c'est la touche haut
                    y1_change = -snake_block # le serpent va en haut
                    x1_change = 0
                elif event.key == pygame.K_DOWN: # si c'est la touche bas
                    y1_change = snake_block # le serpent va en bas
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            # si le serpent sort de la fenetre
            game_close = True
        x1 += x1_change # on change la position x du serpent
        y1 += y1_change # on change la position y du serpent
        dis.fill(blue) # fond bleu
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) # dessine la nourriture
        snake_head = [x1,y1] # liste des coordonnées de la tête du serpent
        snake_List.append(snake_head) # ajoute les coordonnées de la tête du serpent a la liste
        if len(snake_List) > Length_of_snake: # si la longueur du serpent est plus grande que la longueur du serpent
            del snake_List[0] # supprime le dernier bloc du 
        for x in snake_List[:-1]: # pour chaque bloc du serpent
            if x == snake_head: # si le serpent se touche
                game_close = True # le jeu est fini
        
        
        our_snake(snake_block, snake_List) # dessine le serpent
        Your_score(Length_of_snake - 1) # affiche le score

        pygame.display.update() # met a jour l'affichage

        if x1 == foodx and y1 == foody: # si le serpent mange la nourriture    
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # position x de la nourriture
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 # position y de la nourriture
            Length_of_snake += 1 # augmente la longueur du serpent
        clock.tick(snake_speed) # vitesse du serpent
    pygame.quit() # quitte pygame
    quit() # quitte python
    
gameLoop()