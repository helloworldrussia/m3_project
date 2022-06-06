from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__is_staff = ext.ExtStringField(
            label=u'admin',
            name='is_staff',
            allow_blank=False,
            anchor='100%')

        self.field__is_active = ext.ExtStringField(
            label=u'online',
            name='is_active',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_active,
            self.field__is_staff,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class ContentTypeAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(ContentTypeAddWindow, self)._init_components()

        self.field__app_label = ext.ExtStringField(
            label=u'Название приложения',
            name='app_label',
            allow_blank=False,
            anchor='100%')

        self.field__model = ext.ExtStringField(
            label=u'Модель',
            name='model',
            allow_blank=False,
            anchor='100%')

        self.field__objects = ext.ExtStringField(
            label=u'Объекты',
            name='objects',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(ContentTypeAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__app_label,
            self.field__model,
            self.field__objects,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(ContentTypeAddWindow, self).set_params(params)
        self.height = 'auto'


class GroupAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(GroupAddWindow, self)._init_components()

        self.field__app_label = ext.ExtStringField(
            label=u'Имя',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__model = ext.ExtStringField(
            label=u'Разрешения',
            name='permissions',
            allow_blank=False,
            anchor='100%')

        self.field__objects = ext.ExtStringField(
            label=u'Объекты',
            name='objects',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(GroupAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__peremissions,
            self.field__objects,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(GroupAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Имя',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__model = ext.ExtStringField(
            label=u'Content Type',
            name='content_type',
            allow_blank=False,
            anchor='100%')

        self.field__code_name = ext.ExtStringField(
            label=u'Кодовое имя',
            name='codename',
            allow_blank=False,
            anchor='100%')

        self.field__objects = ext.ExtStringField(
            label=u'Объекты',
            name='objects',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__code_name,
            self.field__objects,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'
