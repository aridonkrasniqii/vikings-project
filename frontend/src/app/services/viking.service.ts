import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from './base.service';

import { PaginatedEntity } from '../interfaces/paginated.entity.interface';
import { ResponseEntity } from '../interfaces/response.entity.interface';
import { BackendViking, FrontendViking } from '../models/viking.model';
import { PaginationParams } from '../interfaces/pagination-params.inteface';

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
      catchError(err => { console.log(err); return of(null) }));
  }

  getVikings(
    params: PaginationParams): Observable<PaginatedEntity<BackendViking>> {

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
        console.error('Error white trying to get vikings: ', error);
        return of(null);
      })
    );
  }


  getVikingByName(name: string): Observable<ResponseEntity<BackendViking>> {
    return this.getBy(`${this.resource}/name/${name}`, httpOptions).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error while trying to get viking by name', error);
        return of(null);
      })
    );
  }

  createViking(data: FrontendViking): Observable<ResponseEntity<BackendViking>> {
    return this.postModel(this.resource, FrontendViking.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error in while trying to create viking: ', error);
        return of(null);
      })
    );
  }

  updateViking(id: number, data: FrontendViking): Observable<ResponseEntity<BackendViking>> {
    return this.putModel(`${this.resource}/${id}`, FrontendViking.toBackend(data)).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error while trying to update viking: ', error);
        return of(null);
      })
    );
  }

  deleteViking(id: number): Observable<ResponseEntity<BackendViking>> {
    return this.deleteModel(`${this.resource}/${id}`).pipe(
      map(response => response),
      catchError(error => {
        console.error('Error while trying to delete viking:', error);
        return of(null);
      })
    );
  }


}
