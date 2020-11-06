import { Injectable } from '@angular/core';
import { HttpClient } from  '@angular/common/http';
import {Observable} from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private  http:HttpClient) { }

  registerUser(userData): Observable<any> {
    return this.http.post('https://dj-services-api.herokuapp.com/api/accounts/register', userData);
  }
  loginUser(userData): Observable<any> {
    return this.http.post('https://dj-services-api.herokuapp.com/api/accounts/login', userData);
  }
  getServices():Observable<any>{
    return  this.http.get('https://dj-services-api.herokuapp.com/api/service');
  }

}

