from crafting_system.dataclasses.items import Item
from crafting_system.transformations.transformations_single import Transformation_Single


class ItemBuilder:
    def __init__(self, item: Item):
        self.item = item
        self.transformations = []
    
    def add_transformation_single(self, transformation: Transformation_Single) -> 'ItemBuilder':
        self.transformations.append(transformation)
        return self
    
    def execute(self) -> Item:
        current_item = self.item
        for transformation in self.transformations:
            current_item = transformation.transform(current_item)
        return current_item