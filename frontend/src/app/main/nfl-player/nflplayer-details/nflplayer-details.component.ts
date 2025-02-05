import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { NFLPlayerService } from '../../../services/nfl-player.service';
import { FrontendNFLPlayer } from '../../../models/nfl-players.model';


@Component({
  standalone: false,
  selector: 'app-nflplayer-details',
  templateUrl: './nflplayer-details.component.html',
  styleUrls: ['./nflplayer-details.component.css']
})
export class NFLPlayerDetailsComponent implements OnInit {
  nflPlayer: FrontendNFLPlayer;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private playerService: NFLPlayerService
  ) {}

  ngOnInit(): void {
    this.getPlayerDetails();
  }

  getPlayerDetails(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.playerService.getNFLPlayerById(id).subscribe((response) => {
      if (response && response.data) {
        this.nflPlayer = FrontendNFLPlayer.fromBackend(response.data[0]);
      }
    });
  }

  goBack(): void {
    this.router.navigate(['/nflplayers']);
  }
}
