from models.models import Sheep
from typing import Dict

class FakeDB:
    def __init__(self):
        self.data: Dict[int, Sheep] = {}

    def get_sheep(self, id: int) -> Sheep:
        return self.data.get(id)

    def add_sheep(self, sheep: Sheep) -> Sheep:
        if sheep.id in self.data:
            raise ValueError("Sheep with this ID exists")
        self.data[sheep.id] = sheep
        return sheep

db = FakeDB()

db.data = {
    1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe"),
    2: Sheep(id=2, name="Blondie", breed="Polypay", sex="ram")
}