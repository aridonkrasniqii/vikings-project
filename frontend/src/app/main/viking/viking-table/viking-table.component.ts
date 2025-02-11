import { Component, OnInit, AfterViewInit } from '@angular/core';
import { VikingService } from '../../../services/viking.service';

import { PaginatedEntity } from '../../../interfaces/paginated.entity.interface';
import { BackendViking, FrontendViking } from '../../../models/viking.model';
import { PaginationParams } from '../../../interfaces/pagination-params.inteface';

@Component({
  standalone: false,
  selector: 'app-viking-table',
  templateUrl: './viking-table.component.html',
  styleUrls: ['./viking-table.component.css']
})
export class VikingTableComponent implements OnInit, AfterViewInit {
  displayedColumns: string[] = ['picture', 'actorName', 'characterName', 'description', 'actions'];
  dataSource: FrontendViking[] = [];
  searchTerm: string = '';
  totalItems = 0;
  itemsPerPage = 10;
  currentPage = 1;
  sortField: string = '';
  sortDirection: string = '';

  constructor(private vikingService: VikingService) {}

  ngOnInit(): void {
    this.getVikings();
  }

  ngAfterViewInit(): void {}

  getVikings(): void {
    const params = this.getParams();
    this.vikingService.getVikings(params)
      .subscribe((response: PaginatedEntity<BackendViking>) => {
        if (response) {
          this.dataSource = response.data.map(backendViking => FrontendViking.fromBackend(backendViking));
          this.totalItems = response.total_items;
        } else {
          console.warn('No response received');
        }
      });
  }

  getParams(): PaginationParams {
    return {
      page: this.currentPage,
      limit: this.itemsPerPage, 
      q: this.searchTerm
    }
  }

  deleteViking(id: number): void {
    this.vikingService.deleteViking(id).subscribe(() => {
      this.dataSource = this.dataSource.filter(viking => viking.id !== id);
      this.totalItems = this.dataSource.length;
      this.getVikings(); // Refresh the data after deletion
    });
  }

  applyFilter(): void {
    this.currentPage = 1; // Reset to the first page
    this.getVikings();
  }

  handlePageChange(page: number): void {
    this.currentPage = page;
    this.getVikings();
  }
}
