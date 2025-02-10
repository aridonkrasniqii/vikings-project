from django.db import models

from api.base.models.base_models import VikingBase
from api.vikings.vikings_manager import VikingManager

class Viking(VikingBase):
    actor_name = models.CharField(max_length=255)
    description = models.TextField()

    objects = VikingManager()

    class Meta:
        db_table = 'vikings'

    def __str__(self):
        return self.name
