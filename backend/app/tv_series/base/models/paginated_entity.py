
class PaginatedEntity:
    def __init__(self, total_items, total_pages, current_page, limit, data):
        self.total_items = total_items
        self.total_pages = total_pages
        self.current_page = current_page
        self.limit = limit
        self.data = data
