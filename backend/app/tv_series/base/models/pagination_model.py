from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Q

from tv_series.base.models.paginated_entity import PaginatedEntity


class PaginationModel(PageNumberPagination):
    PAGE_SIZE = 10
    LIMIT = 50
    page_query_param = 'page'
    page_size_query_param = 'limit'
    max_page_size = LIMIT

    def __init__(self, request):
        self.request = request
        self.search_fields = self.get_search_fields_from_request()
        self.q = request.GET.get('q', None)
        self.asc = request.GET.get('asc', None)
        self.desc = request.GET.get('desc', None)
        self.page = None
        self.paginator = None

        limit = request.GET.get('limit')
        if limit and limit.isdigit():
            self.page_size = min(int(limit), self.max_page_size)
        else:
            self.page_size = self.PAGE_SIZE

    def get_search_fields_from_request(self):
        search_fields_param = self.request.GET.get('search_fields', '')
        return search_fields_param.split(',') if search_fields_param else []

    def get_search_filters(self):
        if not self.q or not self.search_fields:
            return Q()
        search_query = Q()
        for field in self.search_fields:
            search_query |= Q(**{f"{field}__icontains": self.q})
        return search_query

    def get_ordering(self):
        if self.asc:
            return self.asc
        elif self.desc:
            return f"-{self.desc}"
        return "id"

    def paginate_queryset(self, queryset, request, view=None):
        self.paginator = self.django_paginator_class(queryset, self.get_page_size(request))
        page_number = self.get_page_number(request, self.paginator)

        try:
            self.page = self.paginator.page(page_number)
        except Exception:
            self.page = None

        return self.page

    def get_paginated_response(self, paginated_queryset):
        total_items = self.paginator.count if self.paginator else 0
        total_pages = self.paginator.num_pages if self.paginator else 1
        current_page = self.page.number if self.page else 1
        limit = self.page_size if self.page_size else self.PAGE_SIZE
        data = paginated_queryset.object_list if paginated_queryset else []

        return PaginatedEntity(
            total_items=total_items,
            total_pages=total_pages,
            current_page=current_page,
            limit=limit,
            data=data
        )



