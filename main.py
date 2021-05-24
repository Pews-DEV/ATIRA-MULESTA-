import pygame
import random
from player import Player
from enemies import Enemies
from tiro import Tiro
from killzone import Zone
from missil import Misseis
from bosses import Boss
from laser import Laser

#Iciando o pygame 
pygame.init()

#Criando a janela
janela = pygame.display.set_mode([600, 480])

#Grupos
objectGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()
menuGroup = pygame.sprite.Group()
zoneGroup = pygame.sprite.Group()
overGroup = pygame.sprite.Group()


#BG GAME
bg1 = pygame.sprite.Sprite(objectGroup)
bg1.image = pygame.image.load("Sprites/Cenario.png")
bg1.rect = pygame.Rect(10, 20, 100, 100)

bg2 = pygame.sprite.Sprite(objectGroup)
bg2.image = pygame.image.load("Sprites/Cenario.png")
bg2.rect = pygame.Rect(10, 250, 100, 100)

bg3 = pygame.sprite.Sprite(objectGroup)
bg3.image = pygame.image.load("Sprites/Cenario.png")
bg3.rect = pygame.Rect(490, 20, 100, 100)

bg4 = pygame.sprite.Sprite(objectGroup)
bg4.image = pygame.image.load("Sprites/Cenario.png")
bg4.rect = pygame.Rect(490, 250, 100, 100)

#BG MENU
bgm = pygame.sprite.Sprite(menuGroup)
bgm.image = pygame.image.load("Sprites/Menu.png")
bgm.rect = bgm.image.get_rect()

#BG GAME OVER
bgo = pygame.sprite.Sprite(overGroup)
bgo.image = pygame.image.load("Sprites/Gameover.png")
bgo.rect = bgm.image.get_rect()



#Musica
pygame.mixer.music.load("Musica/Musica.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

#Variaveis de controle
clock = pygame.time.Clock() #Definiro "fps" do jogo
click = False
pontos = 0
gameMode = 1
vidaBoss = 0

#Função para apresentar a pontuação
def Pontos(): 
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render("Score : " + str(pontos), True, (255, 255, 255))
    janela.blit(score, (250, 20))
    
#Logica do game
def Game():
    
    pygame.display.set_caption("ATIRA MULESTA! - GAME - ") #Tela

    #Efeitos sonoros
    tiro = pygame.mixer.Sound("Musica/Tiro.wav")
    pygame.mixer.Sound.set_volume(tiro, 0.1)


    player = Player(objectGroup) #Criar o player
    

    #Loop principal
    global pontos
    global restart    # Variaveis globais
    global gameMode 
    global vidaBoss

    #Variaveis de controle em geral
    shot = True # controle do tiro
    pode = True # controle para spawnar o boss
    timer1 = 0
    timer2 = 0 #Timers para controlar tempo
    timer3 = 0
    timer4 = 0
    restart = 0
    gameMode = 3
    gameLoop = True
    
    if __name__ == "__main__":
        while gameLoop:
            clock.tick(60)

            for event in pygame.event.get():  # Essa linha captura os inputs
                if event.type == pygame.QUIT: #Input de fechar o game
                    gameMode = 1
                    gameLoop = False
                                
                elif event.type == pygame.KEYDOWN and shot: #Input SPACE
                    if event.key == pygame.K_SPACE:
                        tiro.play()
                        newShot = Tiro(objectGroup, shotGroup) #Cria o tiro se apertar SPACE
                        newShot.rect.center = player.rect.center
                        shot = False
                        


            objectGroup.update()
            timer1 += 1
            timer2 += 1     #Atualizadores
            timer3 += 1
            timer4 += 1
            restart += 1

            if restart == 1: # Restart
                zona = Zone(objectGroup, zoneGroup)
                zona.rect.center = player.rect.center


            #Spawn de inimigos simples
            if timer1 > 30:
                timer1 = 0
                shot = True
                if random.randint(1, 10) <= 3:
                    newEnemy = Enemies(objectGroup, enemyGroup)

            #Spawn de inimgos complexos
            if timer2 > 60:
                timer2 = 0
                if random.randint(1, 10) <= 1:
                    newMissil = Misseis(objectGroup, enemyGroup)

            #Boss
            if timer3 >= 1800 and vidaBoss == 0 and pode:
                pode = False
                vidaBoss = 10
                if vidaBoss == 10:
                    newBoss = Boss(objectGroup, zoneGroup)

            #Laser do boss
            if timer4 > 60 and not pode:
                timer4 = 0
                print("opa")
                laser = Laser(objectGroup, enemyGroup)
                #laser.rect.center = 
                
                    

            #Verifica colisão de sprites (sprite do palyer com sprites do enemyGroup)
            collisions = pygame.sprite.spritecollide(player, enemyGroup, True, pygame.sprite.collide_mask)

            if collisions: # Se colidir, morre, game over e tal
                print("Game over")
                player.kill()
                if not pode:
                    newBoss.kill()
                gameover()
                gameLoop = False
                

            #Colisões de gupo, as variaveis boleanas nas colisões servem pra dizer se o objeto vai ser ou não destruido
            hits = pygame.sprite.groupcollide(shotGroup, enemyGroup, True, True, pygame.sprite.collide_mask)
            zoo = pygame.sprite.groupcollide(zoneGroup, enemyGroup, False, True, pygame.sprite.collide_mask)

            if hits: #Se acertar algum inimigo, conta ponto
                pontos += 1


            # Acertar o boss
            bossHit = pygame.sprite.groupcollide(shotGroup, zoneGroup, True, False)
            if bossHit:
                if bossHit and vidaBoss > 0:
                    vidaBoss -= 1
                    
                elif vidaBoss == 0:
                    newBoss.kill()
                    vidaBoss = 1


            #Atualizadores da tela e de pontos
            janela.fill([0, 0, 0])
            objectGroup.draw(janela)
            Pontos()
            pygame.display.update()


#Função de menu
#Tudo nessa função serve para apresentar a tela de menu
def Menu():
    global restart
    global pontos
    
    while True:
        
        pygame.display.set_caption("ATIRA MULESTA! - MENU - ")
        janela.fill([0, 0, 0])
        

        mx, my = pygame.mouse.get_pos()# Posição do mouse

        button = pygame.Rect(200, 310, 190, 95)

        
        if button.collidepoint((mx, my)): #Se o mouse esta encima do botão
            if click: # se click, inicia o jogo
                Game()

        pygame.draw.rect(janela, (255, 0, 0), button)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  #Verificando e acianando o click
                print("Antes")
                if event.button == 1:
                    print("Funcionou")
                    restart = 0
                    pontos = 0
                    click = True
                    
                

        menuGroup.draw(janela)
        clock.tick(60)              #Atualizadores
        pygame.display.update()
        

def gameover(): #A tela de game over

    global restart
    global pontos
    gameLoop = True
    while gameLoop:
        
        janela.fill([0, 0, 0])
        overGroup.draw(janela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
        
        clock.tick(60)
        pygame.display.update()

    
#Chamando a função de menu, serve pra iniciar o game em si
Menu()










