from pages.newpurchase import NewPurchase
from pages.productlist import ProductList
from pages.start_menu_screen import StartMenuScreen
from pages.start_screen import StartScreen


class App:
    def __init__(self):
        self.current_display = "start"

    def get_next(self) -> None:
        if self.current_display == "start":
            return StartScreen(on_key_pressed=self.go_to_start_menu).render()
        if self.current_display == "start menu":
            return StartMenuScreen(on_option_selected=self.go_to_start_menu_option).render()
        if self.current_display=="productlist":
            return ProductList(on_option_selected=self.go_to_categories).render()
        if self.current_display=="newpurchase":
            return NewPurchase(on_form_completed=self.go_to_invoice).render()

    def has_more(self) -> bool:
        return self.current_display != "exit"

    def exit(self):
        self.current_display = "exit"

    def go_to_start_menu(self):
        self.current_display = "start menu"

    def go_to_start_menu_option(self, option: int):
        if option==1:
            self.current_display="productlist"
        if option==2:
            self.current_display="newpurchase"
        else: 
            self.current_display="exit"
    def go_to_categories(self,option:int):
        print(f"option: {option}")
        self.exit()
    def go_to_invoice(self,product,quantity,paymethod):
        print(f"purchase: {product}-{quantity}-{paymethod}")
        self.exit()



    def run(self):
        while self.has_more():
            self.get_next()
