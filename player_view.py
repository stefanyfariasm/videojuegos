import pygame
import random
import time

# Inicialización
pygame.init()
screen = pygame.display.set_mode((800, 500))
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
end_font = pygame.font.Font(None, 48)  # Fuente más pequeña para el mensaje final
clock = pygame.time.Clock()
running = True

words = sorted([
    "gato", "perro", "elefante", "jirafa", "tigre", "leon", "rinoceronte", "hipopotamo",
    "casa", "auto", "barco", "tren", "avion", "bicicleta", "moto", "camion",
    "ventana", "puerta", "pared", "techo", "suelo", "mesa", "silla", "cama",
    "almohada", "lampara", "reloj", "computadora", "telefono", "television", 
    "raton", "teclado", "impresora", "escuela", "universidad"
], key=len)  # Ordenar por longitud
current_word = words.pop(0)  # Sacar la primera palabra de la lista
input_text = ""
feedback = ""
start_time = time.time()
game_duration = 50  # Duración del juego en segundos
incorrect_feedback_time = None  # Para rastrear el tiempo de la respuesta incorrecta
correct_feedback_time = None  # Para rastrear el tiempo de la respuesta correcta

# Función para mostrar la palabra con la primera y última letra
def get_word_hint(word):
    if len(word) > 2:
        return word[0] + ' '.join(['_'] * (len(word) - 2)) + word[-1]
    return word

def display_input_and_word():
    screen.fill((255, 255, 255))
    word_text = font.render("Palabra actual: " + get_word_hint(current_word), True, (0, 0, 0))
    input_text_render = font.render("Tu respuesta: " + input_text, True, (0, 0, 0))
    
    feedback_text = None
    if feedback:
        if "incorrecta" in feedback and incorrect_feedback_time:
            if time.time() - incorrect_feedback_time <= 1.2:
                feedback_text = small_font.render(feedback, True, (255, 0, 0))
        elif "correcta" in feedback and correct_feedback_time:
            if time.time() - correct_feedback_time <= 1.2:
                feedback_text = small_font.render(feedback, True, (0, 128, 0))

    if feedback_text:
        screen.blit(feedback_text, (100, 400))  # Ajustado para que no interfiera

    screen.blit(word_text, (100, 150))  # Ajustar posición de la palabra
    screen.blit(input_text_render, (100, 250))  # Ajustar posición del input

def display_timer():
    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_duration - elapsed_time)
    timer_text = small_font.render(f"Tiempo restante: {int(remaining_time)}s", True, (0, 0, 0))
    screen.blit(timer_text, (550, 50))
    if remaining_time <= 10:  # Advertencia en los últimos 10 segundos
        warning_text = small_font.render("¡El juego está por terminar!", True, (255, 0, 0))
        screen.blit(warning_text, (500, 100))  # Mantener en la posición

while running:
    screen.fill((255, 255, 255))  # Limpiar la pantalla al principio del bucle
    display_input_and_word()
    display_timer()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.lower() == current_word:
                    feedback = "¡Respuesta correcta!"
                    current_word = words.pop(0) if words else ''
                    correct_feedback_time = time.time()  # Establecer tiempo para ocultar feedback correcto
                    incorrect_feedback_time = None  # Reiniciar temporizador de respuesta incorrecta
                else:
                    feedback = "¡Respuesta incorrecta!"
                    incorrect_feedback_time = time.time()  # Establecer tiempo para ocultar feedback incorrecto
                    correct_feedback_time = None  # Reiniciar temporizador de respuesta correcta
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    if time.time() - start_time > game_duration:
        running = False

    pygame.display.flip()
    clock.tick(30)

screen.fill((255, 255, 255))
end_text = end_font.render("¡El juego se ha terminado!", True, (0, 0, 0))
screen.blit(end_text, (200, 300))  # Ajustado para que se ajuste en la pantalla
pygame.display.flip()
time.sleep(10)

pygame.quit()
