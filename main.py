import pygame
import time
import random

# Inicialización
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True

# Variables del Juego
words = sorted([
    "gato", "perro", "elefante", "jirafa", "tigre", "leon", "rinoceronte", "hipopotamo",
    "casa", "auto", "barco", "tren", "avion", "bicicleta", "moto", "camion",
    "ventana", "puerta", "pared", "techo", "suelo", "mesa", "silla", "cama",
    "almohada", "lampara", "reloj", "computadora", "telefono", "television", 
    "raton", "teclado", "impresora", "escuela", "universidad"
], key=len)  # Ordenar por longitud
current_word = words.pop(0)  # Sacar la primera palabra de la lista
start_time = time.time()
correct_guesses = [0] * 4
team_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
game_duration = 50  # Duración del juego en segundos

# Función para mostrar el progreso de cada equipo
def display_team_progress():
    y_pos = 100
    for i in range(4):
        text = font.render(f"Equipo {i + 1}: {correct_guesses[i]}", True, team_colors[i])
        screen.blit(text, (100, y_pos))
        y_pos += 100

# Función para mostrar el cronómetro
def display_timer():
    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_duration - elapsed_time)
    timer_text = small_font.render(f"Tiempo restante: {int(remaining_time)}s", True, (0, 0, 0))
    screen.blit(timer_text, (550, 50))
    if remaining_time <= 10:  # Advertencia en los últimos 10 segundos
        warning_text = small_font.render("¡El juego está por terminar!", True, (255, 0, 0))
        screen.blit(warning_text, (500, 100))

# Bucle Principal del Juego
while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                correct_guesses[0] += 1
                current_word = words.pop(0) if words else ''
            elif event.key == pygame.K_2:
                correct_guesses[1] += 1
                current_word = words.pop(0) if words else ''
            elif event.key == pygame.K_3:
                correct_guesses[2] += 1
                current_word = words.pop(0) if words else ''
            elif event.key == pygame.K_4:
                correct_guesses[3] += 1
                current_word = words.pop(0) if words else ''

    display_team_progress()
    display_timer()
    
    if time.time() - start_time > game_duration:
        running = False

    pygame.display.flip()
    clock.tick(30)

# Mensaje de fin del juego
screen.fill((255, 255, 255))
end_text = font.render("¡El juego se ha terminado!", True, (0, 0, 0))
screen.blit(end_text, (200, 250))
pygame.display.flip()

# Mantener la pantalla de fin del juego abierta por 5 segundos
time.sleep(10)

pygame.quit()

print("¡El tiempo se acabó!")
ganador = correct_guesses.index(max(correct_guesses)) + 1
print(f"El equipo ganador es el equipo {ganador} con {max(correct_guesses)} palabras adivinadas.")
