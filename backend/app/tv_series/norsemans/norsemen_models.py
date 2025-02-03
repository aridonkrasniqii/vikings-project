from django.db import models

from tv_series.base.models.base_models import VikingBase
from tv_series.norsemans.norsemen_managers import NorsemenManager


class Norseman(VikingBase):
    actor_name = models.CharField(max_length=255)
    description = models.TextField()

    objects = NorsemenManager()

    class Meta:
        db_table = 'norsemans'

    def __str__(self):
        return self.name
