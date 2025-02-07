import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from './base.service';
import { PaginatedEntity } from '../interfaces/paginated.entity.interface';
import { ResponseEntity } from '../interfaces/response.entity.interface';
import { BackendNorseman, FrontendNorseman } from '../models/norseman.model';

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

  getNorsemans(pageIndex: number, pageSize: number): Observable<PaginatedEntity<BackendNorseman>> {
    return this.getAllModels(this.resource, {
      params: {
        pageIndex: pageIndex.toString(),
        pageSize: pageSize.toString()
      },
      ...httpOptions
    }).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in getNorsemans:', error);
        return of(null); 
      })
    );
  }

  getNorsemanByName(name: string): Observable<ResponseEntity<BackendNorseman>> {
    return this.getBy(`${this.resource}/name/${name}`, httpOptions).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in getNorsemanByName:', error);
        return of(null); 
      })
    );
  }

  createNorseman(data: FrontendNorseman): Observable<ResponseEntity<BackendNorseman>> {
    return this.postModel(this.resource, FrontendNorseman.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in createNorseman:', error);
        return of(null); 
      })
    );
  }

  updateNorseman(id: number, data: FrontendNorseman): Observable<ResponseEntity<BackendNorseman>> {
    return this.putModel(`${this.resource}/${id}`, FrontendNorseman.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in updateNorseman:', error);
        return of(null); 
      })
    );
  }

  deleteNorseman(id: number): Observable<ResponseEntity<BackendNorseman>> {
    return this.deleteModel(`${this.resource}/${id}`).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in deleteNorseman:', error);
        return of(null); 
      })
    );
  }
}
