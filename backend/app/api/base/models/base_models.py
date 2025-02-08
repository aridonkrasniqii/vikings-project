from django.db import models

class VikingBase(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
