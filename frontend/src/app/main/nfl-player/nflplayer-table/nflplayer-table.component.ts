import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NFLPlayer } from '../../../interfaces/nfl-player.interface';


@Component({
  standalone: false,
  selector: 'app-nflplayer-table',
  templateUrl: './nflplayer-table.component.html',
  styleUrls: ['./nflplayer-table.component.css']
})
export class NflPlayerTableComponent implements OnInit {
  nflplayers: NFLPlayer[] = [];
  @Output() selectNFLPlayer = new EventEmitter<{ nflplayer: NFLPlayer, mode: 'edit' | 'details' }>();

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get<NFLPlayer[]>('YOUR_API_ENDPOINT')
      .subscribe(
        (data) => {
          this.nflplayers = data;
        },
        (error) => {
          console.error('Error fetching data:', error);
        }
      );
  }

  select(nflplayer: NFLPlayer, mode: 'edit' | 'details'): void {
    this.selectNFLPlayer.emit({ nflplayer, mode });
  }
}
