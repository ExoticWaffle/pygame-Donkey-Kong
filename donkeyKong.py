import pygame
import random
pygame.init()

screenWidth=1024
screenHeight=960
win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("donkey kong")

invSurf= pygame.Surface((1024,960))
invSurf.set_alpha(0)

runSpriteLeft=[pygame.image.load('marioRun1.png'),pygame.image.load('marioRun2.png')]
runRight1=pygame.transform.flip(runSpriteLeft[0],True,False)
runRight2=pygame.transform.flip(runSpriteLeft[1],True,False)
runSpriteRight=[runRight1,runRight2]
stillLeft=pygame.image.load('stillMario.png')
stillRight=pygame.transform.flip(stillLeft,True,False)
jumpLeft=pygame.image.load('marioJump.png')
jumpRight=pygame.transform.flip(jumpLeft,True,False)
ladderLeft=pygame.image.load('ladderMario.png')
ladderRight=pygame.transform.flip(ladderLeft, True, False)
ladderAnim=[ladderLeft, ladderRight]
ladderTopLeft=pygame.image.load('ladderTop1.png')
ladderTopRight=pygame.transform.flip(ladderTopLeft,True,False)
ladderEndLeft=pygame.image.load('ladderTop2.png')
ladderEndRight=pygame.transform.flip(ladderEndLeft, True,    False)
ladderTopAnim=[ladderTopLeft, ladderEndRight]
ladderStand=pygame.image.load('ladderStand.png')
death1=pygame.image.load('deathAnim1.png')
death2=pygame.transform.rotate(death1, 270)
death3=pygame.transform.flip(death1,False,True)
death4=pygame.transform.rotate(death1, 90)
deathAnim=[death1,death2,death3,death4]
deathHalo=pygame.image.load('haloMario.png')

barrel1=pygame.image.load('barrel.png')
barrel2=pygame.transform.flip(barrel1, False, True)
barrel3=pygame.transform.flip(barrel1, True, True)
barrel4=pygame.transform.flip(barrel1, True, False)
barrelRoll=[barrel1,barrel2,barrel3,barrel4]
ladderBarrel1=pygame.image.load('ladderBarrel.png')
ladderBarrel2=pygame.image.load('ladderBarrel2.png')
barrelRollLadder=[ladderBarrel1,ladderBarrel2]
barrelStack=pygame.image.load('4Barrels.png')
oilBarrel=pygame.image.load('oilCan.png')

dkBarrel=pygame.image.load('donkeyKong3.png')
dkGorilla=pygame.image.load('donkeyKong2.png')
dkGorilla2=pygame.transform.flip(dkGorilla, True, False)
dkPickUp=pygame.image.load('donkeyKong1.png')
dkThrow=pygame.transform.flip(dkPickUp,True,False)
dkAnim=[dkPickUp,dkBarrel,dkThrow,dkThrow,dkGorilla,dkGorilla2]

pauline1=pygame.image.load('pauline1.png')
pauline2=pygame.image.load('pauline2.png')
paulineAnim=[pauline1, pauline2]

platform1=pygame.image.load('platform.png')
ladderEdge=pygame.image.load('ladderEdge.png')
ladderStep=pygame.image.load('ladderStep.png')

textFont=pygame.font.Font('8-Bit Madness.ttf', 32)
finishText=textFont.render("Congratulations! Other features and levels may come soon...", True, (255,255,255))


clock=pygame.time.Clock()

rectList1=[pygame.draw.rect(win, (0,0,0), (64, 880, 448, 32))]
rectList2=[]
rectList3=[]
rectList4=[]
rectList5=[]
rectList6=[pygame.draw.rect(win, (0,0,0), (64, 224, 568, 32))]
rectList7=[pygame.draw.rect(win, (0,0,0), (416, 112, 192, 32))]

