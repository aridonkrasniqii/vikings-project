from tv_series.base.managers import BaseManager

class VikingManager(BaseManager):
    def get_all_vikings(self):
        return self.get_all()

    def get_viking_by_id(self, viking_id):
        return self.get_by_id(viking_id)

    def create_viking(self, viking):
        return self.create_model(viking)

    def update_viking(self, viking):
        return self.update_model(viking)

    def delete_viking(self, viking):
        return self.delete_model(viking)
