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

        self.field__date_joined = ext.ux.form.ExtDateTimeField(
            label=u'registration date',
            name='date_joined',
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
            self.field__date_joined,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
