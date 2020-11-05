import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
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

  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
