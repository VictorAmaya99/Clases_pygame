import pygame

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Crear una ventana
screen = pygame.display.set_mode((800, 600))
screen.fill(WHITE)

# Coordenadas de los vértices del triángulo (x, y)
# Puedes ajustar estos valores para cambiar la forma y el tamaño del triángulo
vertices = [
    (400, 100),  # Vértice superior
    (300, 200),  # Vértice inferior izquierdo
    (500, 200)   # Vértice inferior derecho
]

# Dibujar un triángulo rojo usando draw.polygon
pygame.draw.polygon(screen, RED, vertices, 2)

# Actualizar la ventana
pygame.display.flip()

# Mantener la ventana abierta hasta que se cierre manualmente
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()