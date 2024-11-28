import pygame   #dùng thư viện pygame
from random import randint
from sklearn.cluster import KMeans
import math 
import numpy as np 
import matplotlib.pyplot as plt
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]))
pygame.init()   #khởi tạo thư viện
screen=pygame.display.set_mode((1200,700)) #tạo màn hình
pygame.display.set_caption('KMean Visualition') #ghitiêuđề
running=True
clock =pygame.time.Clock()
BACKGROUND=(214,214,214)
BLACK=(0,0,0)
WHITE=(255,255,255)
BACKGROUND_PANEL=(249,255,230)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(147,153,35)
SKY=(0,255,255)
ORGANCE=(255,125,25)
GRAPE=(100,155,65)
GRASS=(55,155,65)
COLORS=[RED,GREEN, BLUE, YELLOW, SKY, ORGANCE, GRAPE, GRASS]
font=pygame.font.SysFont('sans',40)
fontsmall=pygame.font.SysFont('sans',20)
text_plus=font.render('+', True, WHITE)
text_minus=font.render('-', True, WHITE)
text_run=font.render('Run', True, WHITE)
text_random=font.render('Random', True, WHITE)
text_algorithm=font.render('Algorithm', True, WHITE)
text_reset=font.render('Reset', True, WHITE)
text_elbow = font.render("Elbow", True, WHITE)
K=0
error=0
points=[]
clusters=[]
labels=[]
while running:
    clock.tick(60)
    screen.fill(BACKGROUND)
    mouse_x, mouse_y=pygame.mouse.get_pos()
    #ve giao dien -Draw interface
    #ve panel
    pygame.draw.rect(screen, BLACK, (50,50,700,500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55,55,690,490))
    #ve nut K +
    pygame.draw.rect(screen, BLACK, (850,50,50,50))
    screen.blit(text_plus, (860,50))
    #ve nut K -
    pygame.draw.rect(screen, BLACK, (950,50,50,50))
    screen.blit(text_min, (960,50))
    #K value
    text_k= font.render('K=' +str(K), True, BLACK)
    screen.blit(text_k, (1050,50))
    # Run  button
    pygame.draw.rect(screen, BLACK, (850,150,150,50))
    screen.blit(text_run, (900,150))
    # Random  button
    pygame.draw.rect(screen, BLACK, (850,250,150,50))
    screen.blit(text_random, (850,250))
    #Vẽ elbow button
    pygame.draw.rect(screen, BLACK, (850, 450, 150, 50))
    screen.blit(text_elbow, (850, 450))
    # Algorithm button scikit -learn
    pygame.draw.rect(screen, BLACK, (850,450,150,50))
    screen.blit(text_algorithm, (850,450))
    # Reset button 
    pygame.draw.rect(screen, BLACK, (850,550,150,50))
    screen.blit(text_reset, (850,550))
    #text_error
    text_error=font.render('Error=' + str(int(error)), True, BLACK)
    screen.blit(text_error, (850,350))
        # draw mouse pos when it is panel
    if 50<mouse_x <750 and 50<mouse_y<550:
        text_mouse=fontsmall.render('(' +str(mouse_x-50)+','+ str(mouse_y-50)+ ')',True, BLACK)
        screen.blit(text_mouse, (mouse_x+10,mouse_y))
    #ket thuc giao dien
    mouse_x, mouse_y=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 50<=mouse_x<=700 and  50<=mouse_y<=500:
                point=mouse_x-50, mouse_y-50
                print(mouse_x, mouse_y)
                points.append(point)
            #change K button + 
            if 850<mouse_x< 900 and 50<mouse_y<100:
                 K+=1
                print('Press K+')
             #change K button - 
            if 950<mouse_x< 1000 and 50<mouse_y<100:
                 if K>0:
                    K-=1
                print('Press -')
            # Run button
            if 850<mouse_x< 1000 and 150<mouse_y<200:
                labels=[]
                for p in points:
                    distances_to_clusters=[]
                    for c in clusters:
                        dis=distance(p,c)
                        distances_to_clusters.append(dis)
                    dis_min=min(distances_to_clusters)
                    label=distances_to_clusters.index(dis_min)
                    labels.append(label)
                for i in range(K):
                    sum_x=0
                    sum_y=0
                    count=0
                    for j in range(len(points)):
                        if labels[j]==i:
                            sum_x+=points[i][0]
                            sum_y+=points[i][1]
                            count+=1
                    if count!=0:
                        new_x=sum_x/count
                        new_y=sum_y/count
                        clusters[i]=(new_x, new_y)
                print('Press Run ')
            # Random button
            if 850<mouse_x< 1000 and 250<mouse_y<300:
                clusters=[]
                for i in range(K):
                    rand_point =(randint(0,700), randint(0,500))
                    clusters.append(rand_point)
                print('Press Random ')
            # Algorithm button
            if 850<mouse_x< 1000 and 450<mouse_y<500:
                print('Algorithm Random ')
            # Reset button
            if 850<mouse_x< 1000 and 550<mouse_y<600:
                print('Reset ')
    
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0]+50, points[i][1]+50), 6)
        if labels==[]:
            pygame.draw.circle(screen, WHITE, (points[i][0]+50, points[i][1]+50), 5)
        else: 
            pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0]+50, points[i][1]+50), 5)  
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i], (clusters[i][0]+50, clusters[i][1]+50), 10)
    pygame.display.flip() #cập nhật thay đổi màn hình
pygame.quit()
