import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from './base.service';
import { Norseman } from '../interfaces/norseman.interface';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};
@Injectable({
  providedIn: 'root'
})
export class NorsemanService extends BaseService<Norseman> {
  private resource = 'norsemans';
  constructor(http: HttpClient) {
    super(http);
  }
  getAllNorsemans(): Observable<Norseman[]> {
    return this.getAll(this.resource);
  }
  getNorsemanById(id: number): Observable<Norseman> {
    return this.get(`${this.resource}/${id}`);
  }
  getNorsemanByName(name: string): Observable<Norseman> {
    return this.get(`${this.resource}/name/${name}`);
  }
  updateNorseman(id: number, data: Partial<Norseman>): Observable<Norseman> {
    return this.put(`${this.resource}/${id}`, data);
  }
  deleteNorseman(id: number): Observable<Norseman> {
    return this.delete(`${this.resource}/${id}`);
  }
}
