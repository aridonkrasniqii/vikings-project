import { Component, Output, EventEmitter, Input } from '@angular/core';

@Component({
  standalone: false,
  selector: 'app-custom-paginator',
  templateUrl: './custom-paginator.component.html',
  styleUrls: ['./custom-paginator.component.css']
})
export class CustomPaginatorComponent {
  @Input() totalItems: number;
  @Input() itemsPerPage: number;
  @Input() currentPage: number;
  @Output() pageChange: EventEmitter<number> = new EventEmitter<number>();

  get totalPages(): number {
    return Math.ceil(this.totalItems / this.itemsPerPage);
  }

  previousPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.pageChange.emit(this.currentPage);
    }
  }

  nextPage(): void {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
      this.pageChange.emit(this.currentPage);
    }
  }

  get displayRangeStart(): number {
    return (this.currentPage - 1) * this.itemsPerPage + 1;
  }

  get displayRangeEnd(): number {
    return Math.min(this.currentPage * this.itemsPerPage, this.totalItems);
  }
}
