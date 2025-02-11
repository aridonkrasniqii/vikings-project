import { Component, OnInit } from '@angular/core';
import { NFLPlayerService } from '../../../services/nfl-player.service';
import { PaginatedEntity } from '../../../interfaces/paginated.entity.interface';
import { BackendNFLPlayer, FrontendNFLPlayer } from '../../../models/nfl-players.model';
import { PaginationParams } from '../../../interfaces/pagination-params.inteface';
import { BackendViking, FrontendViking } from '../../../models/viking.model';

@Component({
  standalone: false,
  selector: 'app-nflplayer-table',
  templateUrl: './nflplayer-table.component.html',
  styleUrls: ['./nflplayer-table.component.css']
})
export class NFLPlayerTableComponent implements OnInit {
  displayedColumns: string[] = ['photo', 'name', 'number', 'position', 'age', 'experience', 'college', 'actions'];
  dataSource: FrontendNFLPlayer[] = [];
  searchTerm: string = '';
  totalItems = 0;
  itemsPerPage = 10;
  currentPage = 1; 
  sortField: string = '';
  sortDirection: string = '';

  constructor(private nflPlayerService: NFLPlayerService) {}

  ngOnInit(): void {
    this.getNFLPlayers();
  }

  getNFLPlayers(): void {
      const params = this.getParams();
      this.nflPlayerService.getNFLPlayers(params)
        .subscribe((response: PaginatedEntity<BackendNFLPlayer>) => {
          if (response) {
            this.dataSource = response.data.map(backendNFLPlayer => FrontendNFLPlayer.fromBackend(backendNFLPlayer));
            this.totalItems = response.total_items;
            console.log(`Total Items: ${this.totalItems}`);
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

  deleteNFLPlayer(id: number): void {
    this.nflPlayerService.deleteNFLPlayer(id).subscribe(() => {
      this.dataSource = this.dataSource.filter(player => player.id !== id);
      this.totalItems = this.dataSource.length;
      this.getNFLPlayers();
    });
  }

  applyFilter(): void {
    this.currentPage = 1;
    this.getNFLPlayers();
  }

  handlePageChange(page: number): void {
    this.currentPage = page;
    this.getNFLPlayers();
  }
}
