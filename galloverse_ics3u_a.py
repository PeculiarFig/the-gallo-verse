# pygame template
import math
import random
import pygame

def linear_interpolation(x, x0, x1, y0, y1):
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)


pygame.init()
pygame.font.init()


WIDTH = 1920
HEIGHT = 1080
SIZE = (WIDTH, HEIGHT)

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

num_students = 33
MAP_SIZE = math.ceil(math.sqrt(num_students))
MAP_SIZE += 1 - MAP_SIZE % 2
MID = MAP_SIZE//2
PLOT_WIDTH = 640
PLOT_HEIGHT = 480
MIN_SCALE = HEIGHT/(MAP_SIZE*PLOT_HEIGHT)
MAX_SCALE = 1
screen = pygame.Surface((PLOT_WIDTH * MAP_SIZE, PLOT_HEIGHT * MAP_SIZE))
camera_x = screen.get_width()//2
camera_y = screen.get_height()//2
zoom_level_gallo = 1 # 1-10
grid_font = pygame.font.SysFont('Arial', 20)


# ---------------------------
# Initialize global variables for animation
# These must have your name in there

font_gallo = pygame.font.SysFont('Arial', 120)
welcome_font_gallo = pygame.font.SysFont('Arial', 40)
bg_color_gallo = "#E15E03"
# fg_color_gallo = "#FF9142"
fg_color_gallo = "#FEC661"
text_gallo = font_gallo.render("The Gallo-verse", True, fg_color_gallo)
welcome_text_gallo = welcome_font_gallo.render("Welcome to", True, fg_color_gallo)
frames_gallo = 0
bg_start = pygame.Color("#E05F02")
bg_end = pygame.Color("#6B2D01")
bg_gallo_large = pygame.Surface((1000, 1000))
bg_gallo_large.fill((0, 0, 0))
for x in range(1000):
    pygame.draw.line(bg_gallo_large, bg_end.lerp(bg_start, x/1000), (x, 0), (x, 1000))
bg_gallo_large = pygame.transform.rotate(bg_gallo_large, -45)
bg_gallo = pygame.Surface((640, 480))
bg_gallo.blit(bg_gallo_large, (-500, -500))
welcome_text_buffer = {}
# ---------------------------

ghost_x_maggie = 0
ghost_y_maggie = 200

switch_maggie = "right"

# ----------------------

duncan_glow_x, duncan_glow_y, duncan_glow_radius = 315, 220, 70
duncan_vignette_x, duncan_vignette_y, duncan_vignette_radius = 320, 240, 250

duncan_rect_x, duncan_rect_y, duncan_rect_sizex, duncan_rect_sizey = 285, 190, 60, 70
duncan_circle_x, duncan_circle_y, duncan_circle_radius = 315, 187, 30

duncan_inside_x, duncan_inside_y, duncan_inside_sizex, duncan_inside_sizey = 288, 193, 55, 65
duncan_inner_circle_x, duncan_inner_circle_y, duncan_inner_circle_radius = 315, 190, 27.5

duncan_eye_leftx, duncan_eye_lefty, duncan_eye_left_radius = 307, 190, 6
duncan_eye_rightx, duncan_eye_righty, duncan_eye_right_radius = 322, 190, 5

duncan_hover_speed = 1
duncan_glow_speed, duncan_glow_color, duncan_glow_growth = 2, 245, 1
duncan_background_color, duncan_background_change_speed = 50, 2
#---------------------

circle_x_ilia = 320
circle_y_ilia = 240
flash_color = (0, 0, 255)
last_flash_time = 0
flash_interval = 500
growrate = 5
sizeilia = 150

# ------------------

arm_r_a_rhee = 320
arm_r_b_rhee = 290
hand_r_rhee = 305
hand_r_y_rhee = 270
arm_r_y_a_rhee = 260
arm_r_y_b_rhee = 265
wave_a_rhee = False
wave_b_rhee = False
wave_c_rhee = False
arm_l_a_rhee = 160
arm_l_b_rhee = 190
hand_l_rhee = 175
hand_l_y_rhee = 270
arm_l_y_a_rhee = 260
arm_l_y_b_rhee = 265
arm_far_rhee = False
eye_a_rhee = 150
eye_b_rhee = 25
eye_c_rhee = 163
eye_d_rhee = 8
blink_rhee = False

# ------------------


