from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack


class UserPack(ObjectPack):
    model = User
    add_to_menu = True


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True


class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True


class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True
