"""
Validation and property utilities for crafting transformations.

Provides helper methods for:
- Type validation (single/multiple items)
- Tag presence/absence checks
- Property aggregation
"""

from umt_craftsim.dataclasses.items import Item
from umt_craftsim.service.exceptions import InvalidItemTypeError, TagConflictError, TagMissingError


class TransformationHelperMixin:
    """
    Shared validation and calculation helpers for transformations.

    All methods are static and don't require class instantiation.
    """

    @staticmethod
    def validate_type(item: Item, excepted_item_type: str):
        """
        Verify an item matches a specific expected type.

        Args:
            item (Item): Item to validate
            expected_item_type (str): Required item type constant (from ItemTypes)

        Raises:
            InvalidItemTypeError: If item type doesn't match expected type
        """
        if item.item_type != excepted_item_type:
            raise InvalidItemTypeError(excepted_item_type, item.item_type, item)

    @staticmethod
    def validate_multiple_items_types(items: list[Item], excepted_item_types: list[str]):
        """
        Verify no items in a list have any of the prohibited tags.

        Args:
            items (list[Item]): List of items to check
            tags (list[str]): List of prohibited tag constants

        Raises:
            TagConflictError: If any item contains any prohibited tag
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
        Verify an item does NOT have a specific tag.

        Args:
            item (Item): Item to check
            tag (str): Tag constant (from Tags) that should be absent

        Raises:
            TagConflictError: If the prohibited tag is present
        """
        if tag in item.tags:
            raise TagConflictError(tag, item)

    @staticmethod
    def validate_multiple_items_tags_absence(items: list[Item], tags: list[str]):
        """
        Verify no items in a list have any of the prohibited tags.

        Args:
            items (list[Item]): List of items to check
            tags (list[str]): List of prohibited tag constants

        Raises:
            TagConflictError: If any item contains any prohibited tag
        """
        for item in items:
            for tag in tags:
                if tag in item.tags:
                    raise TagConflictError(tag, item)

    @staticmethod
    def validate_tag_present(item: Item, tag: str):
        """
        Verify an item HAS a specific required tag.

        Args:
            item (Item): Item to check
            tag (str): Required tag constant (from Tags)

        Raises:
            TagMissingError: If the required tag is absent
        """
        if tag not in item.tags:
            raise TagMissingError(tag, item)

    @staticmethod
    def validate_multiple_items_tags_present(items: list[Item], tags: list[str]):
        """
        Verify all items have all required tags.

        Args:
            items (list[Item]): List of items to check
            tags (list[str]): List of required tag constants

        Raises:
            TagMissingError: If any item is missing any required tag
        """
        for item in items:
            for tag in tags:
                if tag not in item.tags:
                    raise TagMissingError(tag, item)

    @staticmethod
    def properties_totals(items: list[Item]) -> Item:
        """
        Aggregate properties from multiple items into a new summary item.

        Creates a new Item with:
        - Value: Sum of all item values
        - Materials: Sum of all material costs
        - Tags: Union of all unique tags
        - Sequence: List of all item sequences

        Args:
            items: List of items to aggregate

        Returns:
            Item: New item containing aggregated properties
        """
        return Item(
            value=sum(item.value for item in items),
            materials=sum(item.materials for item in items),
            tags=list(set(items[0].tags).union(*[item.tags for item in items[1:]])),
            sequence=[item.sequence for item in items],
        )
