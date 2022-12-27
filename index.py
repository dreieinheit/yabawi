import pygame
import random

pygame.init()

background = pygame.display.set_mode((1680, 800))
pygame.display.set_caption("야바위")

img_onecup = pygame.image.load("images/cup1.png")
img_twocup = pygame.image.load("images/cup2.png")
img_threecup = pygame.image.load("images/cup3.png")
img_watercup = pygame.image.load("images/watercup.png")

size_bg_width = background.get_size()[0]
size_onecup_width = img_onecup.get_rect().size[0]
size_twocup_width = img_twocup.get_rect().size[0]
size_threecup_width = img_threecup.get_rect().size[0]
onecup_rect = img_onecup.get_rect()
twocup_rect = img_twocup.get_rect()
threecup_rect = img_threecup.get_rect()

onecup_rect.center = (420,400)
twocup_rect.center = (840,400)
threecup_rect.center = (1260,400)

x_pos_onecup = size_bg_width/2 - 420
x_pos_twocup = size_bg_width/2
x_pos_threecup = size_bg_width/2 + 420

random_onecup = random.randrange(0, 1680)
random_twocup = random.randrange(0, 1680)
random_threecup = random.randrange(0, 1680)   

to_x_onecup = 0
to_x_twocup = 0
to_x_threecup = 0

play = True
turn = False

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               turn = True
            if event.key == pygame.K_1 and x_pos_onecup < x_pos_twocup < x_pos_threecup:
                print("실패! 정답은 2번")
            if event.key == pygame.K_1 and x_pos_onecup < x_pos_threecup < x_pos_twocup:
                print("실패! 정답은 3번")
            if event.key == pygame.K_1 and x_pos_threecup < x_pos_onecup < x_pos_twocup:
                print("실패! 정답은 3번")    
            if event.key == pygame.K_1 and x_pos_threecup < x_pos_twocup < x_pos_onecup:
                print("실패! 정답은 2번")
            if event.key == pygame.K_1 and x_pos_twocup < x_pos_onecup < x_pos_threecup:
                print("성공!")
            if event.key == pygame.K_1 and x_pos_twocup < x_pos_threecup < x_pos_onecup:
                print("성공!")
            if event.key == pygame.K_2 and x_pos_onecup < x_pos_twocup < x_pos_threecup:
                print("성공!")
            if event.key == pygame.K_2 and x_pos_onecup < x_pos_threecup < x_pos_twocup:
                print("실패! 정답은 3번")
            if event.key == pygame.K_2 and x_pos_threecup < x_pos_onecup < x_pos_twocup:
                print("실패! 정답은 3번")    
            if event.key == pygame.K_2 and x_pos_threecup < x_pos_twocup < x_pos_onecup:
                print("성공!")
            if event.key == pygame.K_2 and x_pos_twocup < x_pos_onecup < x_pos_threecup:
                print("실패! 정답은 1번")
            if event.key == pygame.K_2 and x_pos_twocup < x_pos_threecup < x_pos_onecup:
                print("실패! 정답은 1번")
            if event.key == pygame.K_3 and x_pos_onecup < x_pos_twocup < x_pos_threecup:
                print("실패! 정답은 2번")
            if event.key == pygame.K_3 and x_pos_onecup < x_pos_threecup < x_pos_twocup:
                print("성공!")
            if event.key == pygame.K_3 and x_pos_threecup < x_pos_onecup < x_pos_twocup:
                print("성공!")    
            if event.key == pygame.K_3 and x_pos_threecup < x_pos_twocup < x_pos_onecup:
                print("실패! 정답은 2번")
            if event.key == pygame.K_3 and x_pos_twocup < x_pos_onecup < x_pos_threecup:
                print("실패! 정답은 1번")
            if event.key == pygame.K_3 and x_pos_twocup < x_pos_threecup < x_pos_onecup:
                print("실패! 정답은 1번")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
               turn = False

    if turn:
        
        if random_onecup-1/2 < x_pos_onecup and random_onecup+1.5/2 > x_pos_onecup:
            random_onecup = random.randrange(480, 1240)
        elif random_onecup > x_pos_onecup:
            x_pos_onecup += 1
        elif random_onecup < x_pos_onecup:
            x_pos_onecup -= 1

        if random_twocup-1/2 < x_pos_twocup and random_twocup+1.5/2 > x_pos_twocup:
            random_twocup = random.randrange(480, 1240)
        elif random_twocup > x_pos_twocup:
            x_pos_twocup += 1
        elif random_twocup < x_pos_twocup:
            x_pos_twocup -= 1
        
        if random_threecup-1/2 < x_pos_threecup and random_threecup+1.5/2 > x_pos_threecup:
            random_threecup = random.randrange(480, 1240)
        elif random_threecup > x_pos_threecup:
            x_pos_threecup += 1
        elif random_threecup < x_pos_threecup:
            x_pos_threecup -= 1
          

        onecup_rect.centerx = x_pos_onecup
        twocup_rect.centerx = x_pos_twocup
        threecup_rect.centerx = x_pos_threecup

    background.fill("black")

    background.blit(img_onecup, onecup_rect)
    background.blit(img_twocup, twocup_rect)
    background.blit(img_threecup, threecup_rect)
    
    pygame.display.update()
        
pygame.quit()