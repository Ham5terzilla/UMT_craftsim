class ItemError(Exception):
    """Base exception for all item-related errors"""

    def __init__(self, message="Item processing error", item=None):
        self.message = message
        self.item = item
        super().__init__(self.message)

    def __str__(self):
        if self.item:
            return f"{self.message} (Item: {self.item})"
        return self.message


class ItemValidationError(ItemError):
    """Validation-related errors"""


class InvalidItemTypeError(ItemValidationError):
    """Invalid item type"""

    def __init__(self, expected, actual, item=None):
        message = f"Expected item type '{expected}', got '{actual}'"
        super().__init__(message, item)
        self.expected = expected
        self.actual = actual


class TagConflictError(ItemValidationError):
    """Tag conflict during processing"""

    def __init__(self, tag, item=None):
        message = f"Tag '{tag}' already exists or conflicts with existing tags"
        super().__init__(message, item)
        self.tag = tag
