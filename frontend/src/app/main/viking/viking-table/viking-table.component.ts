import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { VikingService } from '../../../services/viking.service';
import { Viking } from '../../../interfaces/viking.interface';
import { PaginatedEntity } from '../../../interfaces/paginated.entity.interface';


@Component({
  standalone: false,
  selector: 'app-viking-table',
  templateUrl: './viking-table.component.html',
  styleUrls: ['./viking-table.component.css']
})
export class VikingTableComponent implements OnInit, AfterViewInit {
  displayedColumns: string[] = ['picture', 'actorName', 'characterName', 'description', 'actions'];
  dataSource = new MatTableDataSource<Viking>();
  searchTerm: string = '';
  totalItems = 0;
  itemsPerPage = 10;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private vikingService: VikingService) { }

  ngOnInit(): void {
    this.dataSource.filterPredicate = (data: Viking, filter: string) => {
      const transformedFilter = filter.trim().toLowerCase();
      const actorName = data.actorName.trim().toLowerCase();
      const characterName = data.name.trim().toLowerCase();
      const description = data.description.trim().toLowerCase();

      return actorName.includes(transformedFilter) || 
             characterName.includes(transformedFilter) || 
             description.includes(transformedFilter);
    };

    this.getVikings(0, this.itemsPerPage);
  }

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  getVikings(pageIndex: number, pageSize: number): void {
    this.vikingService.getVikings(pageIndex, pageSize).subscribe((response: PaginatedEntity<Viking>) => {
      if (response) {
        console.log('Received vikings:', response.data);
        this.dataSource.data = response.data;
        this.totalItems = response.total_items;
      } else {
        console.warn('No response received');
      }
    });
  }
  

  deleteViking(id: number): void {
    this.vikingService.deleteViking(id).subscribe(() => {
      this.dataSource.data = this.dataSource.data.filter(viking => viking.id !== id);
      this.totalItems = this.dataSource.data.length;
    });
  }

  applyFilter(): void {
    this.dataSource.filter = this.searchTerm.trim().toLowerCase();
    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  applyPagination(event: any): void {
    const pageIndex = event.pageIndex;
    const pageSize = event.pageSize;
    this.getVikings(pageIndex, pageSize);
  }
}
