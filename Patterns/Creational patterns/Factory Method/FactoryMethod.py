from abc import ABC, abstractmethod

"""Реализуем интерфейс карт"""
class IBankCard(ABC):
    @abstractmethod
    def card_method():
        pass
    
"""Класс белой карты"""
class WhiteCard(IBankCard):
    
    def __init__(self):
        self.cardtype = "White"
        
    def card_method(self):
        print(f"i am {self.cardtype} card")
        
"""Класс черной карты"""
class BlackCard(IBankCard):
        
    def __init__(self):
        self.cardtype = "Black"
        
    def card_method(self):
        print(f"i am {self.cardtype} card")

"""Класс фабрики для карт"""
class CardFactory:
    
    def create_card(cardtype):
        if cardtype.lower().strip() in ["w", "white"]:
            return WhiteCard()
        if cardtype.lower().strip() in ["b", "black"]:
            return BlackCard()
        print ("Invalid card type")
        return None
        
        
if __name__ == "__main__":
    cardtype = input("What card do you want? black(b) or white(w)?\n")
    card = CardFactory.create_card(cardtype)
    card.card_method()