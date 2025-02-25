import datetime
from typing import Optional

import strawberry_django

from superapp.apps.authentication.models import User


@strawberry_django.type(User, fields="__all__")
class UserType:
    email_verified = Optional[datetime.datetime]
    phone_verified = Optional[datetime.datetime]
    can_view_quote_materials: bool


