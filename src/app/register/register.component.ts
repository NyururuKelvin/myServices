import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/api.service'

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  providers: [ApiService]
})
export class RegisterComponent implements OnInit {
  register;
  constructor(private apiServive: ApiService) { 

  }

  ngOnInit(){
    this.register = {
      name: '',
      username: '',
      password: '',
      email: ''

    };
  }
  registerUser() {
    this.apiServive.registerUser(this.register).subscribe(
      response => {
        alert('User ' + this.register.username + ' has been created!')
      },
      error => console.log('error', error)
    );
  }
}
