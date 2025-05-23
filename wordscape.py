import pygame
import spacy
import random
import sys

nlp = spacy.load("en_core_web_sm")

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("WordScape - Generating Worlds from Words")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24)
input_text = ""
background_color = (0, 0, 0)
objects = []

visual_map = {
    "lake": "purple_lake",
    "mountain": "iphone_mountain",
    "iphone": "iphone_mountain",
    "animal": "animals",
    "animals": "animals",
    "caress": "animals",
    "fire": "firestorm",
    "tree": "forest",
    "sun": "sun",
    "cloud": "clouds",
    "car": "road",
    "ocean": "waves",
}

def draw_scene():
    screen.fill(background_color)
    for obj in objects:
        kind = obj["type"]
        x, y = obj["pos"]

        if kind == "purple_lake":
            pygame.draw.ellipse(screen, (150, 0, 255), (x, y, 200, 100))
        elif kind == "iphone_mountain":
            pygame.draw.polygon(screen, (100, 100, 100), [(x, y), (x+50, y-100), (x+100, y)])
        elif kind == "animals":
            pygame.draw.circle(screen, (255, 200, 150), (x, y), 25)
        elif kind == "firestorm":
            pygame.draw.circle(screen, (255, 80, 0), (x, y), 40)
        elif kind == "forest":
            pygame.draw.rect(screen, (34,139,34), (x, y, 20, 80))
        elif kind == "sun":
            pygame.draw.circle(screen, (255, 255, 0), (x, y), 40)
        elif kind == "clouds":
            pygame.draw.ellipse(screen, (200, 200, 200), (x, y, 120, 60))
        elif kind == "road":
            pygame.draw.rect(screen, (50, 50, 50), (x, y, 100, 20))
        elif kind == "waves":
            pygame.draw.arc(screen, (0, 191, 255), (x, y, 100, 50), 0, 3.14, 3)

    txt_surface = font.render("Narration: " + input_text, True, (255, 255, 255))
    screen.blit(txt_surface, (20, 560))

def update_scene(narration):
    global background_color, objects
    objects = []

    doc = nlp(narration.lower())
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    tone = "neutral"

    if any(word in narration for word in ["dark", "sad", "storm", "fire"]):
        tone = "dark"
    elif any(word in narration for word in ["love", "happy", "bright", "sun"]):
        tone = "bright"

    if tone == "dark":
        background_color = (30, 30, 60)
    elif tone == "bright":
        background_color = (255, 230, 200)
    else:
        background_color = (100, 100, 120)
        
    for noun in nouns:
        key = visual_map.get(noun)
        if key:
            for _ in range(random.randint(1, 3)):
                objects.append({
                    "type": key,
                    "pos": (random.randint(0, 900), random.randint(100, 500))
                })

running = True
while running:
    draw_scene()
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                update_scene(input_text)
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

pygame.quit()
sys.exit()
