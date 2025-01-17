from typing import List
from project import DVD


class Customer:

    def __init__(self, name, age, _id):
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's " \
               f"({', '.join(str(d.name) for d in self.rented_dvds)})"
