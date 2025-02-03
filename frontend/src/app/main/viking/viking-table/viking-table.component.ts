import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { VikingService } from '../../../services/viking.service';
import { Viking } from '../../../interfaces/viking.interface';

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
    this.getAllVikings();
  }

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  getAllVikings(): void {
    this.vikingService.getAllVikings().subscribe((vikings) => {
      this.dataSource.data = vikings;
      this.totalItems = vikings.length;
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
    this.dataSource.paginator.pageIndex = pageIndex;
    this.dataSource.paginator.pageSize = pageSize;
  }
}
