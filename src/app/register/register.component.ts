import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service';
import {Router} from "@angular/router";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  providers: [ApiService]
})
export class RegisterComponent implements OnInit {
  register;
  constructor(private apiServive: ApiService, private router: Router) {}

  ngOnInit(){
    this.register = {
      name: '',
      username: '',
      password: '',
      email: ''

    };
  }
  redirectToLogin():any{
    this.router.navigate(['/login']);
  }
  registerUser(): any {
    this.apiServive.registerUser(this.register).subscribe(
      response => {
        alert('User ' + this.register.username + ' has been created!');
        this.redirectToLogin();
      },
      error => console.log('error', error)
    );

  }



}
