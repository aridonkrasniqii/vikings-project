import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { NFLPlayer } from '../interfaces/nfl-player.interface';
import { BaseService } from './base.service';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};
@Injectable({
  providedIn: 'root'
})
export class NflPlayerService extends BaseService<NFLPlayer> {
  private resource = 'nfl-players';

  constructor(http: HttpClient) {
    super(http);
  }
  getAllNflPlayers(): Observable<NFLPlayer[]> {
    return this.getAll(this.resource);
  }
  getNflPlayerById(id: number): Observable<NFLPlayer> {
    return this.get(`${this.resource}/${id}`);
  }
  getNflPlayerByName(name: string): Observable<NFLPlayer> {
    return this.get(`${this.resource}/name/${name}`);
  }
  updateNflPlayer(id: number, data: Partial<NFLPlayer>): Observable<NFLPlayer> {
    return this.put(`${this.resource}/${id}`, data);
  }
  deleteNflPlayer(id: number): Observable<NFLPlayer> {
    return this.delete(`${this.resource}/${id}`);
  }
}
