import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from './base.service';

import { of } from 'rxjs';
import { PaginatedEntity } from '../interfaces/paginated.entity.interface';
import { NFLPlayer, NFLPlayerStats } from '../interfaces/nfl-player.interface';
import { ResponseEntity } from '../interfaces/response.entity.interface';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class NFLPlayerService extends BaseService<NFLPlayer> {
  private resource = 'nflplayers';

  constructor(http: HttpClient) {
    super(http);
  }

  getNFLPlayers(pageIndex: number, pageSize: number): Observable<PaginatedEntity<NFLPlayer>> {
    return this.getAllModels(this.resource, {
      params: {
        pageIndex: pageIndex.toString(),
        pageSize: pageSize.toString()
      },
      ...httpOptions
    }).pipe(
      map(response => {
        const transformedResponse: PaginatedEntity<NFLPlayer> = {
          total_items: response.total_items,
          total_pages: response.total_pages,
          current_page: response.current_page,
          limit: response.limit,
          data: response.data.map((item: any) => this.transformNFLPlayer(item))
        };
        return transformedResponse;
      }),
      catchError(error => {
        console.error('Error in getNFLPlayers:', error);
        return of(null); 
      })
    );
  }

  getNFLPlayerById(id: number): Observable<ResponseEntity<NFLPlayer>> {
    return this.getBy(`${this.resource}/${id}`).pipe(
      map(response => {
        return {
          data: this.transformNFLPlayer(response.data[0]),
          message: response.message,
          status_code: response.status_code
        };
      }),
      catchError(error => {
        console.error('Error in getNFLPlayerById:', error);
        return of(null); 
      })
    );
  }

  createNFLPlayer(data: NFLPlayer): Observable<ResponseEntity<NFLPlayer>> {
    return this.postModel(this.resource, data).pipe(
      map(response => {
        return {
          data: this.transformNFLPlayer(response.data),
          message: response.message,
          status_code: response.status_code
        };
      }),
      catchError(error => {
        console.error('Error in createNFLPlayer:', error);
        return of(null); 
      })
    );
  }

  updateNFLPlayer(id: number, data: Partial<NFLPlayer>): Observable<ResponseEntity<NFLPlayer>> {
    return this.putModel(`${this.resource}/${id}/`, data).pipe(
      map(response => {
        return {
          data: this.transformNFLPlayer(response.data),
          message: response.message,
          status_code: response.status_code
        };
      }),
      catchError(error => {
        console.error('Error in updateNFLPlayer:', error);
        return of(null); 
      })
    );
  }

  deleteNFLPlayer(id: number): Observable<ResponseEntity<NFLPlayer>> {
    return this.deleteModel(`${this.resource}/${id}`).pipe(
      map(response => {
        return {
          data: this.transformNFLPlayer(response.data),
          message: response.message,
          status_code: response.status_code
        };
      }),
      catchError(error => {
        console.error('Error in deleteNFLPlayer:', error);
        return of(null); 
      })
    );
  }

  private transformNFLPlayer(item: any): NFLPlayer {
    return {
      id: item.id,
      number: item.number,
      position: item.position,
      age: item.age,
      experience: item.experience,
      college: item.college,
      name: item.name,
      photo: item.photo,
      stats: item.stats.map((stat: any) => this.transformNFLPlayerStats(stat)),
      createdAt: item.created_at,
      updatedAt: item.updated_at
    };
  }

  private transformNFLPlayerStats(item: any): NFLPlayerStats {
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
}
