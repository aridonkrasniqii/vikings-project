import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { VikingService } from '../../../services/viking.service';
import { Viking } from '../../../interfaces/viking.interface';

@Component({
  standalone: false,
  selector: 'app-viking-table',
  templateUrl: './viking-table.component.html',
  styleUrls: ['./viking-table.component.css']
})
export class VikingTableComponent implements OnInit {
  vikings: Viking[] = [];
  filteredVikings: Viking[] = [];
  searchTerm: string = '';
  dataSource = new MatTableDataSource<Viking>();
  
  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private vikingService: VikingService) { }

  ngOnInit(): void {
    this.getAllVikings();
  }

  getAllVikings(): void {
    this.vikingService.getAllVikings().subscribe((vikings) => {
      this.vikings = vikings;
      this.filteredVikings = vikings;
      this.dataSource.data = vikings;
      this.dataSource.paginator = this.paginator;
    });
  }

  deleteViking(id: number): void {
    this.vikingService.deleteViking(id).subscribe(() => {
      this.vikings = this.vikings.filter(viking => viking.id !== id);
      this.filteredVikings = this.filteredVikings.filter(viking => viking.id !== id);
      this.dataSource.data = this.filteredVikings;
    });
  }

  
  applyFilter(): void {
    this.filteredVikings = this.vikings.filter(viking => 
      viking.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
    this.dataSource.data = this.filteredVikings;
    // Reapply pagination after filtering
    if (this.paginator) {
      this.paginator.firstPage();
    }
  }

  // Apply pagination for server-side fetching
  applyPagination(event: any): void {
    const pageIndex = event.pageIndex;
    const pageSize = event.pageSize;

    this.vikingService.getVikings(pageIndex, pageSize).subscribe((data) => {
      this.dataSource.data = data.vikings;
      this.paginator.length = data.totalCount; // total count from the server
    });
  }
}
