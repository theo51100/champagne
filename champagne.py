# Importez les bibliothèques nécessaires
import pygame

# Définissez les constantes
WIDTH = 640
HEIGHT = 480

# Créez une fenêtre Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Créez un bouchon de champagne
cork = pygame.Rect((0, 0), (32, 32))

# Créez une liste de bulles de champagne
bubbles = []

# Créez une boucle de jeu
while True:
    # Gérez les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Met à jour l'état du jeu
    update()

    # Dessinez l'écran
    draw()

    # Actualisez l'écran
    pygame.display.flip()

# Fonction de mise à jour
def update():
    # Déplacez le bouchon
    cork.y += 5

    # Créez de nouvelles bulles
    if len(bubbles) < 10:
        bubbles.append(pygame.Rect((random.randint(0, WIDTH), 0), (16, 16)))

    # Faites bouger les bulles
    for bubble in bubbles:
        bubble.y += 10

    # Supprimez les bulles qui ont atteint le bas de l'écran
    for i in range(len(bubbles) - 1, -1, -1):
        if bubbles[i].y > HEIGHT:
            bubbles.pop(i)

# Fonction de dessin
def draw():
    # Remplissez l'écran en blanc
    screen.fill((255, 255, 255))

    # Dessinez le bouchon
    pygame.draw.rect(screen, (0, 0, 0), cork)

    # Dessinez les bulles
    for bubble in bubbles:
        pygame.draw.rect(screen, (255, 0, 0), bubble)
