import pygame
import requests
import io

API_URL = "https://api.thecatapi.com/v1/images/search"

def get_random_cat():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["url"]
    return None

def show_cat_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_data = io.BytesIO(response.content)
        image = pygame.image.load(image_data)

        pygame.init()
        screen = pygame.display.set_mode(image.get_size())
        pygame.display.set_caption("Random Cat")

        screen.blit(image, (0, 0))
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

cat_url = get_random_cat()
if cat_url:
    show_cat_image(cat_url)
