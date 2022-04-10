from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


from expenses_site.web.validators import only_letters_validator, MaxSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2

    BUDGET_DEFAULT = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_UPLOAD_DIR = 'profiles/'
    IMAGE_DEFAULT = '/staticfiles/images/user.png'
    IMAGE_MAX_SIZE_MB = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        )
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_DIR,
        null=True,
        blank=True,
        validators=(
            MaxSizeInMbValidator(IMAGE_MAX_SIZE_MB),
        )
    )


class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    expense_image = models.URLField()

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )
