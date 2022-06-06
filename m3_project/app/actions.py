from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack


class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    can_delete = True

    columns = [
        {
            'data_index': 'username',
            'header': u'username',
        },
        {
            'data_index': 'first_name',
            'header': u'first name',
        },
        {
            'data_index': 'email',
            'header': u'email',
        },
        {
            'data_index': 'username',
            'header': u'username',
        },
        {
            'data_index': 'is_staff',
            'header': u'admin',
        },
        {
            'data_index': 'is_active',
            'header': u'online',
        },
        {
            'data_index': 'date_joined',
            'header': u'registration date',
        },
    ]

    def prepare_row(self, obj, request, context):

        obj.is_active = '<div class="x-grid3-check-col%s"/>' % (
            '-on' if obj.is_active is True else '')

        obj.is_staff = '<div class="x-grid3-check-col%s"/>' % (
            '-on' if obj.is_staff is True else '')

        return obj


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True
    can_delete = True


class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    can_delete = True


class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True
    can_delete = True
