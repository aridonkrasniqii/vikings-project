import { Component, Input, Output, EventEmitter } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NFLPlayer } from '../../../interfaces/nfl-player.interface';


@Component({
  standalone: false,
  selector: 'app-nflplayer-edit',
  templateUrl: './nflplayer-edit.component.html',
  styleUrls: ['./nflplayer-edit.component.css']
})
export class NflPlayerEditComponent {
  @Input() nflplayer: NFLPlayer | null = null;
  @Output() saved = new EventEmitter<void>();
  @Output() cancelled = new EventEmitter<void>();

  constructor(private http: HttpClient) {}

  saveNflPlayer(): void {
    if (this.nflplayer) {
      this.http.put(`YOUR_API_ENDPOINT/${this.nflplayer.id}`, this.nflplayer)
        .subscribe(
          () => {
            this.saved.emit();
          },
          (error) => {
            console.error('Error saving data:', error);
          }
        );
    }
  }

  cancel(): void {
    this.cancelled.emit();
  }
}
