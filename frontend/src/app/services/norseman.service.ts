import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from './base.service';
import { Norseman } from '../interfaces/norseman.interface';
import { PaginatedEntity } from '../interfaces/paginated.entity.interface';
import { of } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class NorsemanService extends BaseService<Norseman> {
  private resource = 'norsemen'; 

  constructor(http: HttpClient) {
    super(http);
  }

  getAllNorsemans(): Observable<Norseman[]> {
    return this.getAllModels(this.resource, httpOptions).pipe(
      map(response => response.data.map(item => this.transformNorseman(item)))
    );
  }

  getNorsemanById(id: number): Observable<Norseman> {
    return this.getBy(`${this.resource}/${id}`, httpOptions).pipe(
      map(response => this.transformNorseman(response))
    );
  }

  getNorsemans(pageIndex: number, pageSize: number): Observable<PaginatedEntity<Norseman>> {
    return this.getAllModels(this.resource, {
      params: {
        pageIndex: pageIndex.toString(),
        pageSize: pageSize.toString()
      },
      ...httpOptions
    }).pipe(
      map(response => {
        const transformedResponse: PaginatedEntity<Norseman> = {
          total_items: response.total_items,
          total_pages: response.total_pages,
          current_page: response.current_page,
          limit: response.limit,
          data: response.data.map(item => this.transformNorseman(item))
        };
        return transformedResponse;
      }),
      catchError(error => {
        console.error('Error in getNorsemans:', error);
        return of(null); 
      })
    );
  }

  getNorsemanByName(name: string): Observable<Norseman> {
    return this.getBy(`${this.resource}/name/${name}`, httpOptions).pipe(
      map(response => this.transformNorseman(response))
    );
  }

  createNorseman(data: Norseman): Observable<Norseman> {
    return this.postModel(this.resource, data).pipe(
      map(response => this.transformNorseman(response))
    );
  }

  updateNorseman(id: number, data: Partial<Norseman>): Observable<Norseman> {
    return this.putModel(`${this.resource}/${id}`, data).pipe(
      map(response => this.transformNorseman(response))
    );
  }

  deleteNorseman(id: number): Observable<Norseman> {
    return this.deleteModel(`${this.resource}/${id}`).pipe(
      map(response => this.transformNorseman(response))
    );
  }

  private transformNorseman(item: any): Norseman {
    return {
      id: item.id,
      name: item.name,
      photo: item.photo,
      actorName: item.actor_name,
      description: item.description,
      createdAt: item.created_at,
      updatedAt: item.updated_at
    };
  }
}
