class Game_State:
    def __init__(self):
        self.running = True
        self.menu_loop = True
        self.main_loop = False
        self.inventory_open = False

    def start_game(self):
        self.menu_loop = False
        self.main_loop = True

    def quit(self):
        self.running = False
        self.menu_loop = False
        self.main_loop = False


    def toggle_inventory(self): # really confusing naming here
        if self.inventory_open:
            self.inventory_open = False
        else:
            self.inventory_open = True