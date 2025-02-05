import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from './base.service';

import { PaginatedEntity } from '../interfaces/paginated.entity.interface';
import { ResponseEntity } from '../interfaces/response.entity.interface';
import { BackendViking, FrontendViking } from '../models/viking.model';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class VikingService extends BaseService<BackendViking> {
  private resource = 'vikings';

  constructor(http: HttpClient) {
    super(http);
  }

  getVikingById(id: number): Observable<ResponseEntity<BackendViking>> {
    return this.getBy(`${this.resource}/${id}`).pipe(
      map(response => response), 
    catchError(err =>  { console.log(err); return of(null)} ));
  }

  getVikings(pageIndex: number, pageSize: number): Observable<PaginatedEntity<BackendViking>> {
    return this.getAllModels(this.resource, {
      params: {
        pageIndex: pageIndex.toString(),
        pageSize: pageSize.toString()
      },
      ...httpOptions
    }).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in getVikings:', error);
        return of(null); 
      })
    );
  }

  getVikingByName(name: string): Observable<ResponseEntity<BackendViking>> {
    return this.getBy(`${this.resource}/name/${name}`, httpOptions).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in getVikingByName:', error);
        return of(null); 
      })
    );
  }

  createViking(data: FrontendViking): Observable<ResponseEntity<BackendViking>> {
    return this.postModel(this.resource, FrontendViking.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in createViking:', error);
        return of(null); 
      })
    );
  }

  updateViking(id: number, data: FrontendViking): Observable<ResponseEntity<BackendViking>> {
    return this.putModel(`${this.resource}/${id}`, FrontendViking.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in updateViking:', error);
        return of(null); 
      })
    );
  }

  deleteViking(id: number): Observable<ResponseEntity<BackendViking>> {
    return this.deleteModel(`${this.resource}/${id}`).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in deleteViking:', error);
        return of(null); 
      })
    );
  }


}
