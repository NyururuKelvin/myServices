import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service'
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [ApiService]
})
export class LoginComponent implements OnInit {
  loggin;
  constructor(private apiServive: ApiService, private router: Router) { }

  ngOnInit(){
    this.loggin = {
      username: '',
      password: '',

    };
  }
  loginUser() {
    this.apiServive.loginUser(this.loggin).subscribe(
      response => {
        alert('User ' + this.loggin.username + 'loged in Succesfully!');
      },
      error => console.log('error', error)
    );
  }
}
