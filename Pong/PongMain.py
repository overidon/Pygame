# MEGA PONG

# Import Area
import pygame


# Pygame screen && engine initialization area
# Initialize pygame
pygame.init()

# Create an [Array] that will hold the height and the width of the screen
screenSize = [700, 500]

# Use the pygame engine to create a game screen
# It takes the parameters of the "screenSize" array
screen = pygame.display.set_mode(screenSize)

# set the caption phrase for the window
pygame.display.set_caption("PONG pong Pong")

# Loop until the user clicks the close button.
# notice the use of "done" this is important because  it allows us to end the program
done = False

# set the repeat keyboard control and
# Create a variable which will control "Framerates"
clock = pygame.time.Clock()




# Variable Area
# Set variables equal to RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (150, 150, 150)
PURPLE = (130, 17, 190)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKYBLUE = (135, 206, 250)
MINT = (147, 255, 181)
r = 50
g = 50
b = 50


# Setup images
image = pygame.image.load("cloud.png").convert_alpha()

image = pygame.transform.scale(image, (300, 200))



# set the player one control for paddle movement
#playerMove == "NULL"

# Create an [Array] that holds the rectangle objects
gObs = [0 for x in range(5)]

# Object Classes
class RectangleParent():

    #solid = True
    #solidType = "enemy"

    def __init__(self, color, xPosition, yPosition, width, height):
        # Set the color of the object
        # Notice how the init function allows us to make unique numbers for instances
        # The unique random is automatically created as part of the init and does not
        # need to be passed as an argument
        self.color = color
        self.xPos = xPosition
        self.yPos = yPosition
        self.width = width
        self.height = height

        # corner data
        self.topleftX = xPosition
        self.topleftY = yPosition
        self.toprightX = xPosition + width
        self.toprightY = yPosition
        self.botleftX = xPosition
        self.botleftY = yPosition - height
        self.botrightX = xPosition + width
        self.botrightY = yPosition - height

    def function(self):
        print("This is a message inside the TestEnemy class.")


# OBJECT CREATION AREA
# NOTE: DO NOT PUT THE COLORS IN QUOTES if they are being processed through
leftPaddle = RectangleParent(WHITE, 20, 220, 20, 100 )

# put objects into the game Objects array
gObs[0] = leftPaddle


# Starting position of the rectangle
rect_x = 75
rect_y = 75

# Set the size of the exterior rectangle
rectSizeA = 35
# Set the size of the interior rectangle
rectSizeB = 15

# Control the change in X and Y - Which basically turns into the box speed
rect_change_x = 1.7
rect_change_y = 1.7


def update():

    # Snag Keyboard INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                #Move the left paddle up
                gObs[0].yPos = gObs[0].yPos - 10
                print("Hey, you pressed the key, 'w'!")
            if event.key == pygame.K_s:
                #Move the left paddle down
                gObs[0].yPos = gObs[0].yPos + 10
                print("Hey, you pressed the key, 's'!")

    if pygame.mouse.get_pressed()[0]:
        mpos = pygame.mouse.get_pos()

        #if mpos

        print (mpos)
        print(mpos[0])
        print(mpos[1])

        if mpos[0] > 0 and mpos[0] < 192:
            if mpos[1] > 300 and mpos[1] < 492:
                print ("Potential click on shop")

# Begin game
while not done:

    # update the game
    update()
    # Check to see if the game close button is clicked
    for event in pygame.event.get():
        # If close is clicked
        if event.type == pygame.QUIT:
            # end the game

            done = True

    # Change the current X location of the rectangle by the change in X
    rect_x += rect_change_x
    # Change the current Y location of the rectangle by the change in Y
    rect_y += rect_change_y

    # Bounce the rectangle
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
        # A hit has occured, let's grow the rectangle
        rectSizeA = rectSizeA * 1.1
        rectSizeB = rectSizeB * 1.1
        # Let's also change the background
        if g <= 40:
            g = 230
        else:
            g = g * 0.7
        if r >= 230:
            r = 11
        else:
            r = r * 1.05

        if b >= 230:
            b = 13
        else:
            b = b * 1.3
        BACKGROUND = (r, g, b)
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
        # A hit has occured, let's grow the rectangle
        rectSizeA = rectSizeA * 1.1
        rectSizeB = rectSizeB * 1.1
        # Let's also change the background
        if r >= 230:
            r = 11
        else:
            r = r * 1.05

        if g <= 40:
            g = 230
        else:
            g = g * 0.7
        if b >= 230:
            b = 13
        else:
            b = b * 1.3
        BACKGROUND = (r, g, b)

    # Set the screen background to grey
    # Notice that the background is drawn first
    screen.fill(BACKGROUND)

    # Draw the rectangles
    # draw the white line in the middle of the board
    pygame.draw.rect(screen, WHITE, [340, 0, 20, 500])

    # Draw the player goal line
    pygame.draw.rect(screen, WHITE, [0, 0, 5, 500])

    # draw the opponent goal line
    pygame.draw.rect(screen, WHITE, [695, 0, 5, 500])

    # draw the white player paddle
    pygame.draw.rect(screen, gObs[0].color, [gObs[0].xPos, gObs[0].yPos, gObs[0].width, gObs[0].height] )

    # draw the white top barrier
    pygame.draw.rect(screen, WHITE, [0, 0, 700, 5])
    # draw the white bottom barrier
    pygame.draw.rect(screen, WHITE, [0, 495, 700, 5])

    # Notice the variable screen is used in the beginning
    # This is similar to choose the "CTX" in javascript canvas
    pygame.draw.rect(screen, PURPLE, [rect_x, rect_y, rectSizeA, rectSizeA])
    pygame.draw.rect(screen, GREEN, [rect_x + 10, rect_y + 10, rectSizeB, rectSizeB])

    screen.blit(image, (100, 100))

    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("monospace", 15)

    # render text
    label = myfont.render("TEST TEXT", 1, (255, 255, 0))
    screen.blit(label, (100, 100))

   # label2 = myfont.render("awesome test", 1, (255, 255, 0))
    #font = pygame.font.SysFont("Arial", 72)
   # text = font.render("Hello!", True, PURPLE)

    # Set FPS to 60 frames per second
    clock.tick(60)

    # Update the screen render
    pygame.display.flip()

# Close everything down
pygame.quit()