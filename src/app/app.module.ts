import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { ServicedetailsComponent } from './servicedetails/servicedetails.component';
import { BusinessComponent } from './business/business.component';
import { BslistComponent } from './bslist/bslist.component';
import { RegisterComponent } from './register/register.component'


@NgModule({
  declarations: [
    AppComponent,
    BusinessComponent,
    ft_business.list,
    BslistComponent,
    RegisterComponent,
    LoginComponent,
    ft-servicedetails
    ServicedetailsComponent,
  ],
  
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
