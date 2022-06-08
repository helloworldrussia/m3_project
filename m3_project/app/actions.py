from django.contrib.auth.models import User, Group, Permission, PermissionManager
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from django.contrib.auth.models import Permission
from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext
from objectpack.ui import ModelEditWindow

from .models import PermissionProxy
from .ui import UserAddWindow, ContentTypeAddWindow, PermissionAddWindow


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


class GroupAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(GroupAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%'),

        self.field__permissions = make_combo_box(
            label=u'permissions',
            name='permissions',
            allow_blank=False,
            anchor='100%',
            data=list(Permission.objects.all().values_list('pk', 'codename')),
        )

        # self.field__permissions = ext.ExtComboBox(
        #     label='permissions',
        #     display_field='id',
        #     value_field='name',
        #     trigger_action=ext.BaseExtTriggerField.ALL
        # )
        # self.field__permissions.store = ext.ExtDataStore(
        #     # data=[(12, 'name'), (13, 'name2')]
        #     data=list(Permission.objects.all().values_list('pk', 'codename'))
        # )

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(GroupAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__permissions,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(GroupAddWindow, self).set_params(params)
        self.height = 'auto'

    def save_row(self, obj, create_new, request, context):
        print('+')
        permission = Permission.objects.get(pk=obj.permission)
        obj.permission = None
        super(GroupPack, self).save_row(obj, create_new, request, context)
        group = Group.objects.get(name=obj.name)
        group.permission.add(permission)
        print('++')


class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    can_delete = True

    add_window = edit_window = GroupAddWindow

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

    def prepare_row(self, obj, request, context):
        group = Group.objects.get(name=obj.name)
        obj.permissions.set(group.permissions.all())
        return obj


class ContentTypePack(ObjectPack):
    model = ContentType
    model_name = 'ContentType'
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

    @staticmethod
    def _get_model_pack(model_name):
        print('YES!!!!')
        return None


class PermissionPack(ObjectPack):
    model = PermissionProxy
    # parent = ContentTypePack
    relations = ['content_type']
    select_related = ['content_type']

    add_to_menu = True
    can_delete = True

    add_window = edit_window = ModelEditWindow.fabricate(model)

    columns = [
        # {
        #     'data_index': '__unicode__',
        #     'header': u'Наименование',
        # },
        {
            'data_index': 'name',
            'header': u'name',
        },
        {
            'data_index': 'content_type',
            'header': u'content_type',
        },
        {
            'data_index': 'codename',
            'header': u'codename',
        },
    ]
