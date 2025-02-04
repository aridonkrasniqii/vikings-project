import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { NFLPlayerService } from '../../../services/nfl-player.service';
import { NFLPlayer } from '../../../interfaces/nfl-player.interface';
import { PaginatedEntity } from '../../../interfaces/paginated.entity.interface';


@Component({
  standalone: false,
  selector: 'app-nflplayer-table',
  templateUrl: './nflplayer-table.component.html',
  styleUrls: ['./nflplayer-table.component.css']
})
export class NFLPlayerTableComponent implements OnInit, AfterViewInit {
  displayedColumns: string[] = ['photo', 'name', 'number', 'position', 'age', 'experience', 'college', 'actions'];
  dataSource = new MatTableDataSource<NFLPlayer>();
  searchTerm: string = '';
  totalItems = 0;
  itemsPerPage = 10;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private nflPlayerService: NFLPlayerService) { }

  ngOnInit(): void {
    this.dataSource.filterPredicate = (data: NFLPlayer, filter: string) => {
      const transformedFilter = filter.trim().toLowerCase();
      const name = data.name.trim().toLowerCase();
      const position = data.position.trim().toLowerCase();
      const college = data.college.trim().toLowerCase();

      return name.includes(transformedFilter) || 
             position.includes(transformedFilter) || 
             college.includes(transformedFilter);
    };

    this.getNFLPlayers(0, this.itemsPerPage);
  }

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  getNFLPlayers(pageIndex: number, pageSize: number): void {
    this.nflPlayerService.getNFLPlayers(pageIndex, pageSize).subscribe((response: PaginatedEntity<NFLPlayer>) => {
      if (response) {
        console.log('Received NFL players:', response.data);
        this.dataSource.data = response.data;
        this.totalItems = response.total_items;
      } else {
        console.warn('No response received');
      }
    });
  }

  deleteNFLPlayer(id: number): void {
    this.nflPlayerService.deleteNFLPlayer(id).subscribe(() => {
      this.dataSource.data = this.dataSource.data.filter(player => player.id !== id);
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
    this.getNFLPlayers(pageIndex, pageSize);
  }
}
