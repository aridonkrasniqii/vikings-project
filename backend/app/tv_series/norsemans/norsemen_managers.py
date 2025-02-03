from tv_series.base.managers import BaseManager

class NorsemenManager(BaseManager):
    def get_all_norsemen(self):
        return self.get_all()

    def get_norseman_by_id(self, norseman_id):
        return self.get_by_id(norseman_id)

    def create_norseman(self, norseman):
        return self.create_model(norseman)

    def update_norseman(self, norseman):
        return self.update_model(norseman)

    def delete_norseman(self, norseman):
        return self.delete_model(norseman)
