from tv_series.base.models.pagination_model import PaginationModel
from django.db import models  # Ensure correct import

class BaseManager(models.Manager):

    def get_paginated_models(self, request, view):
        paginator = PaginationModel(request)
        queryset = self.get_all_models()

        search_filter = paginator.get_search_filters()
        if search_filter:
            queryset = queryset.filter(search_filter)

        ordering = paginator.get_ordering()
        queryset = queryset.order_by(ordering)

        paginated_queryset = paginator.paginate_queryset(queryset, request, view)
        return paginator.get_paginated_response(paginated_queryset)


    def get_all_models(self):
        return self.all()

    def get_model_by_id(self, model_id):
        return self.filter(id=model_id)

    def create_model(self, **kwargs):
        return self.create(**kwargs)

    def update_model(self, instance):
        instance.save()
        return self.get_model_by_id(instance.id)

    def delete_model(self, instance):
        instance.delete()