for i in range(13):
    if i>=6:
        rectList1.append(pygame.draw.rect(win, (0,0,0), (128 + (64*i), 876-(4*(i-6)), 64, 32)))

    rectList2.append(pygame.draw.rect(win, (0,0,0), (64 + (64*i), 720+(4*i), 64, 32)))
    rectList3.append(pygame.draw.rect(win, (0,0,0), (128 + (64*i), 636-(4*i), 64, 32)))
    rectList4.append(pygame.draw.rect(win, (0, 0, 0), (64 + (64 * i), 456 + (4 * i), 64, 32)))
    rectList5.append(pygame.draw.rect(win, (0, 0, 0), (128 + (64 * i), 372 - (4 * i), 64, 32)))

    if i>=9:
        rectList6.append(pygame.draw.rect(win, (0, 0, 0), (64 + (64 * i), 228 + (4 * (i-9)), 64, 32)))

rectsList=[rectList1, rectList2, rectList3, rectList4, rectList5, rectList6, rectList7]

floor1=pygame.draw.rect(win, (0, 0, 0), (0, 720, 1024, 202), 1)

floor2=pygame.draw.rect(win, (0, 0, 0), (0, 588, 1024, 202), 1)

floor3=pygame.draw.rect(win, (0, 0, 0), (0, 456, 1024, 202), 1)

floor4=pygame.draw.rect(win, (0, 0, 0), (0, 324, 1024, 202), 1)

floor5=pygame.draw.rect(win, (0, 0, 0), (0, 192, 1024, 202), 1)

floor6=pygame.draw.rect(win, (0, 0, 0), (0, 60, 1024, 202), 1)

floor7=pygame.draw.rect(win, (0,0,0), (0, 0, 1024, 70), 1)

floors=[floor1, floor2, floor3, floor4, floor5, floor6, floor7]

donkeyRect=pygame.draw.rect(win, (0,0,0), (126, 96, 184, 128))

def ladderLines(x, starty, endy):
    return pygame.draw.line(win, (255, 0, 0), (x, starty), (x, endy))


ladderLinesLeft=[ladderLines(800, 796, 860), ladderLines(448,648,744), ladderLines(192,664,728), ladderLines(512,512,612),
                 ladderLines(800,532,596), ladderLines(192,400,464), ladderLines(352, 388, 472), ladderLines(800,268,332), ladderLines(576,144,224)]

ladderLinesRight=[ladderLines(832, 796, 860), ladderLines(480,648,744), ladderLines(224,664,728), ladderLines(544,512,612),
                  ladderLines(832,532,596), ladderLines(224,400,464), ladderLines(384, 388, 472), ladderLines(832,268,332), ladderLines(608,144,224)]

ladderTopLeft=[ladderLines(800, 764 ,796), ladderLines(448,616,648), ladderLines(192,632,664), ladderLines(512,480,512),
               ladderLines(800,500,532), ladderLines(192,368,400), ladderLines(352, 356,388), ladderLines(800,236,268), ladderLines(576,112,144)]

ladderTopRight=[ladderLines(832, 764 ,796), ladderLines(480,616,648), ladderLines(224,632,664), ladderLines(544,480,512),
                ladderLines(832,500,532), ladderLines(224,368,400), ladderLines(384, 356,388), ladderLines(832,236,268), ladderLines(608,112,144)]

ladderDownLeft=[(800,764), (448,616), (192,632), (512,480), (800,500), (192,368), (352,356), (800,236), (576,112)]

ladderDownRight=[(832,764), (480,616), (224,632), (544,480), (832,500), (224,368), (384,356), (832,236), (608,112)]


brokenLadderLeft=[(384,736), (320,468), (736,332), (416,224)]

brokenLadderRight=[(416,736), (352,468), (768,332), (448,224)]

ladderDieRoll=[0,1,0]
brokenLadderDieRoll=[0,0,1,0,0]


