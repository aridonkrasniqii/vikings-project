
from api.base.managers import BaseManager

class NorsemenManager(BaseManager):
    def get_paginated_norsemen(self, request, view):
        return self.get_paginated_models(request, view)

    def get_norseman_by_id(self, norseman_id):
        return self.get_model_by_id(norseman_id)

    def create_norseman(self, data):
        return self.create_model(**data)

    def update_norseman(self, norseman_id, data):
        return self.update_model(norseman_id, data)

    def delete_norseman(self, norseman):
        return self.delete_model(norseman)
