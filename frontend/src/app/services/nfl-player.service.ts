import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from './base.service';

import { of } from 'rxjs';
import { PaginatedEntity } from '../interfaces/paginated.entity.interface';
import { ResponseEntity } from '../interfaces/response.entity.interface';
import { BackendNFLPlayer, FrontendNFLPlayer } from '../models/nfl-players.model';
import { PaginationParams } from '../interfaces/pagination-params.inteface';

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

  getNFLPlayers(params: PaginationParams): Observable<PaginatedEntity<BackendNFLPlayer>> {
     let httpParams = new HttpParams()
          .set('page', params.page.toString())
          .set('limit', params.limit.toString());
    
        if (params.q) {
          httpParams = httpParams.set('q', params.q);
          httpParams = httpParams.set('search_fields', 'name,college');
        }
        if (params.asc) {
          httpParams = httpParams.set('asc', params.asc);
        }
        if (params.desc) {
          httpParams = httpParams.set('desc', params.desc);
        }
    
        return this.getAllModels(this.resource, httpParams).pipe(
          map(response => response),
          catchError(error => {
            console.error('Error in getVikings:', error);
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
