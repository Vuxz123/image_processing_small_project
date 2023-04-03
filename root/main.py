import pygame

# initialize pygame
pygame.init()

# set up window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# set up font
font = pygame.font.Font(None, 50)

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# define menu options
play_option = font.render("Play", True, WHITE)
mute_option = font.render("Mute", True, WHITE)

# define option positions
play_pos = (350, 200)
mute_pos = (350, 300)

# define option states
play_state = "inactive"
mute_state = "inactive"

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if play_pos[0] <= mouse_pos[0] <= play_pos[0]+play_option.get_width() \
                    and play_pos[1] <= mouse_pos[1] <= play_pos[1]+play_option.get_height():
                play_state = "hover"
                mute_state = "inactive"
            elif mute_pos[0] <= mouse_pos[0] <= mute_pos[0]+mute_option.get_width() \
                    and mute_pos[1] <= mouse_pos[1] <= mute_pos[1]+mute_option.get_height():
                mute_state = "hover"
                play_state = "inactive"
            else:
                play_state = "inactive"
                mute_state = "inactive"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_pos[0] <= mouse_pos[0] <= play_pos[0]+play_option.get_width() \
                    and play_pos[1] <= mouse_pos[1] <= play_pos[1]+play_option.get_height():
                # start the game
                print("Starting the game...")
            elif mute_pos[0] <= mouse_pos[0] <= mute_pos[0]+mute_option.get_width() \
                    and mute_pos[1] <= mouse_pos[1] <= mute_pos[1]+mute_option.get_height():
                # mute/unmute the sound
                print("Muting the sound...")

    # draw the menu
    window.fill(BLACK)
    pygame.draw.rect(window, GRAY, (play_pos[0]-10, play_pos[1]-10,
                                    play_option.get_width()+20, play_option.get_height()+20), 0, 10)
    pygame.draw.rect(window, GRAY, (mute_pos[0]-10, mute_pos[1]-10,
                                    mute_option.get_width()+20, mute_option.get_height()+20), 0, 10)
    if play_state == "inactive":
        pygame.draw.rect(window, BLACK, (play_pos[0], play_pos[1],
                                         play_option.get_width(), play_option.get_height()), 0)
    else:
        pygame.draw.rect(window, GRAY, (play_pos[0], play_pos[1],
                                        play_option.get_width(), play_option.get_height()), 0)
    if mute_state == "inactive":
        pygame.draw.rect(window, BLACK, (mute_pos[0], mute_pos[1],
                                         mute_option.get_width(), mute_option.get_height()), 0)
    else:
        pygame.draw.rect(window, GRAY, (mute_pos[0], mute_pos[1],
                                        mute_option.get_width(), mute_option.get_height()), 0)
    window.blit(play_option, play_pos)
    window.blit(mute_option, mute_pos)

    pygame.display.update()

pygame.quit()
