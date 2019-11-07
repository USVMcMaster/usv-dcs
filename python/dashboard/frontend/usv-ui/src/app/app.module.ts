import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AgmCoreModule } from '@agm/core';
import { AppComponent } from './app.component';
import { NgOpenCVModule } from 'ng-open-cv';
import { MatCardModule, MatGridListModule, MatButtonModule } from '@angular/material';
// import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs'
    }),
    NgOpenCVModule,
    MatCardModule,
    MatGridListModule,
    MatButtonModule,
    // BrowserAnimationsModule
  ],
  exports: [NgOpenCVModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
