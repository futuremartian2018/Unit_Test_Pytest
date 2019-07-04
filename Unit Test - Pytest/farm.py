# CLASS REPRESENTING PETS

class Pets:

    # Constructor
    def __init__(self, kind, age, name):
        self.kind = kind
        self.age = age
        self._name = name
        self._hunger = 0

    # Hunger getter
    @property
    def hunger(self):
        return self._hunger

    # Hunger setter
    @hunger.setter
    def hunger(self, hunger):
        self._hunger = hunger

    # Check if your pet is hungry
    def hungry(self):
        if self._hunger < 75:
            return('Your animal is hungry! You should feed your {} !'.format(self.kind))
        return('Your {} is full and happy :)'.format(self.kind))

    # Feed your pet
    def feed(self, amount):
        self._hunger += amount
        self.hungry()

    # Time for sume fun :)
    def play(self, fun):
        self._hunger -= fun
        self.hungry()

    # Name getter
    @property
    def name(self):
        return self._name

    #Change your pets name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Basic information about your pet
    def info(self):
        if self.age > 1:
            return('My {}\'s name is {} and he is {} years old.'.format(self.kind, self._name, self.age))
        return('My {}\'s name is {} and he is 1 year old.'.format(self.kind, self._name))
        
    # Reading data about your animal from a JSON file ---------------------------------------------
    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'r') as f:
            line = f.readline()
            kind, name, age = line.split(',')
            age = age.rstrip()
        return cls(kind, name, age)


# CLASS REPRESENTING FARM ANIMALS

class FarmAnimals(Pets):
    
    # Constructor
    def __init__(self, kind, age, name, sound):
        super().__init__(kind, age, name)
        self.sound = sound

    # Check if your animal is angry
    @property
    def anger(self):
        if self._hunger < 75:
            print('This animal is angry!')
            return True
        print('This animal is happy for now!')
        return False

    # Animal makes a sound
    def makeSound(self):
        return ('{} does {}!'.format(self.kind, self.sound))
