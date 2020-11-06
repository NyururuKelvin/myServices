import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {RegisterComponent} from "./register/register.component";
import {LoginComponent} from "./login/login.component";
import {AppComponent} from "./app.component";
import {HomepageComponent} from "./homepage/homepage.component";
import {BusinessComponent} from "./business/business.component";
import {ServicedetailsComponent} from "./servicedetails/servicedetails.component";
import {BslistComponent} from "./bslist/bslist.component";

const routes: Routes = [

  {path:"register", component:RegisterComponent},
  {path:"login", component: LoginComponent},
  {path:"", component: HomepageComponent},
  {path:"business", component:BusinessComponent},
  {path:"service",component:ServicedetailsComponent},
  {path:"business/list", component:BslistComponent}

];
@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
