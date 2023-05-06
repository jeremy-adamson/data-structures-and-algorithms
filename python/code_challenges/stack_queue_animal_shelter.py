from data_structures.queue import Queue


class AnimalShelter(Queue):
    def enqueue(self, animal):
        if animal.species == "dog" or animal.species == "cat":
            super().enqueue(animal)
        else:
            return None

    def dequeue(self, pref = None):

        if not self.peek():
            return None
        if pref == None:
            animal = super().dequeue()
            return animal
        if pref == "dog":
            if self.front.value.species == "dog":
                animal = super().dequeue()
                return animal

            animal = self.front
            prev_animal = None

            while not animal.value.species == "dog":
                prev_animal = animal
                animal = animal.next
                if animal == None:
                    return None

            prev_animal.next = animal.next
            return animal.value

        if pref == "cat":
            if self.front.value.species == "cat":
                animal = super().dequeue()
                return animal

            animal = self.front
            prev_animal = None

            while not animal.value.species == "cat":
                prev_animal = animal
                animal = animal.next
                if animal == None:
                    return None

            prev_animal.next = animal.next
            return animal.value

        return None



class Animal:
    def __init__(self, name=None):
        self.name = name
        self.species = None

class Dog(Animal):
    def __init__(self, name = None):
        Animal.__init__(self, name)
        self.species = "dog"

class Cat(Animal):
    def __init__(self, name = None):
        Animal.__init__(self, name)
        self.species = "cat"




