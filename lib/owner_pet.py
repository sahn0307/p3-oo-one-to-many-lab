class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be of type Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        type(self).all.append(self)