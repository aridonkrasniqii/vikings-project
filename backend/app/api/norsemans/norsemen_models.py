from django.db import models

from api.base.models.base_models import VikingBase
from api.norsemans.norsemen_managers import NorsemenManager


class Norseman(VikingBase):
    actor_name = models.CharField(max_length=255)
    description = models.TextField()

    objects = NorsemenManager()

    class Meta:
        db_table = 'norsemans'
        app_label = "api"

    def __str__(self):
        return self.name
