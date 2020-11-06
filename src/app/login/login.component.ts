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
  redirectToHomepage(){
    this.router.navigate(['']);
  }
  loginUser() {
    this.apiServive.loginUser(this.loggin).subscribe(
      response => {
        console.log(response);
        this.redirectToHomepage();
      },
      error => console.log('error', error)
    );
  }
}
