import { Component, OnInit } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { NorsemanService } from '../../../services/norseman.service';
import { PaginatedEntity } from '../../../interfaces/paginated.entity.interface';
import { BackendNorseman, FrontendNorseman } from '../../../models/norseman.model';
import { PaginationParams } from '../../../interfaces/pagination-params.inteface';

@Component({
  standalone: false,
  selector: 'app-norseman-table',
  templateUrl: './norseman-table.component.html',
  styleUrls: ['./norseman-table.component.css']
})
export class NorsemanTableComponent implements OnInit {
  displayedColumns: string[] = ['picture', 'actorName', 'characterName', 'description', 'actions'];
  dataSource: FrontendNorseman[] = [];
  searchTerm: string = '';
  totalItems = 0;
  itemsPerPage = 10;
  currentPage = 1; // Custom paginator starts from page 1
  sortField: string = '';
  sortDirection: string = '';

  constructor(private norsemanService: NorsemanService) {}

  ngOnInit(): void {
    this.getNorsemans();
  }

  getNorsemans(): void {
    const params = this.getParams();
    this.norsemanService.getNorsemans(params)
      .subscribe((response: PaginatedEntity<BackendNorseman>) => {
        if (response) {
          this.dataSource = response.data.map(backendNorseman => FrontendNorseman.fromBackend(backendNorseman));
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
  

  deleteNorseman(id: number): void {
    this.norsemanService.deleteNorseman(id).subscribe(() => {
      this.dataSource = this.dataSource.filter(norseman => norseman.id !== id);
      this.totalItems = this.dataSource.length;
      this.getNorsemans(); // Refresh the data after deletion
    });
  }

  applyFilter(): void {
    this.currentPage = 1; // Reset to the first page
    this.getNorsemans();
  }

  handlePageChange(page: number): void {
    this.currentPage = page;
    this.getNorsemans();
  }
}
