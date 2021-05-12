# import the pygame module, so you can use it
import pygame
from time import sleep
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("maximal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((960,720))
    xpos = 900
    ypos = 700
    vel = 1
    radius = 10

     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:

        screen.fill((0, 0, 0))

        pygame.draw.circle(screen, (255, 255, 255), (int(xpos), int(ypos)), radius)

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
        pressKey = pygame.key.get_pressed()

        if pressKey[pygame.K_a] and xpos>=0:
            xpos -= vel
            pygame.time.delay(1)  
        if pressKey[pygame.K_s] and ypos<=720:
            ypos += vel
            pygame.time.delay(1)   
        if pressKey[pygame.K_w] and ypos>=0:
            ypos -= vel
            pygame.time.delay(1) 
        if pressKey[pygame.K_d] and xpos<=960:
            xpos += vel
            pygame.time.delay(1)
        
        

        pygame.display.update()
        
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()