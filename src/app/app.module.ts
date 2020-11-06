import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { ServicedetailsComponent } from './servicedetails/servicedetails.component';
import { BusinessComponent } from './business/business.component';
import { BslistComponent } from './bslist/bslist.component';
import { RegisterComponent } from './register/register.component';
import { HomepageComponent } from './homepage/homepage.component'
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from './api.service';
import { FormsModule } from '@angular/forms';
import { NgProgressModule } from '@ngx-progressbar/core';
import { NgProgressHttpClientModule } from '@ngx-progressbar/http-client';
import {AppRoutingModule} from "./app-routing.module";

@NgModule({
  declarations: [
    AppComponent,
    BusinessComponent,
    BslistComponent,
    RegisterComponent,
    LoginComponent,
    HomepageComponent,
    ServicedetailsComponent,
  ],

  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    FormsModule,
    NgProgressModule.forRoot(),
    NgProgressHttpClientModule,
    AppRoutingModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
