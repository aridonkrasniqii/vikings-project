from django.db import models

class BaseManager(models.Manager):
    def get_all(self):
        return self.all()

    def get_by_id(self, model_id):
        return self.filter(id=model_id).first()

    def create_model(self, instance):
        return self.create(**instance.__dict__)

    def update_model(self, instance):
        instance.save()
        return instance

    def delete_model(self, instance):
        instance.delete()
