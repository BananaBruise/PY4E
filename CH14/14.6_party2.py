class PartyAnimal:

    def __init__(self) -> None:
        self.x = 0 # this is how python define class attribute

    def party(self) -> None:
        self.x = self.x + 1
        print("So far", self.x)
    
an = PartyAnimal() # constructor calls __init__
an.party()
an.party()
an.party()