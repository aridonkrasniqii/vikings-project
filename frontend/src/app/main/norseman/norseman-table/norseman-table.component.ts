import { Component, OnInit } from '@angular/core';
import { NorsemanService } from '../../../services/norseman.service';
import { Norseman } from '../../../interfaces/norseman.interface';

@Component({
  standalone: false,
  selector: 'app-norseman-table',
  templateUrl: './norseman-table.component.html',
  styleUrls: ['./norseman-table.component.scss']
})
export class NorsemanTableComponent implements OnInit {
  norsemans: Norseman[] = [];
  filteredNorsemans: Norseman[] = [];
  searchTerm: string = '';

  constructor(private norsemanService: NorsemanService) { }

  ngOnInit(): void {
    this.getAllNorsemans();
  }

  getAllNorsemans(): void {
    this.norsemanService.getAllNorsemans().subscribe((norsemans) => {
      this.norsemans = norsemans;
      this.filteredNorsemans = norsemans;
    });
  }

  deleteNorseman(id: number): void {
    this.norsemanService.deleteNorseman(id).subscribe(() => {
      this.norsemans = this.norsemans.filter(norseman => norseman.id !== id);
      this.filteredNorsemans = this.filteredNorsemans.filter(norseman => norseman.id !== id);
    });
  }

  applyFilter(): void {
    this.filteredNorsemans = this.norsemans.filter(norseman => 
      norseman.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }
}
