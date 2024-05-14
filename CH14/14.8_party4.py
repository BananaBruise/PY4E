class PartyAnimal:

    def __init__(self):
        self.x = 0
        print('Constructor')

    def party(self):
        self.x += 1
        print('So far', self.x)

    def __del__(self):
        print('Destructor', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42 # trigger desctructor on PartyAnimal instance
print('an contains', an)