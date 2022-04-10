from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


ONLY_LETTERS_VALIDATION_ERROR = "Ensure this value contains only letters."


def only_letters_validator(value):
    if value.isalpha():
        return None
    raise ValidationError(ONLY_LETTERS_VALIDATION_ERROR)


@deconstructible
class MaxSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        megabyte_limit = self.max_size
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError(f"Max file size is {self.max_size:.2f} MB")

