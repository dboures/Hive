import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HOVER_COLOR = (50, 70, 90)

START = "START"
RULES = "RULES"
OPTIONS = "OPTIONS"

class Button:
    def __init__(self, text, rect):
        self.text = text
        self.rect = rect
        self.color = BLACK

    def run_if_clicked(self, pos):
        if self.rect.collidepoint(pos):
            if self.text == START:
                print('start')
            elif self.text == OPTIONS:
                print('opts')
            elif self.text == RULES:
                print('rules')
        
    def highlight_if_hovered(self, pos):
        if self.rect.collidepoint(pos):
            self.color = HOVER_COLOR
        else:
            self.color = BLACK

    def draw(self, background):
        FONT = pg.font.SysFont("Times New Norman", 60)
        font = FONT.render(self.text, True, WHITE)

        pg.draw.rect(background, self.color, self.rect)
        background.blit(font, self.rect)



def start_menu(screen):
    WIDTH,HEIGHT = screen.get_size()

    button_width = WIDTH / 4.5
    button_height = HEIGHT / 10
    button_pos = (WIDTH/2) - (button_width/2)

    rect1 = pg.Rect(button_pos,(3/9) * HEIGHT ,button_width,button_height)
    rect2 = pg.Rect(button_pos,(4/9) * HEIGHT,button_width,button_height)
    rect3 = pg.Rect(button_pos,(5/9) * HEIGHT,button_width,button_height)

    buttons = [
    Button(START, rect1),
    Button(OPTIONS, rect2),
    Button(RULES, rect3),
    ]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.MOUSEMOTION:
                for button in buttons:
                    button.highlight_if_hovered(event.pos)
            elif event.type == pg.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.run_if_clicked(event.pos)

        screen.fill((20, 50, 70))

        for button in buttons:
            button.draw(screen)

        pg.display.flip()
