import { Component, OnInit } from '@angular/core';
import {ApiService} from "../api.service";

@Component({
  selector: 'app-servicedetails',
  templateUrl: './servicedetails.component.html',
  styleUrls: ['./servicedetails.component.css']
})
export class ServicedetailsComponent implements OnInit {
  serviceItem;
  serviceType={
    id: '',
    name:''
  }
  serviceList=[]

  constructor(private apiService: ApiService) {
    this.serviceItem = {
      description: '',
      id: '',
      name: '',
      serviceType: this.serviceItem
    };
  }

  getApiServices(): any{
    this.apiService.getServices().subscribe(
      response => {
        this.serviceList = response.services;
        console.log(this.serviceList);
      },
      error => {
        console.log(error);
      }
    );
  }
  ngOnInit(): void {
  this.getApiServices();
  }

}
