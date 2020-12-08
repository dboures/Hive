import pygame as pg
import webbrowser

# helpful
# https://stackoverflow.com/questions/51580173/how-to-implement-button-interaction-for-main-menu-pygame

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
HOVER_COLOR = (50, 70, 90)

START = "START"
RULES = "RULES"
OPTIONS = "OPTIONS"

NEWGAME = "NEW GAME"
QUIT = "QUIT"


class StartButton:
    def __init__(self, text, rect):
        self.text = text
        self.rect = rect
        self.color = BLACK

    def run_if_clicked(self, pos, state):
        if self.rect.collidepoint(pos):
            if self.text == START:
                state.start_game()
                return
            elif self.text == OPTIONS:
                print('opts')
            elif self.text == RULES:
                open_rules()

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

def start_menu(screen, state, event):
    WIDTH, HEIGHT = screen.get_size()

    button_width = WIDTH / 4.5
    button_height = HEIGHT / 10
    button_pos = (WIDTH/2) - (button_width/2)

    rect1 = pg.Rect(button_pos, (3/9) * HEIGHT, button_width, button_height)
    rect2 = pg.Rect(button_pos, (4/9) * HEIGHT, button_width, button_height)
    rect3 = pg.Rect(button_pos, (5/9) * HEIGHT, button_width, button_height)

    buttons = [
        StartButton(START, rect1),
        StartButton(OPTIONS, rect2),
        StartButton(RULES, rect3),
    ]

    if event.type == pg.MOUSEMOTION:
        for button in buttons:
            button.highlight_if_hovered(event.pos)
    elif event.type == pg.MOUSEBUTTONDOWN:
        for button in buttons:
            button.run_if_clicked(event.pos, state)

    screen.fill((20, 50, 70))

    for button in buttons:
        button.draw(screen)

    pg.display.flip()

class EndButton:
    def __init__(self, text, pos):
        self.text = text

        font = pg.font.SysFont("Times New Norman", 90)
        self.FONT = font.render(self.text, True, (131,31,250))
        self.FONT.set_alpha(250)
        self.font_rect = self.FONT.get_rect(center=pos)

    def run_if_clicked(self, pos, state):
        if self.font_rect.collidepoint(pos):
            if self.text == NEWGAME:
                state.new_game()
                return
            elif self.text == QUIT:
                state.quit()
                return

    def draw(self, background):
        background.blit(self.FONT, self.font_rect)

def end_menu(screen, state, event):
    WIDTH, HEIGHT = 880, 900

    clear_surface = pg.Surface((WIDTH,HEIGHT))  
    clear_surface.set_alpha(5)         
    clear_surface.fill((255,255,255)) 
    buttons = [
        EndButton(NEWGAME, (WIDTH/2, HEIGHT/2)),
        EndButton(QUIT, (WIDTH/2, 0.65*HEIGHT))
        ]

    title_font = pg.font.SysFont("Times New Norman", 120)

    if state.winner == "WHITE":
        wins = title_font.render("White Wins!", True, (131,31,250))
    elif state.winner == "BLACK":
        wins = title_font.render("Black Wins!", True, (131,31,250))
    else:
        wins = title_font.render("Draw", True, (131,31,250))
    wins.set_alpha(250)
    wins_rect = wins.get_rect(center=(WIDTH/2, HEIGHT/8))


    if event.type == pg.MOUSEBUTTONDOWN:
        for button in buttons:
            button.run_if_clicked(event.pos, state)

    for button in buttons:
        button.draw(clear_surface)

    clear_surface.blit(wins, wins_rect)
    
    screen.blit(clear_surface, (0,0))  

    pg.display.flip()

def open_rules():
    webbrowser.open("https://www.ultraboardgames.com/hive/game-rules.php")
