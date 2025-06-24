from crafting_system.dataclasses.items import Item
from crafting_system.exceptions import InvalidItemTypeError, TagConflictError


class ValidationMixin:
    @staticmethod
    def validate_type(item: Item, expected_type: str):
        if item.item_type != expected_type:
            raise InvalidItemTypeError(expected_type, item.item_type, item)

    @staticmethod
    def validate_tag_absence(item: Item, tag: str):
        if tag in item.tags:
            raise TagConflictError(tag, item)

    @staticmethod
    def validate_tag_present(item: Item, tag: str):
        if tag not in item.tags:
            raise TagConflictError(tag, item)


class TransformationHelperMixin:
    @staticmethod
    def properties_totals(components: list[Item]) -> Item:
        """
        I'm shy of it >_<\n
        Might rework at some day. Or newer. Who knows.\n
        purpose of why it return Item instead of dict is cus I was unable to properly make type hint for this func
        """
        return Item(value=sum(item.value for item in components),
                    materials=sum(item.materials for item in components),
                    tags=list(set(components[0].tags).union(*[item.tags for item in components[1:]])),
                    sequence=[item.sequence for item in components])