from abc import ABC, abstractmethod

"""Интерфейс маленького помощника"""
class ILittlePet(ABC):
    
    @abstractmethod
    def find_food(self) -> str:
        pass

"""Интерфейс среднего помощника"""
class IMediumPet(ABC):
    
    @abstractmethod
    def heal(self) -> str:
        pass
    
"""Интерфейс большого помощника"""
class IBigPet(ABC):
    
    @abstractmethod
    def attack(self) -> str:
        pass
    
"""Интерфейс фабрики создания помощников"""
class IPetCreator(ABC):
    
    @abstractmethod
    def create_little_pet(self) -> ILittlePet:
        pass
    
    @abstractmethod
    def create_medium_pet(self) -> IMediumPet:
        pass
    
    @abstractmethod
    def create_big_pet(self) -> IBigPet:
        pass
    
"""Фабрика водяных помощников"""
class WaterPetCreator(IPetCreator):
    
    def create_little_pet() -> ILittlePet:
        return LittleWaterPet()
    
    def create_medium_pet() -> IMediumPet:
        return MediumWaterPet()
    
    def create_big_pet() -> IBigPet:
        return BigWaterPet()
    
"""Фабрика наземных помощников"""
class EarthPetCreator(IPetCreator):
    
    def create_little_pet() -> ILittlePet:
        return LittleEarthPet()
    
    def create_medium_pet() -> IMediumPet:
        return MediumEarthPet()

    def create_big_pet() -> IBigPet:
        return BigEarthPet()

"""Фабрика воздушных помощников"""    
class WindPetCreator(IPetCreator):
    
    def create_little_pet() -> ILittlePet:
        return LittleWindPet()
    
    def create_medium_pet() -> IMediumPet:
        return MediumWindPet()
    
    def create_big_pet() -> IBigPet:
        return BigWindPet()

"""Реализация маленького водяного помощника"""
class LittleWaterPet(ILittlePet):
    
    def find_food(self) -> str:
        return "Bulp.. i found 1 fish!"

"""Реализация маленького наземного помощника"""
class LittleEarthPet(ILittlePet):
    
    def find_food(self) -> str:
        return "Bghb.. i found 1 apple!"
    
"""Реализация маленького наземного помощника"""
class LittleWindPet(ILittlePet):
    
    def find_food(self) -> str:
        return "Bghb.. i found 1 bird!"
    
"""Реализация среднего водяного помощника"""
class MediumWaterPet(IMediumPet):
    
    def heal(self) -> str:
        return "Bulp.. WATER HEAL!"

"""Реализация среднего наземного помощника"""
class MediumEarthPet(IMediumPet):
    
    def heal(self) -> str:
        return "Bghb.. EARTH HEAL!"
    
"""Реализация среднего наземного помощника"""
class MediumWindPet(IMediumPet):
    
    def heal(self) -> str:
        return "Bghb.. WIND HEAL!"
    
"""Реализация большого водяного помощника"""
class BigWaterPet(IBigPet):
    
    def attack(self) -> str:
        return "Bulp.. WATER ATTACK!"

"""Реализация большого наземного помощника"""
class BigEarthPet(IBigPet):
    
    def attack(self) -> str:
        return "Bghb.. EARTH ATTACK!"
    
"""Реализация большого наземного помощника"""
class BigWindPet(IBigPet):
    
    def attack(self) -> str:
        return "Bghb.. WIND ATTACK!"
    
def create_pets(factory: IPetCreator) -> None:
    little_pet = factory.create_little_pet()
    print(little_pet.find_food())
    
    medium_pet = factory.create_medium_pet()
    print(medium_pet.heal())
    
    big_pet = factory.create_big_pet()
    print(big_pet.attack())
    
if __name__ == "__main__":
    print("Test water pets:\n")
    create_pets(WaterPetCreator)
    
    print("Test earth pets:\n")
    create_pets(EarthPetCreator)
    
    print("Test wind pets:\n")
    create_pets(WindPetCreator)