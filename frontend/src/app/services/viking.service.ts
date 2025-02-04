import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { BaseService } from './base.service';
import { Viking } from '../interfaces/viking.interface';
import { of } from 'rxjs';
import { PaginatedEntity } from '../interfaces/paginated.entity.interface';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class VikingService extends BaseService<Viking> {
  private resource = 'vikings';

  constructor(http: HttpClient) {
    super(http);
  }

  getAllVikings(): Observable<Viking[]> {
    return this.getAllModels(this.resource, httpOptions).pipe(
      map(response => response.data.map(item => this.transformViking(item)))
    );
  }

  getVikingById(id: number): Observable<Viking> {
    return this.getBy(`${this.resource}/${id}`, httpOptions).pipe(
      map(response => this.transformViking(response))
    );
  }

  getVikings(pageIndex: number, pageSize: number): Observable<PaginatedEntity<Viking>> {
    return this.getAllModels(this.resource, {
      params: {
        pageIndex: pageIndex.toString(),
        pageSize: pageSize.toString()
      },
      ...httpOptions
    }).pipe(
      map(response => {
        const transformedResponse: PaginatedEntity<Viking> = {
          total_items: response.total_items,
          total_pages: response.total_pages,
          current_page: response.current_page,
          limit: response.limit,
          data: response.data.map(item => this.transformViking(item))
        };
        return transformedResponse;
      }),
      catchError(error => {
        console.error('Error in getVikings:', error);
        return of(null); 
      })
    );
  }

  getVikingByName(name: string): Observable<Viking> {
    return this.getBy(`${this.resource}/name/${name}`, httpOptions).pipe(
      map(response => this.transformViking(response))
    );
  }

  createViking(data: Viking): Observable<Viking> {
    return this.postModel(this.resource, data).pipe(
      map(response => this.transformViking(response))
    );
  }

  updateViking(id: number, data: Partial<Viking>): Observable<Viking> {
    return this.putModel(`${this.resource}/${id}`, data).pipe(
      map(response => this.transformViking(response))
    );
  }

  deleteViking(id: number): Observable<Viking> {
    return this.deleteModel(`${this.resource}/${id}`).pipe(
      map(response => this.transformViking(response))
    );
  }

  private transformViking(item: any): Viking {
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
