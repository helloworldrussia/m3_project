from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack

from objectpack.ui import ModelEditWindow

from .ui import UserAddWindow, ContentTypeAddWindow, GroupAddWindow, PermissionAddWindow


class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    can_delete = True

    add_window = edit_window = UserAddWindow

    columns = [
        {
            'data_index': 'username',
            'header': u'username',
        },
        {
            'data_index': 'first_name',
            'header': u'first_name',
        },
        {
            'data_index': 'last_name',
            'header': u'last_name',
        },
        {
            'data_index': 'email',
            'header': u'email',
        },
        {
            'data_index': 'is_staff',
            'header': u'is_staff',
        },
        {
            'data_index': 'is_active',
            'header': u'is_active',
        },
        {
            'data_index': 'date_joined',
            'header': u'date_joined',
        },
    ]


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True
    can_delete = True

    add_window = edit_window = ModelEditWindow.fabricate(model)

    columns = [
        {
            'data_index': 'app_label',
            'header': u'app_label',
        },
        {
            'data_index': 'model',
            'header': u'model',
        },
    ]


class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    can_delete = True

    add_window = edit_window = ModelEditWindow.fabricate(model)

    columns = [
        {
            'data_index': 'name',
            'header': u'name',
        },
        {
            'data_index': 'permissions',
            'header': u'permissions',
        },
    ]


class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True
    can_delete = True

    add_window = edit_window = PermissionAddWindow

    columns = [
        {
            'data_index': 'name',
            'header': u'Имя',
        },
        {
            'data_index': 'content_type',
            'header': u'Content Type',
        },
        {
            'data_index': 'codename',
            'header': u'Кодовое имя',
        },
    ]