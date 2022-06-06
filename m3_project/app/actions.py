from django.contrib.auth.models import User
from objectpack import ObjectPack


class UserPack(ObjectPack):
    model = User
    add_to_menu = True
