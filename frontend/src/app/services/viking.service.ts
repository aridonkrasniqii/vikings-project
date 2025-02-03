import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from './base.service';
import { Viking } from '../interfaces/viking.interface';

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
    return this.getAll(this.resource);
  }
  getVikingById(id: number): Observable<Viking> {
    return this.get(`${this.resource}/${id}`);
  }

  getVikings(pageIndex: number, pageSize: number) {
    return this.http.get<{ vikings: Viking[], totalCount: number }>(this.resource, {
      params: {
        pageIndex: pageIndex.toString(),
        pageSize: pageSize.toString()
      }
    });
  }

  getVikingByName(name: string): Observable<Viking> {
    return this.get(`${this.resource}/name/${name}`);
  }

  createViking(data: Viking): Observable<Viking> {
    return this.post(this.resource, data);
  }
  
  updateViking(id: number, data: Partial<Viking>): Observable<Viking> {
    return this.put(`${this.resource}/${id}`, data);
  }
  deleteViking(id: number): Observable<Viking> {
    return this.delete(`${this.resource}/${id}`);
  }
}
