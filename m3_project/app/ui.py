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

        self.field__last_name = ext.ExtStringField(
            label=u'email',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__date_joined = ext.ExtDateField(
            label=u'registration date',
            name='date_joined',
            anchor='100%')

        self.field__is_stuff = ext.ExtStringField(
            label=u'admin',
            name='is_stuff',
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
        super(PersonAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__surname,
            self.field__gender,
            self.field__birthday,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PersonAddWindow, self).set_params(params)
        self.height = 'auto'
