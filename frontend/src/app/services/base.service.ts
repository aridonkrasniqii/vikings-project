import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { environment } from '../env/env-dev';
import { PaginatedEntity } from '../interfaces/paginated.entity.interface';
import { ResponseEntity } from '../interfaces/response.entity.interface';

export abstract class BaseService<T> {
  protected apiUrl = environment.apiUrl;

  protected httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(protected http: HttpClient) {}

  protected handleError(response: HttpErrorResponse): Observable<never> {
    console.error('An error occurred:', response);  // Add logging
    const errorResponse = {
      statusCode: response.status,
      apiUrl: response.url,
      message: response.error.message,
      error: response
    };

    return throwError(() => errorResponse);
  }

  protected extractData(res: any) {
    const body = res;
    return body || {};
  }

  protected getAllModels(endpoint: string, query?: any): Observable<PaginatedEntity<T>> {
    const options = {
      ...this.httpOptions,
      params: query
    };
    console.log(`${this.apiUrl}/${endpoint}`);
    console.log(options);
    return this.http.get<T[]>(`${this.apiUrl}/${endpoint}`, options).pipe(map(this.extractData), catchError(this.handleError));
  }

  protected getBy(endpoint: string, params?: any): Observable<ResponseEntity<T>> {
    const options = {
      ...this.httpOptions,
      params: params
    };
    return this.http.get<T>(`${this.apiUrl}/${endpoint}`, options).pipe(map(this.extractData), catchError(this.handleError));
  }

  protected postModel(endpoint: string, data: any): Observable<ResponseEntity<T>> {
    return this.http.post<T>(`${this.apiUrl}/${endpoint}`, data, this.httpOptions).pipe(map(this.extractData), catchError(this.handleError));
  }

  protected patchModel(endpoint: string, data: any): Observable<ResponseEntity<T>> {
    return this.http.patch<T>(`${this.apiUrl}/${endpoint}`, data, this.httpOptions).pipe(map(this.extractData), catchError(this.handleError));
  }

  protected putModel(endpoint: string, data: any): Observable<ResponseEntity<T>> {
    return this.http.put<T>(`${this.apiUrl}/${endpoint}`, data, this.httpOptions).pipe(map(this.extractData), catchError(this.handleError));
  }

  protected deleteModel(endpoint: string): Observable<ResponseEntity<T>> {
    return this.http.delete<T>(`${this.apiUrl}/${endpoint}`, this.httpOptions).pipe(map(this.extractData), catchError(this.handleError));
  }
}
