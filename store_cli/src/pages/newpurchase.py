
from typing import Callable
from pages.screen import Screen


class NewPurchase(Screen):
    def __init__(self,on_form_completed:Callable[[str,int,str], None]) -> None:
        super().__init__()
        self.text=self.newpurchase()
        self.on_form_completed=on_form_completed
    def newpurchase(self):
        return """New Purchase:
        Ingresa tu articulo:
    """

    def render(self):
        try:
            product=input(self.text)
            quantity=int(input("cantidad: "))
            paymentmethod=input("metodo de pago: ")
            self.on_form_completed(product,quantity,paymentmethod)
        except ValueError:
            print ("La cantidad debe ser numerica")
            self.render()
    

    


