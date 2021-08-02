import pygame, sys
import time

def image_from_url(url):
    try:
        from urllib2 import urlopen
        from cStringIO import StringIO as inout
    except ImportError:
        from urllib.request import urlopen
        from io import BytesIO as inout
    myurl = urlopen(url)
    return inout(myurl.read())


pygame.init()
pygame.display.set_caption("Happy Birthday")
image_url = ('http://i1315.photobucket.com/albums/t600/11roadkills/explosion_zpsbbc7bb55.png')
image = pygame.image.load(image_from_url(image_url))
p2= False
word = " "
turn = False
cursor = False
count = -15
pygame.mouse.set_visible(False)
window=pygame.display.set_mode((700, 600))
background=pygame.Surface((window.get_rect().width, window.get_rect().height))
background.fill((255, 255, 255))
image2_url = ('http://i1315.photobucket.com/albums/t600/11roadkills/Bomb_zps31e8e05c.png')
image2img = pygame.image.load(image_from_url(image2_url))
image2 = pygame.transform.scale(image2img, (80,80))
font = pygame.font.SysFont("Comic Sans MS", 60)
font2 = pygame.font.SysFont("Comic Sans MS", 20)
font3 = pygame.font.SysFont("Comic Sans MS", 40)
label = font.render("HAPPY BIRTHDAY!", 1, (255,0,0))
label2 = font2.render("Click the center {}".format(word), 1, (0,0,0))
label3 = font3.render("Hope you have a blast!", 1, (255, 0, 0))
image=image.convert()
rect=image.get_rect()
opn = False
bomb = True
i=255
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    mpos = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    window.fill((255, 255, 255))
    window.blit(background, background.get_rect())
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        opn = True
        bomb = False
        
    if bomb:
        window.blit(label2, (10,10))
        window.blit(image2, mpos)
        
    if opn and not cursor:
        image.set_alpha(i)
        window.blit(image, rect)
        window.blit(label, (80, 200))
        pygame.time.delay(5)
        i-=1
        word = "again"
        label2 = font2.render("Click the center {}".format(word), 1, (0,0,0))
        bomb = True
        count += 1
        
    if count >= 2 and event.type == pygame.MOUSEBUTTONDOWN and not cursor:
        i = 255
        p2 = True
        opn =  False
        label2 = font2.render(" ", 1, (0,0,0))
        pygame.mouse.set_visible(True)
        
    if p2:
        bomb = False
        image.set_alpha(i)
        window.blit(image, rect)
        window.blit(label3, (80, 200))
        pygame.time.delay(5)
        i-=1
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor = True





    pygame.display.update()
