import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import { BusinessComponent } from './business/business.component';
import { BslistComponent } from './bslist/bslist.component';

import { RegisterComponent } from './register/register.component'


@NgModule({
  declarations: [
    AppComponent,
    BusinessComponent,
    BslistComponent,
    RegisterComponent,
front_development
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
