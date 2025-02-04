import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { NorsemanService } from '../../../services/norseman.service';
import { Norseman } from '../../../interfaces/norseman.interface';
import { PaginatedEntity } from '../../../interfaces/paginated.entity.interface';

@Component({
  standalone: false,
  selector: 'app-norseman-table',
  templateUrl: './norseman-table.component.html',
  styleUrls: ['./norseman-table.component.css']
})
export class NorsemanTableComponent implements OnInit, AfterViewInit {
  displayedColumns: string[] = ['picture', 'actorName', 'characterName', 'description', 'actions'];
  dataSource = new MatTableDataSource<Norseman>();
  searchTerm: string = '';
  totalItems = 0;
  itemsPerPage = 10;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private norsemanService: NorsemanService) { }

  ngOnInit(): void {
    this.dataSource.filterPredicate = (data: Norseman, filter: string) => {
      const transformedFilter = filter.trim().toLowerCase();
      const actorName = data.actorName.trim().toLowerCase();
      const characterName = data.name.trim().toLowerCase();
      const description = data.description.trim().toLowerCase();

      return actorName.includes(transformedFilter) || 
             characterName.includes(transformedFilter) || 
             description.includes(transformedFilter);
    };

    this.getNorsemans(0, this.itemsPerPage);
  }

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  getNorsemans(pageIndex: number, pageSize: number): void {
    this.norsemanService.getNorsemans(pageIndex, pageSize).subscribe((response: PaginatedEntity<Norseman>) => {
      if (response) {
        console.log('Received norsemans:', response.data);
        this.dataSource.data = response.data;
        this.totalItems = response.total_items;
      } else {
        console.warn('No response received');
      }
    });
  }

  deleteNorseman(id: number): void {
    this.norsemanService.deleteNorseman(id).subscribe(() => {
      this.dataSource.data = this.dataSource.data.filter(norseman => norseman.id !== id);
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
    this.getNorsemans(pageIndex, pageSize);
  }
}
