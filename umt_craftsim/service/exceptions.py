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
"""

class ItemError(Exception):
    """
    Base exception for all item-related errors in the crafting system.

    Attributes:
        message: Explanation of the error.
        item: The Item instance involved in the error (optional).
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
    """Errors during item processing"""


class ItemValidationError(ItemError):
    """Validation-related errors"""


class InvalidItemTypeError(ItemValidationError):
    """Invalid item type"""

    def __init__(self, expected, actual, item=None):
        message = f"Excepted item type '{expected}', got '{actual}'"
        super().__init__(message, item)
        self.expected = expected
        self.actual = actual


class TagConflictError(ItemValidationError):
    """Tag conflict during processing"""

    def __init__(self, tag, item=None):
        message = f"Tag '{tag}' already exists or conflicts with existing tags"
        super().__init__(message, item)
        self.tag = tag
