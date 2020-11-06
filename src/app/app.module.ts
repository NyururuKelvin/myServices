import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { ServicedetailsComponent } from './servicedetails/servicedetails.component';
import { BusinessComponent } from './business/business.component';
import { BslistComponent } from './bslist/bslist.component';
import { RegisterComponent } from './register/register.component';
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from './api.service';
import { FormsModule } from '@angular/forms';
import { NgProgressModule } from '@ngx-progressbar/core';
import { NgProgressHttpClientModule } from '@ngx-progressbar/http-client';


@NgModule({
  declarations: [
    AppComponent,
    BusinessComponent,
    BslistComponent,
    RegisterComponent,
    LoginComponent,
    ServicedetailsComponent,
  ],
  
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    NgProgressModule.forRoot(),
    NgProgressHttpClientModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
