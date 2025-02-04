import logging
from tv_series.base.managers import BaseManager
from tv_series.base.models.pagination_model import PaginationModel

logger = logging.getLogger(__name__)

class VikingManager(BaseManager):

    def get_paginated_vikings(self, request, view):
        return self.get_paginated_models(request, view)

    def get_viking_by_id(self, viking_id):
        return self.get_model_by_id(viking_id)

    def create_viking(self, viking):
        return self.create_model(**viking)

    def update_viking(self, viking):
        return self.update_model(**viking)

    def delete_viking(self, viking):
        return self.delete_model(viking)
