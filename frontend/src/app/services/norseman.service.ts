import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from './base.service';
import { PaginatedEntity } from '../interfaces/paginated.entity.interface';
import { ResponseEntity } from '../interfaces/response.entity.interface';
import { BackendNorseman, FrontendNorseman } from '../models/norseman.model';
import { PaginationParams } from '../interfaces/pagination-params.inteface';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class NorsemanService extends BaseService<BackendNorseman> {
  private resource = 'norsemen';

  constructor(http: HttpClient) {
    super(http);
  }

  getNorsemanById(id: number): Observable<ResponseEntity<BackendNorseman>> {
    return this.getBy(`${this.resource}/${id}`, httpOptions).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in getNorsemanById:', error);
        return of(null);
      })
    );
  }

  getNorsemans(params: PaginationParams): Observable<PaginatedEntity<BackendNorseman>> {
     let httpParams = new HttpParams()
          .set('page', params.page.toString())
          .set('limit', params.limit.toString());
    
      if (params.q) {
        httpParams = httpParams.set('q', params.q);
        httpParams = httpParams.set('search_fields', 'name,actor_name');
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
          console.error('Error while trying to get norsmans: ', error);
          return of(null);
        })
      );
  }

  getNorsemanByName(name: string): Observable<ResponseEntity<BackendNorseman>> {
    return this.getBy(`${this.resource}/name/${name}`, httpOptions).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error while trying to get norseman by name: ', error);
        return of(null); 
      })
    );
  }

  createNorseman(data: FrontendNorseman): Observable<ResponseEntity<BackendNorseman>> {
    return this.postModel(this.resource, FrontendNorseman.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error while trying to get norseman: ', error);
        return of(null); 
      })
    );
  }

  updateNorseman(id: number, data: FrontendNorseman): Observable<ResponseEntity<BackendNorseman>> {
    return this.putModel(`${this.resource}/${id}`, FrontendNorseman.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error while trying to get update norsman: ', error);
        return of(null); 
      })
    );
  }

  deleteNorseman(id: number): Observable<ResponseEntity<BackendNorseman>> {
    return this.deleteModel(`${this.resource}/${id}`).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error while trying to delete norseman: ', error);
        return of(null); 
      })
    );
  }
}
