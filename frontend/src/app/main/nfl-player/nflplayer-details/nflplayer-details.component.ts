import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { NFLPlayerService } from '../../../services/nfl-player.service';
import { NFLPlayer, NFLPlayerStats } from '../../../interfaces/nfl-player.interface';


@Component({
  standalone: false,
  selector: 'app-nflplayer-details',
  templateUrl: './nflplayer-details.component.html',
  styleUrls: ['./nflplayer-details.component.css']
})
export class NFLPlayerDetailsComponent implements OnInit {
  nflPlayer: NFLPlayer;

  constructor(
    private route: ActivatedRoute,
    private nflPlayerService: NFLPlayerService,
    private location: Location
  ) { }

  ngOnInit(): void {
    this.getNFLPlayer();
  }

  getNFLPlayer(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.nflPlayerService.getNFLPlayerById(id)
      .subscribe(response => {
        if (response) {
          this.nflPlayer = this.mapNFLPlayer(response.data);
        } else {
          console.warn('No player data received');
        }
      });
  }

  mapNFLPlayer(item: any): NFLPlayer {
    return {
      id: item.id,
      number: item.number,
      position: item.position,
      age: item.age,
      experience: item.experience,
      college: item.college,
      name: item.name,
      photo: item.photo,
      stats: item.stats.map((stat: any) => this.mapNFLPlayerStats(stat)),
      createdAt: item.created_at,
      updatedAt: item.updated_at
    };
  }

  mapNFLPlayerStats(item: any): NFLPlayerStats {
    return {
      id: item.id,
      playerId: item.player_id,
      season: item.season,
      team: item.team,
      gamesPlayed: item.games_played,
      receptions: item.receptions,
      receivingYards: item.receiving_yards,
      receivingTouchdowns: item.receiving_touchdowns,
      longestReception: item.longest_reception
    };
  }

  goBack(): void {
    this.location.back();
  }
}
