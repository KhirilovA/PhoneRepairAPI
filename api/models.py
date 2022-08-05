from django.db import models
from django.contrib.auth.models import (UserManager,
                                        AbstractUser)
from django.utils.translation import gettext_lazy as _

from .validators import PhoneNumberValidator


class User(AbstractUser):
    username_validator = PhoneNumberValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. This should be your Phone number, for example: +380632737373'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    last_activity = models.DateField(auto_now=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username


class Request(models.Model):
    CHOICES = (
        (1, 'Not started'),
        (2, 'In progress'),
        (3, 'Done')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_model = models.CharField(max_length=63)
    description = models.TextField(max_length=255)
    status = models.PositiveSmallIntegerField(choices=CHOICES, default=1)

    def __str__(self):
        return f'{self.phone_model} - {self.user}'

class Invoice(models.Model):
    CHOICES = (
        (1, 'No'),
        (2, 'Yes')
    )

    request = models.OneToOneField(Request, on_delete=models.CASCADE, limit_choices_to={'status': 3})
    price = models.IntegerField()
    paid = models.PositiveSmallIntegerField(choices=CHOICES, default=1)
