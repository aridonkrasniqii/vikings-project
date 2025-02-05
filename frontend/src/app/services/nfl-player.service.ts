import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from './base.service';

import { of } from 'rxjs';
import { PaginatedEntity } from '../interfaces/paginated.entity.interface';
import { ResponseEntity } from '../interfaces/response.entity.interface';
import { BackendNFLPlayer, FrontendNFLPlayer } from '../models/nfl-players.model';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class NFLPlayerService extends BaseService<BackendNFLPlayer> {
  private resource = 'nflplayers';

  constructor(http: HttpClient) {
    super(http);
  }

  getNFLPlayers(pageIndex: number, pageSize: number): Observable<PaginatedEntity<BackendNFLPlayer>> {
    return this.getAllModels(this.resource, {
      params: {
        pageIndex: pageIndex.toString(),
        pageSize: pageSize.toString()
      },
      ...httpOptions
    }).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in getNFLPlayers:', error);
        return of(null); 
      })
    );
  }

  getNFLPlayerById(id: number): Observable<ResponseEntity<BackendNFLPlayer>> {
    return this.getBy(`${this.resource}/${id}`).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in getNFLPlayerById:', error);
        return of(null); 
      })
    );
  }

  createNFLPlayer(data: FrontendNFLPlayer): Observable<ResponseEntity<BackendNFLPlayer>> {
    return this.postModel(this.resource, FrontendNFLPlayer.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in createNFLPlayer:', error);
        return of(null); 
      })
    );
  }

  updateNFLPlayer(id: number, data: FrontendNFLPlayer): Observable<ResponseEntity<BackendNFLPlayer>> {
    return this.putModel(`${this.resource}/${id}/`, FrontendNFLPlayer.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in updateNFLPlayer:', error);
        return of(null); 
      })
    );
  }

  deleteNFLPlayer(id: number): Observable<ResponseEntity<BackendNFLPlayer>> {
    return this.deleteModel(`${this.resource}/${id}`).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in deleteNFLPlayer:', error);
        return of(null); 
      })
    );
  }
}
