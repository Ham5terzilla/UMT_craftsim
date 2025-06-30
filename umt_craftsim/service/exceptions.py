"""
Custom exceptions for the crafting system's item processing and validation.

This module defines a hierarchy of exceptions for handling errors related to
item transformations, validation, and processing. The base class `ItemError`
provides a foundation for more specific exceptions.

Exceptions:
    ItemError: Base exception for all item-related errors.
    ItemProcessingError: Errors encountered during item processing.
    ItemValidationError: Validation-related errors during item operations.
    InvalidItemTypeError: Raised when an item has an unexpected type.
    TagConflictError: Raised when tag operations cause conflicts.
    TagMissingError: Raised when a required tag is missing from an item.
"""


class ItemError(Exception):
    """
    Base exception for all item-related errors in the crafting system.

    Attributes:
        messag (str): Explanation of the error.
        item (Item): The Item instance involved in the error. Defaults to None.
    """

    def __init__(self, message="Item processing error", item=None):
        self.message = message
        self.item = item
        super().__init__(self.message)

    def __str__(self):
        if self.item:
            return f"{self.message} (Item: {self.item})"
        return self.message


class ItemProcessingError(ItemError):
    """
    Exception raised for errors during item processing operations.

    This includes failures during crafting transformations, machine processing,
    or other runtime operations on items.

    Attributes:
        message (str): Explanation of the error.
        item (Item): The Item instance involved in the error. Defaults to None.
    """


class ItemValidationError(ItemError):
    """
    Exception raised for validation-related errors with items.

    Used when item data fails validation checks before processing.

    Attributes:
        message (str): Explanation of the error.
        item (Item): The Item instance involved in the error. Defaults to None.
    """


class InvalidItemTypeError(ItemValidationError):
    """
    Exception raised when an item has an unexpected or invalid type.

    Attributes:
        expected (str): The expected item type(s).
        actual (str): The actual item type encountered. Defaults to None.
        item (Item): The Item instance involved in the error. Defaults to None.
    """

    def __init__(self, expected, actual, item=None):
        self.expected = expected
        self.actual = actual
        message = f"Excepted item type {expected}, got {actual}"
        super().__init__(message, item)


class TagMissingError(ItemValidationError):
    """
    Exception raised when a required tag is missing from an item.

    Attributes:
        tag (str): The required tag that is missing.
        item (Item): The Item instance involved in the error. Defaults to None.
    """

    def __init__(self, tag, item=None):
        self.tag = tag
        message = f"Required tag {tag} is missing"
        super().__init__(message, item)


class TagConflictError(ItemValidationError):
    """
    Exception raised when a prohibited tag is present on an item.

    Attributes:
        tag (str): The prohibited tag that is present.
        item (Item): The Item instance involved in the error. Defaults to None.
    """

    def __init__(self, tag, item=None):
        self.tag = tag
        message = f"Prohibited tag {tag} is present"
        super().__init__(message, item)