running = True
while running:
    # GALLO VERSE SPECIFIC ----------------------------------------------------------------
    scale = linear_interpolation(zoom_level_gallo, 10, 1, MIN_SCALE, MAX_SCALE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            direction = event.y
            zoom_level_gallo -= direction
            zoom_level_gallo = max(min(zoom_level_gallo, 10), 1)
        elif event.type == pygame.MOUSEMOTION:
            click, _, _ = event.buttons
            if click:
                dx, dy = event.rel
                camera_x += -dx/scale
                camera_y += -dy/scale

    # DRAWING
    screen.fill((255, 255, 255))
    window.fill((100, 100, 100))

    # Draw Plot points
    for x in range(0, MAP_SIZE * PLOT_WIDTH, PLOT_WIDTH):
        for y in range(0, MAP_SIZE * PLOT_HEIGHT, PLOT_HEIGHT):
            pygame.draw.circle(screen, (30, 30, 200), (x, y), 5)
            coord_text = grid_font.render(f"({x}, {y})", False, (0, 0, 0))
            screen.blit(coord_text, (x, y))
    
    # -----------MAGGIE
    x = 1920
    y = 960
    width = 640
    height = 480


    width = 640
    height = 480

    points_maggie = [
        (x+345,y+100),
        (x+285,y+150),
        (x+385,y+150)
    ]

    points_maggie1 = [
        (x+275,y+170),
        (x+225,y+220),
        (x+315,y+220)
    ]

    points_maggie2 = [
        (x+405,y+170),
        (x+355,y+220),
        (x+445,y+220)
    ]

    points_maggie3 = [
        (x+385,y+223),
        (x+385,y+203),
        (x+443,y+190)
    ]


    pygame.draw.rect(screen, (200, 200, 200), (x, y, width, height))

    if ghost_x_maggie > 642:
        switch_maggie = "left"
    elif ghost_x_maggie < 0:
        switch_maggie = "right"


    if switch_maggie == "right":
        ghost_x_maggie += 3
    else:
        ghost_x_maggie -= 3

    # BACKGROUND
    pygame.draw.rect(screen, ("#05133d"), (x, y, width, height))

    #ground
    pygame.draw.rect(screen, ("#013220"), (x, y + 280, width, 200))


    #moon
    pygame.draw.circle(screen, ("gray"), (x + 260, y + 140), 70)

    #smallghost
    pygame.draw.circle(screen, ("white"), (x + 380, y + 183), 20)
    pygame.draw.circle(screen, ("black"), (x + 380, y + 189), 4) #mouth
    pygame.draw.circle(screen, ("black"), (x + 376, y + 180), 2) #eye
    pygame.draw.circle(screen, ("black"), (x + 386, y + 180), 2) #eye
    pygame.draw.polygon(screen, ("white"), points_maggie3)

    # HOUSE    
    pygame.draw.rect(screen, (0, 0, 0), (x + 300, y+150, 70, 150))
    pygame.draw.polygon(screen, (0,0,0), points_maggie)


    pygame.draw.rect(screen, (0, 0, 0), (x + 250, y+210, 47, 90))
    pygame.draw.polygon(screen, (0,0,0), points_maggie1)

    pygame.draw.rect(screen, (0, 0, 0), (x + 373, y+210, 47, 90))
    pygame.draw.polygon(screen, (0,0,0), points_maggie2)

    #TOP
    pygame.draw.rect(screen, (0,0,0), (x + 335, y+87, 20, 5))
    pygame.draw.rect(screen, (0,0,0), (x + 343, y+83, 5, 30))


    #FENCE
    for i in range(40):
        pygame.draw.rect(screen, (0, 0, 0), (x + 150 + 10*i, y+270, 5, 25))
    pygame.draw.rect(screen, (0, 0, 0), (x + 150, y+278,400, 3))

    #WINDOW
    pygame.draw.rect(screen, ("#e0b42c"), (x + 390, y+250, 15, 40)) #right
    pygame.draw.rect(screen, ("#e0b42c"), (x + 260, y+250, 15, 40)) #left
    pygame.draw.rect(screen, ("#e0b42c"), (x + 325, y+170, 25, 40)) #middle

    pygame.draw.circle(screen, ("#e0b42c"), (x + 338, y + 170), 12)


    pygame.draw.rect(screen, (0,0,0), (x + 325, y+190, 28, 3))     #middle lines
    pygame.draw.rect(screen, (0,0,0), (x + 335, y+172, 3, 41))
    pygame.draw.rect(screen, (0,0,0), (x + 325, y+174, 28, 3)) 

    #door
    pygame.draw.rect(screen, ("#3f2a14"), (x + 319, y+257, 30, 40))


    #pumpkin
    pygame.draw.circle(screen, ("orange"), (x + 130, y + 290), 14)
    pygame.draw.rect(screen, ("brown"), (x + 127, y+268, 3, 10))

    pygame.draw.circle(screen, ("orange"), (x + 80, y + 310), 14)
    pygame.draw.rect(screen, ("brown"), (x + 77, y+288, 3, 10))

    pygame.draw.circle(screen, ("orange"), (x + 40, y + 302), 14)
    pygame.draw.rect(screen, ("brown"), (x + 37, y+280, 3, 10))

    #grave
    pygame.draw.rect(screen, ("gray"), (x + 525, y+290, 25, 40)) 
    pygame.draw.circle(screen, ("gray"), (x + 538, y + 290), 12)

    pygame.draw.rect(screen, ("gray"), (x + 575, y+280, 25, 40)) 
    pygame.draw.circle(screen, ("gray"), (x + 588, y + 280), 12)

    #path
    pygame.draw.rect(screen, ("#515151"), (x + 319, y+300, 50, 50))


    # GHOST
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie, y + ghost_y_maggie), 30)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie, y + ghost_y_maggie + 30), 10)
    pygame.draw.rect(screen, (255, 255, 255), (ghost_x_maggie - 30, ghost_y_maggie, 60, 30))
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 20, y + ghost_y_maggie + 30), 10)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie +20, y + ghost_y_maggie + 30), 10)

    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 60, y + ghost_y_maggie + 100), 15)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 60, y + ghost_y_maggie + 115), 5)
    pygame.draw.rect(screen, (255, 255, 255), (ghost_x_maggie - 73, ghost_y_maggie + 100, 27, 15))
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 72, y + ghost_y_maggie + 115), 5)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 50, y + ghost_y_maggie + 115), 5)


    # DUNCAN -------------------------------

    x = 3200
    y = 960
    width = 640
    height = 480
    
    duncan_rect_y += duncan_hover_speed
    duncan_circle_y += duncan_hover_speed
    
    duncan_inside_y += duncan_hover_speed
    duncan_inner_circle_y += duncan_hover_speed
    
    duncan_eye_lefty += duncan_hover_speed * 0.54
    duncan_eye_righty += duncan_hover_speed * 0.65
    
    duncan_glow_y += duncan_hover_speed
    duncan_glow_color += duncan_glow_speed
    duncan_glow_radius += duncan_glow_growth
    
    duncan_background_color += duncan_background_change_speed
    
    if duncan_circle_y < 197: duncan_hover_speed *= -1
    if duncan_rect_y > 180: duncan_hover_speed *= -1
    if duncan_glow_color >= 255: duncan_glow_speed *= -1
    if duncan_glow_color <= 235: duncan_glow_speed *= -1
    if duncan_glow_radius > 100 or duncan_glow_radius < 60: duncan_glow_growth *= -1
    if duncan_background_color > 50 or duncan_background_color < 2: duncan_background_change_speed *= -1

    pygame.draw.rect(screen, (duncan_background_color, duncan_background_color, duncan_background_color), (x, y, width, height))

    pygame.draw.circle(screen, (235, 235, 235), (x + duncan_vignette_x, y + duncan_vignette_y), duncan_vignette_radius)
    pygame.draw.circle(screen, (duncan_glow_color, duncan_glow_color, duncan_glow_color), (x + duncan_glow_x, y + duncan_glow_y), duncan_glow_radius)
    
    pygame.draw.rect(screen, "Black", (x + duncan_rect_x, y + duncan_rect_y, duncan_rect_sizex, duncan_rect_sizey))
    pygame.draw.circle(screen, "Black", (x + duncan_circle_x, y + duncan_circle_y), duncan_circle_radius)
    
    pygame.draw.rect(screen, "White", (x + duncan_inside_x, y + duncan_inside_y, duncan_inside_sizex, duncan_inside_sizey))
    pygame.draw.circle(screen, "White", (x + duncan_inner_circle_x, y + duncan_inner_circle_y), duncan_inner_circle_radius)
    
    pygame.draw.circle(screen, "Black", (x + duncan_eye_leftx, y + duncan_eye_lefty), duncan_eye_left_radius)
    pygame.draw.circle(screen, "Black", (x + duncan_eye_rightx, y + duncan_eye_righty), duncan_eye_right_radius)

    # ILIA ------------------
    current_time = pygame.time.get_ticks()
    
    # Change the color of the circle only if the flash_interval has passed
    if current_time - last_flash_time >= flash_interval:
        flash_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        last_flash_time = current_time

    sizeilia += growrate
    if sizeilia < 10 or sizeilia > 150:
        growrate = growrate *- 1
    x = 2560
    y = 1440
    width_ilia = 640
    height_ilia = 480

    pygame.draw.rect(screen, (45, 96, 255), (x, y, width_ilia, height_ilia))

    pygame.draw.circle(screen, flash_color, (x + circle_x_ilia, y + circle_y_ilia), sizeilia)

    # ----------------------------------------------------------------------------------------

    if arm_far_rhee is False:
        if arm_l_a_rhee < 145:
            arm_far_rhee = True
        arm_l_a_rhee -= 1
        arm_l_b_rhee -= 1
        arm_l_y_a_rhee -= 1
        arm_l_y_b_rhee -= 1
        hand_l_rhee -= 1
        hand_l_y_rhee -= 1
    elif arm_far_rhee is True:
        if arm_l_a_rhee > 165:
            arm_far_rhee = False
        arm_l_a_rhee += 1
        arm_l_b_rhee += 1
        arm_l_y_a_rhee += 1
        arm_l_y_b_rhee += 1
        hand_l_rhee += 1
        hand_l_y_rhee += 1

    if wave_a_rhee is False:
        if arm_r_y_a_rhee < 149:
            wave_a_rhee = True
        if wave_b_rhee is False:
            arm_r_a_rhee += 1
            arm_r_b_rhee += 1
            hand_r_rhee += 1
        if arm_r_a_rhee > 335:
            wave_b_rhee = True
        arm_r_y_a_rhee -= 1
        arm_r_y_b_rhee -= 1
        hand_r_y_rhee -= 1
    elif wave_a_rhee is True:
        if arm_r_a_rhee < 315:
            wave_a_rhee = False
        if arm_r_y_a_rhee > 245:
            wave_b_rhee = False
        if wave_b_rhee is False:
            arm_r_a_rhee -= 1
            arm_r_b_rhee -= 1
            hand_r_rhee -= 1
        arm_r_y_a_rhee += 1
        arm_r_y_b_rhee += 1
        hand_r_y_rhee += 1

    if blink_rhee is False:
        if eye_b_rhee < 10:
            blink_rhee = True
        eye_a_rhee += 0.5
        eye_b_rhee -= 0.5
        eye_c_rhee += 0.25
        eye_d_rhee -= 0.25
    elif blink_rhee is True:
        if eye_b_rhee > 25:
            blink_rhee = False
        eye_a_rhee -= 0.5
        eye_b_rhee += 0.5
        eye_c_rhee -= 0.25
        eye_d_rhee += 0.25

    x = 2560
    y = 2400
    width = 640
    height = 480

    pygame.draw.rect(screen, (142, 84, 176), (x, y, width, height))
    pygame.draw.rect(screen, (142, 84, 176), (x, y, width, height))
    pygame.draw.polygon(screen, (42, 97, 60), [(x, y + 480), (x, y + 325), (x + 640, y + 325), (x + 640, y + 480)])
    pygame.draw.circle(screen, (245, 250, 182), (x + 400, y + 80), 60)
    pygame.draw.circle(screen, (142, 84, 176), (x + 420, y + 60), 40)
    pygame.draw.polygon(screen, (64, 64, 59), [(x + 200, y + 350), (x + 205, y + 290), (x + 275, y + 290), (x + 280, y + 350), (x + 250, y + 350), (x + 240, y + 280), (x + 230, y + 350)])
    pygame.draw.polygon(screen, (46, 46, 41), [(x + 197, y + 340), (x + 196, y + 355), (x + 191, y + 365), (x + 230, y + 365), (x + 232, y + 340)])
    pygame.draw.polygon(screen, (46, 46, 41), [(x + 283, y + 340), (x + 284, y + 355), (x + 289, y + 365), (x + 250, y + 365), (x + 248, y + 340)])
    pygame.draw.polygon(screen, (79, 79, 70), [(x + 200, y + 300), (x + 205, y + 190), (x + 275, y + 190), (x + 280, y + 300)])
    pygame.draw.circle(screen, (64, 64, 59), (x + hand_l_rhee, y + hand_l_y_rhee), 15)
    pygame.draw.circle(screen, (64, 64, 59), (x + hand_r_rhee, y + hand_r_y_rhee), 15)
    pygame.draw.polygon(screen, (79, 79, 70), [(x + arm_l_a_rhee, y + arm_l_y_a_rhee), (x + 176, y + 206), (x + 202, y + 221), (x + 203, y + 218), (x + arm_l_b_rhee, y + arm_l_y_b_rhee)])
    pygame.draw.polygon(screen, (79, 79, 70), [(x + arm_r_a_rhee, y + arm_r_y_a_rhee), (x + 304, y + 206), (x + 278, y + 221), (x + 277, y + 218), (x + arm_r_b_rhee, y + arm_r_y_b_rhee)])
    pygame.draw.polygon(screen, (112, 112, 95), [(x + 240, y + 265), (x + 215, y + 195), (x + 265, y + 195)])
    pygame.draw.polygon(screen, (99, 99, 90), [(x + 240, y + 265), (x + 225, y + 220), (x + 210, y + 230)])
    pygame.draw.polygon(screen, (99, 99, 90), [(x + 240, y + 265), (x + 255, y + 220), (x + 270, y + 230)])
    pygame.draw.polygon(screen, (46, 46, 41), [(x + 175, y + 195), (x + 210, y + 190), (x + 270, y + 190), (x + 305, y + 195), (x + 306, y + 205), (x + 270, y + 225), (x + 250, y + 225), (x + 240, y + 190), (x + 230, y + 225), (x + 210, y + 225), (x + 174, y + 205)])
    pygame.draw.polygon(screen, (64, 64, 59), [(x+215,y+190), (x+205,y+170), (x+210,y+140), (x+225,y+130), (x+255,y+130), (x+270,y+140), (x+275,y+170), (x+265,y+190)])
    pygame.draw.ellipse(screen, (245, 245, 54), [(x + 217, y + eye_a_rhee), (20, eye_b_rhee)])
    pygame.draw.ellipse(screen, (245, 245, 54), [(x + 243, y + eye_a_rhee), (20, eye_b_rhee)])
    pygame.draw.ellipse(screen, (255, 255, 207), [(x + 222, y + eye_c_rhee), (12, eye_d_rhee)])
    pygame.draw.ellipse(screen, (255, 255, 207), [(x + 244, y + eye_c_rhee), (12, eye_d_rhee)])
    pygame.draw.polygon(screen, (46, 46, 41), [(x + 226, y + 185), (x + 232, y + 170), (x + 240, y + 165), (x + 248, y + 170), (x + 254, y + 185), (x + 240, y + 188)])
    
    # ----------------------------------------------------------------------------------------

    # Must have these coordinates
    x = 1920
    y = 1440
    width = 640
    height = 480

    frames_gallo += 1
    text_scale_gallo = abs((math.sin(frames_gallo / 30) - 3) / 3)
    

    # Rather than screen.fill, draw a rectangle
    screen.blit(bg_gallo, (x, y))

    screen.blit(welcome_text_gallo, (x + width//2 - welcome_text_gallo.get_width()//2, y + height//3 - welcome_text_gallo.get_height()//2))
    scaled_text = pygame.transform.scale(text_gallo, (text_gallo.get_width() * text_scale_gallo, text_gallo.get_height() * text_scale_gallo))
    screen.blit(scaled_text, (x + width//2 - scaled_text.get_width()//2, y + height//2 - scaled_text.get_height()//2))
    


    # LEAVE HERE --------------------------------------------
    screen_width, screen_height = screen.get_size()
    scaled_screen = pygame.transform.scale(screen, (int(screen_width * scale), int(screen_height * scale)))
    window.blit(scaled_screen, (-camera_x*scale+WIDTH//2, -camera_y*scale+HEIGHT//2))

    pygame.display.flip()
    clock.tick(30)
    #---------------------------------------------------------


pygame.quit()
