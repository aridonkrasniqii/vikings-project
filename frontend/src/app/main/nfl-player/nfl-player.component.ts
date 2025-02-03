import { Component } from '@angular/core';
import { NFLPlayer } from '../../interfaces/nfl-player.interface';


@Component({
  standalone: false,
  selector: 'app-nflplayer',
  templateUrl: './nfl-player.component.html',
  styleUrls: ['./nfl-player.component.css']
})
export class NflPlayerComponent {
  ngOnInit(): void { 
  }
}
