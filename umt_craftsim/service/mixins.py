"""
Validation and property utilities for crafting transformations.

Provides helper methods for:
- Type validation (single/multiple items)
- Tag presence/absence checks
- Property aggregation
"""
from umt_craftsim.dataclasses.items import Item
from umt_craftsim.service.exceptions import InvalidItemTypeError, TagConflictError


class TransformationHelperMixin:
    """Shared validation and calculation helpers for transformations."""
    @staticmethod
    def validate_type(item: Item, excepted_item_type: str):
        """
        Verify item matches expected type.

        Args:
            item (Item): item for validation
            excepted_item_type (str): _description_

        Raises:
            InvalidItemTypeError: _description_
        """
        if item.item_type != excepted_item_type:
            raise InvalidItemTypeError(excepted_item_type, item.item_type, item)

    @staticmethod
    def validate_multiple_items_types(items: list[Item], excepted_item_types: list[str]):
        """
        for every item in items checking is it equal to at least one type in excepted_item_types\n
        otherwise raises exception
        """

        for item in items:
            b = False
            for excepted_item_type in excepted_item_types:
                if item.item_type == excepted_item_type:
                    b = True
            if not b:
                raise InvalidItemTypeError(excepted_item_types, item.item_type, item)

    @staticmethod
    def validate_tag_absence(item: Item, tag: str):
        """
        raise exception if item.tags contains tag
        """
        if tag in item.tags:
            raise TagConflictError(tag, item)

    @staticmethod
    def validate_multiple_items_tags_absence(items: list[Item], tags: list[str]):
        """
        raise exception if any of items contains any of tags
        """
        for item in items:
            for tag in tags:
                if tag in item.tags:
                    raise TagConflictError(tag, item)

    @staticmethod
    def validate_tag_present(item: Item, tag: str):
        """
        raise exception if item.tags doesn't contains tag
        """
        if tag not in item.tags:
            raise TagConflictError(tag, item)

    @staticmethod
    def validate_multiple_items_tags_present(items: list[Item], tags: list[str]):
        """
        raice exception if any of items doesn't contains any of tags
        """
        for item in items:
            for tag in tags:
                if tag not in item.tags:
                    raise TagConflictError(tag, item)

    @staticmethod
    def properties_totals(items: list[Item]) -> Item:
        """
        Return new Item with sumed properties of all items\n
        I'm shy of it >_<\n
        Might rework at some day. Or newer. Who knows.\n
        purpose of why it return Item instead of dict is cus I was unable to properly make type hint for this func
        """
        return Item(
            value=sum(item.value for item in items),
            materials=sum(item.materials for item in items),
            tags=list(set(items[0].tags).union(*[item.tags for item in items[1:]])),
            sequence=[item.sequence for item in items],
        )
