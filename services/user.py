from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


@transaction.atomic
def create_user(
    username: str,
    password: str = None,
    email: str = None,
    first_name: str = None,
    last_name: str = None,
):
    user = User.objects.create_user(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
    if password:
        user.set_password(password)
        user.save()
    return user


def get_user(user_id: int):
    return User.objects.get(id=user_id)


@transaction.atomic
def update_user(
    user_id: int,
    username: str = None,
    password: str = None,
    email: str = None,
    first_name: str = None,
    last_name: str = None,
):
    user = get_user(user_id)
    if username is not None:
        user.username = username
    if email is not None:
        user.email = email
    if first_name is not None:
        user.first_name = first_name
    if last_name is not None:
        user.last_name = last_name
    if password is not None:
        user.set_password(password)
    user.save()
    return user
