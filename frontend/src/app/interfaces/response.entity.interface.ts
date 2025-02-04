export interface ResponseEntity<T> {
    data: T;
    message: string;
    status_code: number;
}