class player(object):
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=4
        self.jump=False
        self.onLadder=False
        self.ladderTop=False
        self.ladderDown=False
        self.topFrame=0
        self.ladderCount=0
        self.originJump=4
        self.jumpSpeed=4
        self.airCount=0
        self.spinCount=0
        self.numSpins=0
        self.right=True
        self.left=False
        self.still=True
        self.die=False
        self.finish = False
        self.frameCount=0
        self.screenWidth=960
        self.screenHeight=960
        self.hitbox=pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height), 1)
        self.bottomLine=pygame.draw.line(win, (0,0,0), (self.x, self.y), (self.x+2, self.y), 1)
        self.sidePoint1=(self.x, self.y)
        self.sidePoint2=(self.x, self.y)

    def draw(self, win, invWin):
        if self.frameCount != 7:
            self.frameCount += 1
        else:
            self.frameCount = 0

        if self.spinCount!=15 and self.die:
            self.spinCount+=1

        elif self.spinCount==15 and self.die:
            self.spinCount=0
            self.numSpins+=1

        if self.ladderCount==15:
            self.ladderCount=0
        elif self.ladderCount==0:
            self.ladderCount=14

        if self.topFrame==15:
            self.topFrame=0
        elif self.topFrame==0:
            self.topFrame=14

        if self.die:
            if self.numSpins!=4:
                win.blit(deathAnim[self.spinCount//4], (self.x,self.y))
            else:
                win.blit(deathHalo, (self.x, self.y))

        elif self.left and not (self.still) and not (self.jump):
            win.blit(runSpriteLeft[self.frameCount // 4], (self.x, self.y))
        elif self.left and self.still and not (self.jump):
            win.blit(stillLeft, (self.x, self.y))
        elif self.right and not (self.still) and not (self.jump):
            win.blit(runSpriteRight[self.frameCount // 4], (self.x, self.y))
        elif self.right and self.still and not (self.jump):
            win.blit(stillRight, (self.x, self.y))
        elif self.jump and self.left:
            win.blit(jumpLeft, (self.x, self.y))
        elif self.jump and self.right:
            win.blit(jumpRight, (self.x, self.y))
        elif self.onLadder:
            win.blit(ladderAnim[self.ladderCount // 8], (self.x, self.y))
        elif self.ladderTop:
            win.blit(ladderTopAnim[self.topFrame // 8], (self.x, self.y))
        elif self.ladderDown:
            win.blit(ladderStand, (self.x, self.y))

        if (self.left and self.still and not self.jump) or (self.right and self.still and not self.jump) or self.ladderDown:
            self.hitbox=pygame.draw.rect(invWin, (255, 0, 0), (self.x+8, self.y, self.width-16, self.height), 1)
            self.bottomLine = pygame.draw.line(invWin, (255, 0, 0), (self.x+8, self.y+64), (self.x + (self.width-8), self.y+64), 1)
            self.sidePoint1=(self.x+8, self.y+62)
            self.sidePoint2=(self.x+56, self.y+62)

        elif self.onLadder:
            self.hitbox = pygame.draw.rect(invWin, (255, 0, 0), (self.x + 8, self.y, self.width - 16, self.height), 1)
            self.bottomLine = pygame.draw.line(invWin, (255, 0, 0), (self.x + 8, self.y + 64), (self.x + (self.width - 8), self.y + 64), 1)

        elif self.ladderTop:
            self.hitbox= pygame.draw.rect(invWin, (255, 0, 0), (self.x + 4, self.y+8, self.width - 8, self.height-16), 1)
            self.bottomLine=pygame.draw.line(invWin, (255, 0, 0), (self.x+4, self.y + 64), (self.x + (self.width-4), self.y + 64), 1)

        else:
            self.hitbox = pygame.draw.rect(invWin, (255, 0, 0), (self.x, self.y, self.width, self.height), 1)
            self.bottomLine = pygame.draw.line(invWin, (255, 0, 0), (self.x, self.y + 64), (self.x+64, self.y + 64), 1)
            self.sidePoint1=(self.x-2, self.y+62)
            self.sidePoint2=(self.x+66, self.y+62)

    def death(self):
        self.x = 192
        self.y = 812
        self.onLadder = False
        self.ladderTop = False
        self.jump = False
        self.left = False
        self.right = True
        self.still = True
        self.jumpSpeed = mario.originJump
        self.frameCount = 0
        self.airCount = 0
        self.ladderCount = 0
        self.topFrame = 0
        self.spinCount=0
        self.numSpins=0
        self.die = False


class aBarrel(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=64
        self.height=64
        self.vel=8
        self.isLadder=False
        self.isFall=False
        self.kill=False
        self.rollCount=0
        self.i=5
        self.hitbox=pygame.draw.rect(win, (0,0,0), (self.x,self.y,self.width,self.height))
        self.bottomLine=pygame.draw.line(win, (0,0,0), (self.x,self.y), (self.x+2, self.y+2))

    def draw(self, win, invWin):
        if not self.kill:
            self.rollCount+=1

        if self.isLadder:
            if self.rollCount>=3:
                self.rollCount=0

            win.blit(barrelRollLadder[self.rollCount // 2], (self.x,self.y))

            self.hitbox=pygame.draw.rect(invWin, (0,255,0), (self.x+6, self.y+16, self.width-12, self.height-32), 1)
            self.bottomLine=pygame.draw.line(invWin, (0,255,0), (self.x+6, self.y+52), (self.x+58, self.y+52), 1)

        else:
            if self.rollCount==15:
                self.rollCount=0

            win.blit(barrelRoll[self.rollCount//4], (self.x,self.y))

            self.hitbox=pygame.draw.rect(invWin, (0,255,0), (self.x+12, self.y+16, self.width-24, self.height-32), 1)
            self.bottomLine=pygame.draw.line(invWin, (0,255,0), (self.x+12, self.y+52), (self.x+52, self.y+52), 1)


def stepUp(rectList, point):

    for i in range(len(rectList)):
        if rectList[i].collidepoint(point):
            return -4
    return 0


def ladderLine(x,y):
    if (y+12)%16==0:
        win.blit(ladderStep, (x, y))
    else:
        win.blit(ladderEdge, (x, y))


def ladder(height,x,y):
    for i in range(height):
        ladderLine(x,y)
        y+=4


def brokenLadder(height1, height2, skip, x,y):
    ladder(height1,x,y)
    y+=(skip*4)+(height1*4)
    ladder(height2,x,y)


def ladderCheck(ans,ans2,bottomLine, pointList1, pointList2):
    for i in range(len(pointList1)):
        if int(bottomLine.collidepoint(pointList1[i])) + int(bottomLine.collidepoint(pointList2[i]))==ans\
                or int(bottomLine.collidepoint(pointList1[i])) + int(bottomLine.collidepoint(pointList2[i]))==ans2:
            return True
    return False


def platforms(win, x,y,kind,level):
    if kind==1:
        for i in range(7):
            win.blit(level, (x,y))
            x+=64

        for i in range(7):
            y -= 4
            win.blit(level,(x,y))
            x+=64

    elif kind==2:
        for i in range(9):
            win.blit(level, (x, y))
            x+= 64

        for i in range(4):
            y += 4
            win.blit(level, (x, y))
            x += 64

    elif kind==3:
        for i in range(13):
            win.blit(level, (x, y))
            y += 4
            x += 64

    elif kind==4:
        for i in range(13):
            win.blit(level, (x, y))
            y -= 4
            x += 64

    else:
        for i in range(3):
            win.blit(level, (x,y))
            x+=64


def screenUpdate():
    win.fill((0, 0, 0))

    platforms(win,64,864,1,platform1)
    platforms(win,64,704,3,platform1)
    platforms(win,128,620,4,platform1)
    platforms(win,64,440,3,platform1)
    platforms(win,128,356,4,platform1)
    platforms(win,64,208,2,platform1)
    platforms(win,416,96,5,platform1)

    brokenLadder(3, 8, 16, 384, 772)
    brokenLadder(6, 8, 16, 320, 504)
    brokenLadder(8, 8, 16, 736, 368)
    brokenLadder(4, 13, 8, 416, 256)

    ladder(16, 800, 796)
    ladder(24, 448, 648)
    ladder(16, 192, 664)
    ladder(24, 512, 516)
    ladder(16, 800, 532)
    ladder(16, 192, 400)
    ladder(20, 352, 392)
    ladder(16, 800, 268)
    ladder(20, 576, 144)

    ladder(52, 384, 16)
    ladder(52,320, 16)

    win.blit(dkAnim[dkCount//23], (126,96))

    win.blit(barrelStack, (46,96))

    win.blit(paulineAnim[paulineCount//32], (416, 24))

    if not mario.finish:
        for barrel in barrels:
            barrel.draw(win, invSurf)

    win.blit(oilBarrel, (64, 816))

    if not mario.finish:
        mario.draw(win, invSurf)

    else:
        win.blit(stillLeft, (mario.x, mario.y))
        win.blit(finishText, (64, 208))
        pygame.display.update()

    pygame.display.update()

currentFloor=floors[0]
isRect=True
mario=player(192,812,64,64)
barrels=[]
run=True
falling=False
spawnCount=85
dkCount=0
paulineCount=0

i=0

while run:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()

    if not falling and not mario.onLadder and not mario.ladderTop and not mario.ladderDown and not mario.die and not mario.finish:
        mario.ladderCount=0
        mario.topFrame=0
        i=0
        while 5>4:
            if floors[i].collidepoint(mario.x, mario.y):
                break
            i+=1

        if mario.bottomLine.collidelist(rectsList[i])==-1 and not mario.jump:
            if i==1 or i==3 or i==5:
                if mario.x>=896:
                    falling=True

            elif i==2 or i==4:
                if mario.x<=64:
                    falling=True

            mario.y+=4

        if i==1 or i==3 or i==5:
            mario.y+=stepUp(rectsList[i], mario.sidePoint1)

        else:
            mario.y+=stepUp(rectsList[i], mario.sidePoint2)

        if not mario.jump:
            if keys[pygame.K_a] and not (i==0 and mario.x<=128) and mario.x>64:
                mario.x -= mario.vel
                mario.left = True
                mario.right = False
                mario.still = False

            elif keys[pygame.K_d] and mario.x < mario.screenWidth - mario.width:
                mario.x += mario.vel
                mario.right = True
                mario.left = False
                mario.still = False

            else:
                mario.still=True

            if mario.hitbox.collidelist(ladderLinesLeft) != -1 and mario.hitbox.collidelist(ladderLinesRight) != -1:
                if keys[pygame.K_UP]:
                    mario.ladderTop = False
                    mario.onLadder = True
                    mario.left = False
                    mario.right = False
                    mario.still = False
                    mario.y-=2

            if ladderCheck(2, 2, mario.bottomLine, ladderDownLeft, ladderDownRight):
                if keys[pygame.K_DOWN]:
                    mario.ladderTop = True
                    mario.left = False
                    mario.right = False
                    mario.still = False
                    mario.y += 2
                    mario.topFrame = 14
                    i-=1

            if keys[pygame.K_w]:
                mario.jump=True

        else:
            if mario.jumpSpeed>=-mario.originJump:
                mario.y-=(mario.jumpSpeed*abs(mario.jumpSpeed))
                if mario.jumpSpeed==0 or mario.jumpSpeed==0.5 or mario.jumpSpeed==-0.5:
                    if mario.airCount==1:
                        mario.airCount=0
                        mario.jumpSpeed -= 0.5
                    else:
                        mario.airCount+=1
                else:
                    mario.jumpSpeed-=0.5

            else:
                mario.jumpSpeed=mario.originJump
                mario.jump=False
                mario.hasJump=True

            if mario.right and not mario.still and mario.x < mario.screenWidth - mario.width:
                mario.x+=mario.vel

            elif mario.left and not mario.still and mario.x > 64:
                mario.x-=mario.vel

    elif mario.onLadder and not mario.die and not mario.finish:
        mario.left=False
        mario.right=False
        if mario.hitbox.collidelist(ladderLinesLeft)!=-1 or mario.hitbox.collidelist(ladderLinesRight)!=-1:
            if keys[pygame.K_UP]:
                mario.y-=2
                mario.ladderCount+=1

            elif keys[pygame.K_DOWN] and mario.bottomLine.collidelist(rectsList[i])==-1:
                mario.y+=2
                mario.ladderCount-=1

        if mario.bottomLine.collidelist(rectsList[i])!=-1:
            mario.onLadder=False
            mario.still=True
            mario.left=True

        elif mario.bottomLine.collidelist(ladderTopLeft)!=-1 or mario.bottomLine.collidelist(ladderTopRight)!=-1:
            mario.onLadder=False
            mario.ladderTop=True
            mario.y-=2

    elif mario.ladderTop:
        mario.left=False
        mario.right=False
        if keys[pygame.K_UP]:
            mario.y-=2
            mario.topFrame+=1

        elif keys[pygame.K_DOWN]:
            mario.y+=2
            mario.topFrame-=1

        if mario.bottomLine.collidelist(ladderLinesLeft)!=-1 or mario.hitbox.collidelist(ladderLinesRight)!=-1:
            mario.onLadder = True
            mario.ladderTop = False

        elif ladderCheck(1,2, mario.bottomLine, ladderDownLeft, ladderDownRight):
            mario.ladderTop=False
            mario.ladderDown=True
            i+=1

    elif mario.ladderDown and not mario.die and not mario.finish:
        if i!=6:
            if keys[pygame.K_DOWN]:
                mario.topFrame=14
                mario.ladderDown=False
                mario.ladderTop=True
                mario.y+=2
                i-=1
            if keys[pygame.K_a]:
                mario.ladderDown=False
                mario.left=True
            elif keys[pygame.K_d]:
                mario.ladderDown=False
                mario.right=True

            if keys[pygame.K_w]:
                mario.ladderDown=False
                mario.jump=True
                mario.still=True
                mario.left=True

            if mario.bottomLine.collidelist(rectsList[i])==-1:
                mario.y+=2

        else:
            mario.ladderDown=False
            mario.left=True
            mario.still=True
            mario.finish=True

    elif falling and not mario.die and not mario.finish:
        if mario.bottomLine.collidelist(rectsList[i-1])==-1:
            mario.y+=16
        else:
            mario.y-=4
            falling=False

    if not mario.die and not mario.finish:
        for barrel in barrels:
            if not barrel.isLadder and not barrel.isFall:
                barrel.x+=barrel.vel

            elif barrel.isFall and not barrel.isLadder:
                barrel.x+=barrel.vel/4

            if not barrel.isFall and not barrel.isLadder:
                if barrel.bottomLine.collidelist(rectsList[barrel.i])==-1:
                    if barrel.i==1 or barrel.i==3 or barrel.i==5:
                        if barrel.x>=884:
                            barrel.isFall=True

                        barrel.vel=8

                    elif barrel.i==0 or barrel.i==2 or barrel.i==4:
                        if barrel.x<=52 and barrel.i!=0:
                            barrel.isFall=True

                        elif barrel.i==0:
                            if barrel.x<=192:
                                barrels.pop(barrels.index(barrel))

                        barrel.vel=-8

                    barrel.y+=4

                if ladderCheck(2,2,barrel.bottomLine,ladderDownLeft,ladderDownRight):
                    if random.choice(ladderDieRoll)==1:
                        barrel.isLadder=True

                elif ladderCheck(2,2,barrel.bottomLine,brokenLadderLeft,brokenLadderRight):
                    if random.choice(brokenLadderDieRoll)==1:
                        barrel.isLadder=True

            elif barrel.isFall and not barrel.isLadder:
                if barrel.bottomLine.collidelist(rectsList[barrel.i-1])!=-1:
                    barrel.i-=1
                    barrel.vel=-barrel.vel
                    barrel.isFall=False

                else:
                    barrel.y+=8

            elif barrel.isLadder:
                if barrel.bottomLine.collidelist(rectsList[barrel.i-1])==-1:
                    barrel.y += 4

                else:
                    barrel.i -= 1
                    barrel.vel=-barrel.vel
                    barrel.isLadder = False

            if barrel.hitbox.colliderect(mario.hitbox):
                mario.die=True

                for barrel in barrels:
                    barrel.kill=True

        if spawnCount==131:
            spawnCount=0
            barrels.append(aBarrel(308, 164))
        elif not mario.finish:
            spawnCount += 1

        if dkCount==131:
            dkCount=0
        elif not mario.finish:
            dkCount += 1

        if paulineCount==63:
            paulineCount=0
        elif not mario.finish:
            paulineCount+=1

        if mario.hitbox.colliderect(donkeyRect):
            mario.die=True

    if mario.die and not mario.finish:
        if mario.numSpins==4:
            pygame.time.delay(1500)
            mario.death()
            barrels.clear()
            falling = False
            spawnCount=85
            dkCount=0
            paulineCount=0

    screenUpdate()

pygame.quit()