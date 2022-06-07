from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models

from objectpack.models import ModelProxy


class PermissionProxy(ModelProxy):
    model = Permission
    relation = ContentType
