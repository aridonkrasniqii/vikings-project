
export interface PaginatedEntity<T> {
    total_items: number;
    total_pages: number;
    current_page: number;
    limit: number;
    data: T[];
}
