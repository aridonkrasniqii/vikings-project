import { Component, Input, Output, EventEmitter } from '@angular/core';
import { NFLPlayer } from '../../../interfaces/nfl-player.interface';


@Component({
  standalone: false,
  selector: 'app-nflplayer-details',
  templateUrl: './nflplayer-details.component.html',
  styleUrls: ['./nflplayer-details.component.css']
})
export class NflPlayerDetailsComponent {
  @Input() nflplayer: NFLPlayer | null = null;
  @Output() back = new EventEmitter<void>();
}
